---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-08_http-chunk-extension-processing-vulnerabilities.md
original_filename: 2024-01-08_http-chunk-extension-processing-vulnerabilities.md
title: HTTP Chunk Extension Processing Vulnerabilities
category: documents
detected_topics:
- command-injection
- otp
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- otp
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: fc501d89d1cee9c9d131c6c9c0c858422f557e9372bc768a098c15583b72187a
text_sha256: f83969389590e67146d470ffa7fa6027b3ef7b3989cd2507f06528a5f2313405
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# HTTP Chunk Extension Processing Vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-08_http-chunk-extension-processing-vulnerabilities.md
- Source Type: markdown
- Detected Topics: command-injection, otp, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `fc501d89d1cee9c9d131c6c9c0c858422f557e9372bc768a098c15583b72187a`
- Text SHA256: `f83969389590e67146d470ffa7fa6027b3ef7b3989cd2507f06528a5f2313405`


## Content

---
title: "HTTP Chunk Extension Processing Vulnerabilities"
page_title: "HTTP Chunk Extension Processing Vulnerabilities - nowotarski.info"
url: "https://nowotarski.info/http-chunk-extensions/"
final_url: "https://nowotarski.info/http-chunk-extensions/"
authors: ["Bartek Nowotarski"]
programs: ["Golang", "Node.js", "Hyper (Rust HTTP library)", "Puma (Rails HTTP library)"]
bugs: ["HTTP/2 CONTINUATION Flood", "DoS"]
publication_date: "2024-01-08"
added_date: "2024-08-14"
source: "pentester.land/writeups.json"
original_index: 569
---

# HTTP Chunk Extension Processing Vulnerabilities

Posted on January 8, 2024 by Bartek Nowotarski 

