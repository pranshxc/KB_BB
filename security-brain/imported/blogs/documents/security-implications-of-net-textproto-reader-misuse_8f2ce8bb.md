---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-03-05_security-implications-of-nettextprotoreader-misuse.md
original_filename: 2024-03-05_security-implications-of-nettextprotoreader-misuse.md
title: Security Implications of net/textproto.Reader Misuse
category: documents
detected_topics:
- supply-chain
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- supply-chain
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: 8f2ce8bb28888c0f395ddf4bcb747826ddbc0af844cdf6016eb8a54c73c9c466
text_sha256: 666f775520663b1827902c797983ff2a9c020ee855c96fb04f8fd44794009721
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: false
---

# Security Implications of net/textproto.Reader Misuse

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-03-05_security-implications-of-nettextprotoreader-misuse.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: False
- Raw SHA256: `8f2ce8bb28888c0f395ddf4bcb747826ddbc0af844cdf6016eb8a54c73c9c466`
- Text SHA256: `666f775520663b1827902c797983ff2a9c020ee855c96fb04f8fd44794009721`


## Content

---
title: "Security Implications of net/textproto.Reader Misuse"
page_title: "Security Implications of net/textproto.Reader Misuse - nowotarski.info"
url: "https://nowotarski.info/golang-textproto-reader/"
final_url: "https://nowotarski.info/golang-textproto-reader/"
authors: ["Bartek Nowotarski (@bartn_)"]
programs: ["Golang"]
bugs: ["Out Of Memory crash", "Memory leak", "Security code review"]
publication_date: "2024-03-05"
added_date: "2024-08-14"
source: "pentester.land/writeups.json"
original_index: 394
---

# Security Implications of `net/textproto.Reader` Misuse

Posted on March 5, 2024 by Bartek Nowotarski 

