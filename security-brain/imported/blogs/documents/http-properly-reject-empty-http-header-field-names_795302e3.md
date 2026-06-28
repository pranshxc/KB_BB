---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-14_http-properly-reject-empty-http-header-field-names.md
original_filename: 2023-02-14_http-properly-reject-empty-http-header-field-names.md
title: 'http: properly reject empty http header field names'
category: documents
detected_topics:
- sso
- access-control
- command-injection
- automation-abuse
tags:
- imported
- documents
- sso
- access-control
- command-injection
- automation-abuse
language: en
raw_sha256: 795302e375375bf3336d55bc987197b5bd01ee585fe8b886cb458125267579f3
text_sha256: bf8abb5768056d56a3c75f1f87a18de3ceca784dafb1665ecf7d194c2d48fada
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# http: properly reject empty http header field names

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-14_http-properly-reject-empty-http-header-field-names.md
- Source Type: markdown
- Detected Topics: sso, access-control, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `795302e375375bf3336d55bc987197b5bd01ee585fe8b886cb458125267579f3`
- Text SHA256: `bf8abb5768056d56a3c75f1f87a18de3ceca784dafb1665ecf7d194c2d48fada`


## Content

---
title: "http: properly reject empty http header field names"
page_title: "BUG/CRITICAL: http: properly reject empty http header field names · haproxy/haproxy@a8598a2 · GitHub"
url: "https://github.com/haproxy/haproxy/commit/a8598a2eb11b6c989e81f0dbf10be361782e8d32"
final_url: "https://github.com/haproxy/haproxy/commit/a8598a2eb11b6c989e81f0dbf10be361782e8d32"
authors: ["Bahruz Jabiyev (@BahruzJabiyev)", "Anthony Gavazzi", "Engin Kirda", "Kaan Onarlioglu", "Adi Peleg", "Harvey Tuch"]
programs: ["HAProxy"]
bugs: ["HTTP header attack", "HTTP request smuggling", "Access control bypass"]
publication_date: "2023-02-14"
added_date: "2023-02-26"
source: "pentester.land/writeups.json"
original_index: 1529
---

###  Uh oh! 

There was an error while loading. [Please reload this page]().

[ haproxy ](/haproxy) / **[haproxy](/haproxy/haproxy) ** Public

  * [ Notifications ](/login?return_to=%2Fhaproxy%2Fhaproxy) You must be signed in to change notification settings
  * [ Fork 942 ](/login?return_to=%2Fhaproxy%2Fhaproxy)
  * [ Star  6.7k ](/login?return_to=%2Fhaproxy%2Fhaproxy)

  * [ Code ](/haproxy/haproxy)
  * [ Issues 365 ](/haproxy/haproxy/issues)
  * [ Discussions ](/haproxy/haproxy/discussions)
  * [ Actions ](/haproxy/haproxy/actions)
  * [ Projects ](/haproxy/haproxy/projects)
  * [ Wiki ](/haproxy/haproxy/wiki)
  * [ Security and quality 0 ](/haproxy/haproxy/security)
  * [ Insights ](/haproxy/haproxy/pulse)

Additional navigation options

  * [ Code  ](/haproxy/haproxy)
  * [ Issues  ](/haproxy/haproxy/issues)
  * [ Discussions  ](/haproxy/haproxy/discussions)
  * [ Actions  ](/haproxy/haproxy/actions)
  * [ Projects  ](/haproxy/haproxy/projects)
  * [ Wiki  ](/haproxy/haproxy/wiki)
  * [ Security and quality  ](/haproxy/haproxy/security)
  * [ Insights  ](/haproxy/haproxy/pulse)

# Commit a8598a2

[Browse files](/haproxy/haproxy/tree/a8598a2eb11b6c989e81f0dbf10be361782e8d32)[](/haproxy/haproxy/tree/a8598a2eb11b6c989e81f0dbf10be361782e8d32)Browse files