[__](https://x.com/bartn_/status/1758515957318697104)

**tl;dr:** I discovered a family of vulnerabilities in major projects including Golang, Node.js, Hyper (Rust HTTP library), and Puma (Rails HTTP library). Invalid processing of HTTP chunk extensions created an amplification vector for server reads which allowed DoS attacks caused by network bandwidth or CPU exhaustion. 

# What are chunk extensions?

A chunk extension can be added to a data chunk in HTTP/1.1 to extend it with some metadata connected to a given chunk. But what are chunks and chunk encoding in general? Let’s look into [RFC9112](https://datatracker.ietf.org/doc/html/rfc9112#name-chunk-extensions):

> The chunked coding allows each chunk to include zero or more chunk extensions, immediately following the chunk-size, for the sake of supplying per-chunk metadata (such as a signature or hash), mid-message control information, or randomization of message body size.

On the wire, chunks look like this:
  
  
  [chunk size in hex]\r\n
  [chunk]\r\n
  [2nd chunk size in hex]\r\n
  [2nd chunk]\r\n
  ...
  0\r\n
  

The first line contains the chunk size in hex which is followed by another line with the actual chunk data. With extensions it will look like this:
  
  
  [chunk size in hex];extension_name=extension_value\r\n
  [chunk]\r\n
  [2nd chunk size in hex];extension_name=extension_value\r\n
  [2nd chunk]\r\n
  ...
  0\r\n
  

According to RFC9112:

> A server ought to limit the total length of chunk extensions received in a request to an amount reasonable for the services provided, in the same way that it applies length limitations and timeouts for other parts of a message, and generate an appropriate 4xx (Client Error) response if that amount is exceeded.

# Vulnerability

It turns out that Node.js, Golang’s `net/http`, along with many other HTTP server libraries, do not properly limit the number of bytes sent in chunk extensions.

After reviewing _a lot_ of HTTP libraries when researching this bug I think I can separate this vulnerability into two types:

  1. The first type involves HTTP libraries that do not limit the extension size **at all** , allowing an attacker to stream numerous bytes in the chunk extension. This can result in either the server crashing due to out-of-memory errors or the unnecessary consumption of CPU/network resources, which slows down other clients.
  2. The second type relates to HTTP libraries with a very high limit for the extension string, which can be exploited using 1-byte chunks.

## Node.js (and llhttp)

Node.js had an issue falling into the first, more severe category. It has been using [`llhttp`](https://github.com/nodejs/llhttp) internally for HTTP parsing. `llhttp` has a set of callback events defined, which upstream software can use to subscribe to HTTP parsing events like `on_url_complete` (invoked after the URL has been parsed) or `on_header_field_complete` (invoked after a header name has been parsed). It also has a set of events connected to chunk encoding and chunk extensions:

  * `on_chunk_header`: Invoked after a new chunk is started.
  * `on_chunk_extension_name_complete`: Invoked after a chunk extension name is started.
  * `on_chunk_extension_value_complete`: Invoked after a chunk extension value is started.
  * `on_chunk_complete`: Invoked after a new chunk is received.

Apps which use `llhttp` must initialize it with `llhttp_settings_t` struct and assign callback functions for desired events. In Node.js it looked like this:
  
  
  1const llhttp_settings_t Parser::settings = {
  2  Proxy<Call, &Parser::on_message_begin>::Raw,
  3  Proxy<DataCall, &Parser::on_url>::Raw,
  4  Proxy<DataCall, &Parser::on_status>::Raw,
  5  // on_method
  6  nullptr,
  7  // on_version
  8  nullptr,
  9  Proxy<DataCall, &Parser::on_header_field>::Raw,
  10  Proxy<DataCall, &Parser::on_header_value>::Raw,
  11  // on_chunk_extension_name
  12  nullptr,
  13  // on_chunk_extension_value
  14  nullptr,
  15  Proxy<Call, &Parser::on_headers_complete>::Raw,
  16  Proxy<DataCall, &Parser::on_body>::Raw,
  17  Proxy<Call, &Parser::on_message_complete>::Raw,
  18  // on_url_complete
  19  nullptr,
  20  // on_status_complete
  21  nullptr,
  22  // on_method_complete
  23  nullptr,
  24  // on_version_complete
  25  nullptr,
  26  // on_header_field_complete
  27  nullptr,
  28  // on_header_value_complete
  29  nullptr,
  30  // on_chunk_extension_name_complete
  31  nullptr,
  32  // on_chunk_extension_value_complete
  33  nullptr,
  34  Proxy<Call, &Parser::on_chunk_header>::Raw,
  35  Proxy<Call, &Parser::on_chunk_complete>::Raw,
  36  // on_reset,
  37  nullptr,
  38};

Highlighted lines indicate that `on_chunk_extension_name` and `on_chunk_extension_value` callbacks are not set. Because of this Node.js was unable to check what were the extension name and value lengths. What’s worse: standard methods of limiting the requests like timeouts or max body size did not work in this case! `llhttp` was reading chunk extensions indefinitely.

Interestingly, it seems that chunk extension support was added to `llhttp` around 2022 via [http: added chunked extensions parsing and related callbacks](https://github.com/nodejs/llhttp/commit/13541bd127b36ae1a5d15355cf9b8442b929a36c) commit. The `llhttp_settings_t` struct changed, and I believe both callbacks were set to `nullptr` so the code can compile again.

This vulnerability has been assigned [CVE-2024-22019](https://nodejs.org/en/blog/vulnerability/february-2024-security-releases#reading-unprocessed-http-request-with-unbounded-chunk-extension-allows-dos-attacks-cve-2024-22019---high).

## Golang

The Golang falls into the second category. It allowed up to 4096 bytes per chunk extension, which is the default buffer size of `bufio.Reader`. This means that by sending 1 byte chunks the server had to read additional 4096 bytes! This occurred even if the handler did not read the request body at all, as Golang always reads up to a ~262 kB of the body to support some old HTTP clients which can deadlock if the server does not read the entire request. To sum it up it was possible to make every Golang HTTP server waste its resources by reading more than 1GB of data! Let’s dig into the code!

### net/http.chunkWriter.writeHeader

First, let’s see how Go handles discarding a request body that was not fully (or never) read in the handler of a request. It does so because (according to a comment in this function) some clients can deadlock because they wait for the body to be fully read until sending the next request.

This is done in `net/http/server.go`, starting at line [1376](https://github.com/golang/go/blob/go1.21.3/src/net/http/server.go#L1376) (go 1.21.3):
  
  
  1369// We do this by default because there are a number of clients that
  1370// send a full request before starting to read the response, and they
  1371// can deadlock if we start writing the response with unconsumed body
  1372// remaining. See Issue 15527 for some history.
  1373//
  1374// If full duplex mode has been enabled with ResponseController.EnableFullDuplex,
  1375// then leave the request body alone.
  1376if w.req.ContentLength != 0 && !w.closeAfterReply && !w.fullDuplex {
  1377  var discard, tooBig bool
  1378
  1379  switch bdy := w.req.Body.(type) {
  1380  case *expectContinueReader:
  1381  if bdy.resp.wroteContinue {
  1382  discard = true
  1383  }
  1384  case *body:
  1385  bdy.mu.Lock()
  1386  switch {
  1387  case bdy.closed:
  1388  if !bdy.sawEOF {
  1389  // Body was closed in handler with non-EOF error.
  1390  w.closeAfterReply = true
  1391  }
  1392  case bdy.unreadDataSizeLocked() >= maxPostHandlerReadBytes:
  1393  tooBig = true
  1394  default:
  1395  discard = true
  1396  }
  1397  bdy.mu.Unlock()
  1398  default:
  1399  discard = true
  1400  }
  1401
  1402  if discard {
  1403  _, err := io.CopyN(io.Discard, w.reqBody, maxPostHandlerReadBytes+1)
  1404  switch err {
  1405  case nil:
  1406  // There must be even more data left over.
  1407  tooBig = true
  1408  case ErrBodyReadAfterClose:
  1409  // Body was already consumed and closed.
  1410  case io.EOF:
  1411  // The remaining body was just consumed, close it.
  1412  err = w.reqBody.Close()
  1413  if err != nil {
  1414  w.closeAfterReply = true
  1415  }
  1416  default:
  1417  // Some other kind of error occurred, like a read timeout, or
  1418  // corrupt chunked encoding. In any case, whatever remains
  1419  // on the wire must not be parsed as another HTTP request.
  1420  w.closeAfterReply = true
  1421  }
  1422  }
  1423
  1424  if tooBig {
  1425  w.requestTooLarge()
  1426  delHeader("Connection")
  1427  setHeader.connection = "close"
  1428  }
  1429}

To be able to exploit the vulnerability we must ensure `discard` is set to `true`. This will make Go read/discard body bytes. Let’s start with the first condition that will get us there:
  
  
  if w.req.ContentLength != 0 && !w.closeAfterReply && !w.fullDuplex
  

It is `true` for simplest requests with `Transfer-Encoding: chunked` header. Note that the vulnerability will not trigger if `w.fullDuplex` is true, but it is rare because it requires the usage of `ResponseController.EnableFullDuplex` which was added in Go 1.21.

If additional conditions are valid (lines 1379-1400) and the `discard` variable is finally set to `true` Go will run the code in line 1403:
  
  
  _, err := io.CopyN(io.Discard, w.reqBody, maxPostHandlerReadBytes+1)
  

In short, it will read and discard up to `maxPostHandlerReadBytes` (256 « 10 ~= 0.25MB) bytes. In the following section, I will explain that this is not always true and how more than 1GB of data can be read automatically by an HTTP server.

### net/http/internal.chunkedReader

If `Transfer-Encoding: chunked` header is present in the request then the second argument to `io.CopyN` (`w.reqBody`) from the previous section is of type `net/http.body` which wraps `chunkedReader`. So when `io.CopyN` reads that it reads it from a `chunkedReader` instance.

`chunkReader` implements `io.Reader` interface so its `Read` method inserts data to the provided `[]byte` slice and returns `n` which indicates a number of bytes inserted to `[]byte`. So `n` indicates a number of bytes inserted to `[]byte` but **not** a number of bytes read from internal `*bufio.Reader` (`chunkedReader.r`).

Let’s check the simplest example of a chunked body:
  
  
  9\r\n
  abcdefgh\r\n
  

You can guess that `chunkedReader.Read` returned `(9, nil)` values but internally it read 15 bytes. At this point, this is not a big deal because even if we send 1-byte chunks the chunked encoding overhead will be 5 extra bytes, for example:
  
  
  1\r\n
  a\r\n
  

So ultimately we’d send 5 times `maxPostHandlerReadBytes` so around 1.25MB.

The problem appears if we use “chunk extensions”. See `net/http/internal.removeChunkExtension` function godoc which is run for every chunk length line:
  
  
  // removeChunkExtension removes any chunk-extension from p.
  // For example,
  //
  // "0" => "0"
  // "0;token" => "0"
  // "0;token=val" => "0"
  // `0;token="quoted string"` => "0"
  func removeChunkExtension(p []byte) ([]byte, error) {
  p, _, _ = bytes.Cut(p, semi)
  // TODO: care about exact syntax of chunk extensions? We're
  // ignoring and stripping them anyway. For now just never
  // return an error.
  return p, nil
  }
  

So for every chunk, we can add up to 4096 bytes (`bufio.Reader` buffer) which will be read but removed.

To sum it up, it was possible for every Golang HTTP server to waste its resources by reading 1.073 GB of data, which is calculated as follows: 4096 (bytes per chunk) x 262144 (allowed body size) bytes = 1073741824 bytes.

This vulnerability has been assigned [CVE-2023-39326](https://pkg.go.dev/vuln/GO-2023-2382) and fixed in [Go 1.21.5 and Go 1.20.12](https://groups.google.com/g/golang-announce/c/iLGK3x6yuNo/m/z6MJ-eB0AQAJ).

# Is my server vulnerable?

  * Go: YES, [CVE-2023-39326](https://pkg.go.dev/vuln/GO-2023-2382) (fixed in [Go 1.21.5 and Go 1.20.12](https://groups.google.com/g/golang-announce/c/iLGK3x6yuNo/m/z6MJ-eB0AQAJ))
  * Rails (Puma): YES, [CVE-2024-21647](https://github.com/puma/puma/security/advisories/GHSA-c2f4-cvqm-65w2), [Security Advisory](https://github.com/puma/puma/security/advisories/GHSA-c2f4-cvqm-65w2) (fixed in 6.4.2 and 5.6.8.)
  * Rust (Hyper): YES (fixed in [v1.1.0](https://github.com/hyperium/hyper/releases/tag/v1.1.0))
  * Node.js: YES, [CVE-2024-22019](https://nodejs.org/en/blog/vulnerability/february-2024-security-releases#reading-unprocessed-http-request-with-unbounded-chunk-extension-allows-dos-attacks-cve-2024-22019---high)
  * nginx: NO (latest release at a time of check: 1.24.0 was not vulnerable but versions before 1.19.2 are vulnerable)
  * Apache httpd: NO

# More to come…

Unfortunately, this vulnerability seems to be very common. I reported it to multiple projects so I will update this post as fixes are published. That’s why I’m also not publishing the exploit yet.