[__](https://x.com/bartn_/status/1765083174009544720)

**tl;dr:** `net/textproto.Reader` should be only used with `io.LimitReader`. It turns out that often this is not the case, even in Golang standard library. This caused Out Of Memory crash vulnerabilities in Golang `net/http` package (CVE-2023-45290) and other open-source projects. 

**Table of Contents**

  * Infinite read in `net/textproto.Reader`
  * CodeQL query to find `net/textproto.Reader` usage
  * Misuse in `net/http.ReadRequest`
  * Other usages in Golang
  * Vulnerability in `http.Request.FormValue` leads to OOM crash
  * Linking `readMIMEHeader` in `mime/multipart`
  * Parsing multipart form data format using `ParseMultipartForm`
  * Exploiting the lack of read limits in `net/http.Request.FormValue`

# Infinite read in `net/textproto.Reader`

In September 2023 I discovered an issue in Golang’s [`net/textproto.Reader`](https://pkg.go.dev/net/textproto#Reader). In one of its internal methods (`readLineSlice`), the code (in an infinite loop) reads data from `bufio.Reader` and concatenates to `line`: previously read data. It is using `ReadLine` which behaves differently from other `bufio.Reader` methods: this is the only method that does not return an error when internal the buffer fills full. Instead, when the buffer becomes full it returns `more=true` value which indicates there is more data to be read.
  
  
  52func (r *Reader) readLineSlice() ([]byte, error) {
  53	r.closeDot()
  54	var line []byte
  55	for {
  56		l, more, err := r.R.ReadLine()
  57		if err != nil {
  58  return nil, err
  59		}
  60		// Avoid the copy if the first call produced a full line.
  61		if line == nil && !more {
  62  return l, nil
  63		}
  64		line = append(line, l...)
  65		if !more {
  66  break
  67		}
  68	}
  69	return line, nil
  70}

If a very long line is passed to this method, it will be read into memory until `\n` is found which can lead to an OOM crash. However, [`net/textproto.NewReader`](https://pkg.go.dev/net/textproto#NewReader) godoc explicitly mentions this case:

> NewReader returns a new Reader reading from r.
> 
> To avoid denial of service attacks, the provided bufio.Reader should be reading from an io.LimitReader or similar Reader to bound the size of responses.

## CodeQL query to find `net/textproto.Reader` usage

Out of curiosity, I used CodeQL to find projects which use `net/textproto.Reader`. Below you can find CodeQL query to check if your code _might_ be vulnerable (if used without `io.LimitReader` or a similar limiter).
  
  
  1import go
  2
  3predicate textprotoFunction(CallExpr cs, string name) {
  4  cs.getTarget().(Function).hasQualifiedName("net/textproto", name)
  5}
  6
  7predicate textprotoReaderMethod(CallExpr cs, string name) {
  8  cs.getTarget().(Method).hasQualifiedName("net/textproto", "Reader", name)
  9}
  10
  11class TextProto extends CallExpr {
  12  TextProto() {
  13  textprotoFunction(this, "Dial") or
  14  textprotoFunction(this, "NewConn") or
  15  textprotoFunction(this, "NewReader") or
  16  textprotoReaderMethod(this, "ReadLine") or
  17  textprotoReaderMethod(this, "ReadLineBytes") or
  18  textprotoReaderMethod(this, "ReadContinuedLine") or
  19  textprotoReaderMethod(this, "ReadContinuedLineBytes") or
  20  textprotoReaderMethod(this, "ReadResponse") or
  21  textprotoReaderMethod(this, "ReadCodeLine") or
  22  textprotoReaderMethod(this, "ReadDotBytes") or
  23  textprotoReaderMethod(this, "ReadDotLines") or
  24  textprotoReaderMethod(this, "ReadMIMEHeader")
  25  }
  26}
  27
  28from TextProto call
  29select call, "Direct usage of textproto.Reader methods"
  

Unfortunately, this query will not find all the cases and will give false positives.

First, it doesn’t check if the provided `bufio.Reader` is using `io.LimitReader` internally (and if it’s `N` value makes sense). Second, I discovered that `textproto` is used in some HTTP helper packages and CodeQL is unable to find cross-repository calls. Finally, kind of connected to the previous one, `textproto.Reader` is used internally in other standard packages of Golang.

## Misuse in `net/http.ReadRequest`

Turns out that misusing this API is very common, even in Golang standard library. The `net/textproto.Reader` is used in [`net/http.ReadRequest`](https://cs.opensource.google/go/go/+/refs/tags/go1.21.6:src/net/http/request.go;l=1023) and its godoc does not even mention `io.LimitReader`:
  
  
  1017// ReadRequest reads and parses an incoming request from b.
  1018//
  1019// ReadRequest is a low-level function and should only be used for
  1020// specialized applications; most code should use the Server to read
  1021// requests and handle them via the Handler interface. ReadRequest
  1022// only supports HTTP/1.x requests. For HTTP/2, use golang.org/x/net/http2.
  1023func ReadRequest(b *bufio.Reader) (*Request, error) {
  1024	req, err := readRequest(b)
  1025	if err != nil {
  1026		return nil, err
  1027	}
  1028
  1029	delete(req.Header, "Host")
  1030	return req, err
  1031}
  1032
  1033func readRequest(b *bufio.Reader) (req *Request, err error) {
  1034	tp := newTextprotoReader(b)
  1035	defer putTextprotoReader(tp)
  1036
  1037	req = new(Request)
  1038
  1039	// First line: GET /index.html HTTP/1.0
  1040	var s string
  1041	if s, err = tp.ReadLine(); err != nil {
  1042		return nil, err
  1043	}
  1044	defer func() {
  1045		if err == io.EOF {
  1046  err = io.ErrUnexpectedEOF
  1047		}
  1048	}()
  1049// ...
  

To exploit this, an attacker can simply send an infinite byte stream in the first line of an HTTP request and they will all be loaded into memory, ultimately crashing the server.

As mentioned before, some HTTP servers and helper packages use this function without limiters. Most notably [Caddy](https://github.com/caddyserver/caddy/commit/58ab3a01a0d4b5f9e8bff56f623ceb906ff603b9) which was fixed in v2.7.5 after my report. There are more cases like this but my reports were ignored or simply have not been fixed months after the initial report.

## Other usages in Golang

Here’s a list of **public** methods that use `textproto.Reader` on a provided arguments found using my CodeQL query on Golang 1.21.5:

  * `net/http.ReadResponse` and methods in which it’s used internally: 
  * `rpc.DialHTTP`
  * `rpc.DialHTTPPath`
  * ~~`net/http/httputil.ClientConn.Read`~~ (marked as deprecated)
  * `net/http.ReadRequest` (previous section) 
  * ~~`net/http/httputil.ServerConn.Read`~~ (marked as deprecated)
  * `mail.ReadMessage`
  * `smtp.NewClient`
  * `smtp.StartTLS`

I reported it to Golang team but they decided not to fix and improve docs instead. Except `net/http` cases, I agree with this decision: either some obscure use cases were required to trigger the vulnerable code (like a proxy used to make HTTP request had to respond in a rogue way) or the code was in deprecated packages.

Nevertheless, be extra cautious when using any of the functions above in production code!

# Vulnerability in `http.Request.FormValue` leads to OOM crash

Months have passed and I almost forgot about the issue but one day I noticed that there was one more usage of `textproto.Reader` my CodeQL query would never find…

## Linking `readMIMEHeader` in `mime/multipart`

I was checking the `mime/multipart` package and noticed a file (`readmimeheader.go`) with just a couple lines:
  
  
  1// Copyright 2023 The Go Authors. All rights reserved.
  2// Use of this source code is governed by a BSD-style
  3// license that can be found in the LICENSE file.
  4package multipart
  5
  6import (
  7	"net/textproto"
  8	_ "unsafe" // for go:linkname
  9)
  10
  11// readMIMEHeader is defined in package net/textproto.
  12//
  13//go:linkname readMIMEHeader net/textproto.readMIMEHeader
  14func readMIMEHeader(r *textproto.Reader, lim int64) (textproto.MIMEHeader, error)

So basically `mime/multipart` was using a function from `net/textproto` but instead of using the public API, it linked a private function. Why was it done this way? Maybe to avoid circular dependency? But there was no way my CodeQL query could find it, that’s why I’ve missed it!

## Parsing multipart form data format using `ParseMultipartForm`

Anyway, this function is using `readLineSlice` internally and is used by `mime/multipart.Reader.populateHeaders` method:
  
  
  152func (p *Part) populateHeaders(maxMIMEHeaderSize int64) error {
  153	r := textproto.NewReader(p.mr.bufReader)
  154	header, err := readMIMEHeader(r, maxMIMEHeaderSize)
  155	if err == nil {
  156		p.Header = header
  157	}
  158	// TODO: Add a distinguishable error to net/textproto.
  159	if err != nil && err.Error() == "message too large" {
  160		err = ErrMessageTooLarge
  161	}
  162	return err
  163}

What does it do? It parses multipart form data (when `Content-Type` is `multipart/form-data`). Here’s a quick reminder how a request with a multipart body looks like:
  
  
  1POST / HTTP/1.0
  2Host: localhost
  3Content-Type: multipart/form-data; boundary=----boundary
  4Content-Length: 16525
  5
  6------boundary
  7Content-Disposition: form-data; name="data1"
  8Content-Type: text/plain
  9
  10data here
  11
  12------boundary
  13Content-Disposition: form-data; name="data2"
  14Content-Type: text/plain
  15
  16data there
  

Thus, a body can consist of multiple _parts_ , each of which can be of a different type and each part has a set of headers. Turns out, each part’s headers in multipart data are parsed by a function from `net/textproto` package, the one which can lead to vulnerabilities if not used properly.

I quickly checked if `io.LimitReader` was used internally and it was not, however [`multipart.NewReader`](https://pkg.go.dev/mime/multipart#NewReader) accepts `io.Reader`. This means that the caller must ensure that `io.Reader` should be in fact an `io.LimitReader`. Similarly to other functions I reported in September 2023, this one is also missing this essential information in godoc.

Additionally, `populateHeaders` requires `maxMIMEHeaderSize` argument which is passed to `readMIMEHeader`. However, this argument is only taken into account **after** reading the headers using vulnerable methods. So it should not be a problem _if_ there is a vulnerability connected to this method.

Obviously, the next step was checking if `mime/multipart.Reader` is used anywhere in Go codebase. A quick search revealed that it is only used by [`net/http.Request.ParseMultipartForm`](https://pkg.go.dev/net/http#Request.ParseMultipartForm). But there was a gotcha: it required `maxMemory`, explained in godoc:
  
  
  1316// ParseMultipartForm parses a request body as multipart/form-data.
  1317// The whole request body is parsed and up to a total of maxMemory bytes of
  1318// its file parts are stored in memory, with the remainder stored on
  1319// disk in temporary files.
  1320// ParseMultipartForm calls ParseForm if necessary.
  1321// If ParseForm returns an error, ParseMultipartForm returns it but also
  1322// continues parsing the request body.
  1323// After one call to ParseMultipartForm, subsequent calls have no effect.
  1324func (r *Request) ParseMultipartForm(maxMemory int64) error {
  1325	if r.MultipartForm == multipartByReader {
  1326		return errors.New("http: multipart handled by MultipartReader")
  1327	}
  1328	var parseFormErr error
  1329	if r.Form == nil {
  1330		// Let errors in ParseForm fall through, and just
  1331		// return it at the end.
  1332		parseFormErr = r.ParseForm()
  1333	}
  1334	if r.MultipartForm != nil {
  1335		return nil
  1336	}
  1337
  1338	mr, err := r.multipartReader(false)
  1339	if err != nil {
  1340		return err
  1341	}
  1342
  1343	f, err := mr.ReadForm(maxMemory)
  1344	if err != nil {
  1345		return err
  1346	}
  1347// ...
  

So everything below `maxMemory` with default value of:
  
  
  1defaultMaxMemory = 32 << 20 // 32 MB
  

would be stored in memory, the rest on disk. However, if one can exploit `readMIMEHeader` method, it’s possible to store more data in memory…

## Exploiting the lack of read limits in `net/http.Request.FormValue`

A couple of CodeQL queries later I discovered that `net/http.Request.ParseMultipartForm` is used by `net/http.Request.FormValue` which is a pretty common method even for small Golang apps.

The call stack to reach `readMIMEHeader` was looking like this:

  * `net/http.Request.FormValue`
  * `net/http.Request.ParseMultipartForm`
  * `mime/multipart.Reader.ReadForm`
  * `mime/multipart.Reader.readForm`
  * `mime/multipart.Reader.nextPart`
  * `mime/multipart.nextPart`
  * `mime/multipart.populateHeaders`
  * `mime/multipart.readMIMEHeader`

At this point, the last remaining part to call this a **vulnerability** was checking if `multipart.Reader` created in `net/http.Request.ParseMultipartForm` is indeed a `io.LimitReader`. The easiest way was simply writing a test case and setting a proper breakpoint in a debugger.

Turns out that the reader type is `net/http.body` which internally reads from `io.LimitReader`. However, its `N` value is set to… `Content-Length` header and it’s value is never checked! What we can do is send an HTTP request with a very large `Content-Length` value (like 2GiB) followed by a single part with an infinite header name, like this:
  
  
  POST / HTTP/1.0
  Host: localhost
  Content-Type: multipart/form-data; boundary=----boundary
  Content-Length: 2147483648
  
  ------boundary
  Content-Disposition: form-data; name="text1"
  Content-Type: text/plain
  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.......
  

The issue was assigned the [CVE-2023-45290](https://pkg.go.dev/vuln/GO-2024-2599) number and was [fixed](https://github.com/golang/go/commit/041a47712e765e94f86d841c3110c840e76d8f82) in Golang 1.21.8 and 1.22.1.