[![wtarreau](https://avatars.githubusercontent.com/u/8141789?v=4&size=40)](/wtarreau)[wtarreau](/haproxy/haproxy/commits?author=wtarreau)

committed

BUG/CRITICAL: http: properly reject empty http header field names

The HTTP header parsers surprizingly accepts empty header field names, and this is a leftover from the original code that was agnostic to this. When muxes were introduced, for H2 first, the HPACK decompressor needed to feed headers lists, and since empty header names were strictly forbidden by the protocol, the lists of headers were purposely designed to be terminated by an empty header field name (a principle that is similar to H1's empty line termination). This principle was preserved and generalized to other protocols migrated to muxes (H1/FCGI/H3 etc) without anyone ever noticing that the H1 parser was still able to deliver empty header field names to this list. In addition to this it turns out that the HPACK decompressor, despite a comment in the code, may successfully decompress an empty header field name, and this mistake was propagated to the QPACK decompressor as well. The impact is that an empty header field name may be used to truncate the list of headers and thus make some headers disappear. While for H2/H3 the impact is limited as haproxy sees a request with missing headers, and headers are not used to delimit messages, in the case of HTTP/1, the impact is significant because the presence (and sometimes contents) of certain sensitive headers is detected during the parsing. Thus, some of these headers may be seen, marked as present, their value extracted, but never delivered to upper layers and obviously not forwarded to the other side either. This can have for consequence that certain important header fields such as Connection, Upgrade, Host, Content-length, Transfer-Encoding etc are possibly seen as different between what haproxy uses to parse/forward/route and what is observed in http-request rules and of course, forwarded. One direct consequence is that it is possible to exploit this property in HTTP/1 to make affected versions of haproxy forward more data than is advertised on the other side, and bypass some access controls or routing rules by crafting extraneous requests. Note, however, that responses to such requests will normally not be passed back to the client, but this can still cause some harm. This specific risk can be mostly worked around in configuration using the following rule that will rely on the bug's impact to precisely detect the inconsistency between the known body size and the one expected to be advertised to the server (the rule works from 2.0 to 2.8-dev): http-request deny if { fc_http_major 1 } !{ req.body_size 0 } !{ req.hdr(content-length) -m found } !{ req.hdr(transfer-encoding) -m found } !{ method CONNECT } This will exclusively block such carefully crafted requests delivered over HTTP/1. HTTP/2 and HTTP/3 do not need content-length, and a body that arrives without being announced with a content-length will be forwarded using transfer-encoding, hence will not cause discrepancies. In HAProxy 2.0 in legacy mode ("no option http-use-htx"), this rule will simply have no effect but will not cause trouble either. A clean solution would consist in modifying the loops iterating over these headers lists to check the header name's pointer instead of its length (since both are zero at the end of the list), but this requires to touch tens of places and it's very easy to miss one. Functions such as htx_add_header(), htx_add_trailer(), htx_add_all_headers() would be good starting points for such a possible future change. Instead the current fix focuses on blocking empty headers where they are first inserted, hence in the H1/HPACK/QPACK decoders. One benefit of the current solution (for H1) is that it allows "show errors" to report a precise diagnostic when facing such invalid HTTP/1 requests, with the exact location of the problem and the originating address: $ printf "GET / HTTP/1.1\r\nHost: localhost\r\n:empty header\r\n\r\n" | nc 0 8001 HTTP/1.1 400 Bad request Content-length: 90 Cache-Control: no-cache Connection: close Content-Type: text/html <html><body><h1>400 Bad request</h1> Your browser sent an invalid request. </body></html> $ socat /var/run/haproxy.stat <<< "show errors" Total events captured on [10/Feb/2023:16:29:37.530] : 1 [10/Feb/2023:16:29:34.155] frontend decrypt ([#2](https://github.com/haproxy/haproxy/issues/2)): invalid request backend <NONE> (#-1), server <NONE> (#-1), event #0, src 127.0.0.1:31092 buffer starts at 0 (including 0 out), 16334 free, len 50, wraps at 16336, error at position 33 H1 connection flags 0x00000000, H1 stream flags 0x00000810 H1 msg state MSG_HDR_NAME(17), H1 msg flags 0x00001410 H1 chunk len 0 bytes, H1 body len 0 bytes : 00000 GET / HTTP/1.1\r\n 00016 Host: localhost\r\n 00033 :empty header\r\n 00048 \r\n I want to address sincere and warm thanks for their great work to the team composed of the following security researchers who found the issue together and reported it: Bahruz Jabiyev, Anthony Gavazzi, and Engin Kirda from Northeastern University, Kaan Onarlioglu from Akamai Technologies, Adi Peleg and Harvey Tuch from Google. And kudos to Amaury Denoyelle from HAProxy Technologies for spotting that the HPACK and QPACK decoders would let this pass despite the comment explicitly saying otherwise. This fix must be backported as far as 2.0. The QPACK changes can be dropped before 2.6. In 2.0 there is also the equivalent code for legacy mode, which doesn't suffer from the list truncation, but it would better be fixed regardless. [CVE-2023-25725](https://github.com/advisories/GHSA-h2p2-w857-329f "CVE-2023-25725") was assigned to this issue.
  
  
  1 parent [07846cb](/haproxy/haproxy/commit/07846cbda87f5f7c8e2324a333422fc9bbf048e6) commit a8598a2
  
  Copy full SHA for a8598a2

3 files changed

+22Lines changed: 22 additions & 0 deletions

## File tree

Expand file treeCollapse file tree

Open diff view settings

Filter options

  * src

  * h1.c

  * hpack-dec.c

  * qpack-dec.c

Expand file treeCollapse file tree

Open diff view settings

Collapse file

### `‎src/h1.c‎`

Copy file name to clipboardExpand all lines: src/h1.c

+4Lines changed: 4 additions & 0 deletions

Original file line number| Diff line number| Diff line change  
---|---|---  
`@@ -834,6 +834,10 @@ int h1_headers_to_hdr_list(char *start, const char *stop,`  
`834`| `834`| `  
`  
`835`| `835`| ` if (likely(*ptr == ':')) {`  
`836`| `836`| ` col = ptr - start;`  
``| `837`| `+ if (col <= sol) {`  
``| `838`| `+ state = H1_MSG_HDR_NAME;`  
``| `839`| `+ goto http_msg_invalid;`  
``| `840`| `+ }`  
`837`| `841`| ` EAT_AND_JUMP_OR_RETURN(ptr, end, http_msg_hdr_l1_sp, http_msg_ood, state, H1_MSG_HDR_L1_SP);`  
`838`| `842`| ` }`  
`839`| `843`| `  
`  
``  
  
Collapse file

### `‎src/hpack-dec.c‎`

Copy file name to clipboardExpand all lines: src/hpack-dec.c

+9Lines changed: 9 additions & 0 deletions

Original file line number| Diff line number| Diff line change  
---|---|---  
`@@ -420,6 +420,15 @@ int hpack_decode_frame(struct hpack_dht *dht, const uint8_t *raw, uint32_t len,`  
`420`| `420`| ` /* <name> and <value> are correctly filled here */`  
`421`| `421`| ` }`  
`422`| `422`| `  
`  
``| `423`| `+ /* We must not accept empty header names (forbidden by the spec and used`  
``| `424`| `+ * as a list termination).`  
``| `425`| `+ */`  
``| `426`| `+ if (!name.len) {`  
``| `427`| `+ hpack_debug_printf("##ERR@%d##\n", __LINE__);`  
``| `428`| `+ ret = -HPACK_ERR_INVALID_ARGUMENT;`  
``| `429`| `+ goto leave;`  
``| `430`| `+ }`  
``| `431`| `+`  
`423`| `432`| ` /* here's what we have here :`  
`424`| `433`| ` * - name.len > 0`  
`425`| `434`| ` * - value is filled with either const data or data allocated from tmp`  
``  
  
Collapse file

### `‎src/qpack-dec.c‎`

Copy file name to clipboardExpand all lines: src/qpack-dec.c

+9Lines changed: 9 additions & 0 deletions

Original file line number| Diff line number| Diff line change  
---|---|---  
`@@ -531,6 +531,15 @@ int qpack_decode_fs(const unsigned char *raw, uint64_t len, struct buffer *tmp,`  
`531`| `531`| ` len -= value_len;`  
`532`| `532`| ` }`  
`533`| `533`| `  
`  
``| `534`| `+ /* We must not accept empty header names (forbidden by the spec and used`  
``| `535`| `+ * as a list termination).`  
``| `536`| `+ */`  
``| `537`| `+ if (!name.len) {`  
``| `538`| `+ qpack_debug_printf(stderr, "##ERR@%d\n", __LINE__);`  
``| `539`| `+ ret = -QPACK_DECOMPRESSION_FAILED;`  
``| `540`| `+ goto out;`  
``| `541`| `+ }`  
``| `542`| `+`  
`534`| `543`| ` list[hdr_idx].n = name;`  
`535`| `544`| ` list[hdr_idx].v = value;`  
`536`| `545`| ` ++hdr_idx;`  
``  
  
## 0 commit comments

Comments

0 (0)
