---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-18_challenge-writeup-content-type-shenanigans.md
original_filename: 2023-09-18_challenge-writeup-content-type-shenanigans.md
title: challenge writeup content-type shenanigans
category: blogs
detected_topics:
- sso
- xss
- command-injection
- automation-abuse
- clickjacking
tags:
- imported
- blogs
- sso
- xss
- command-injection
- automation-abuse
- clickjacking
language: en
raw_sha256: 9dd013c908419c635aca1f6ecddbf7f55cc0a7252614eef0fd4364e7a58bae20
text_sha256: 6ddd61fbf925c51337715e2b5c4e9041c98131d649babc6d3d36a15da2170b83
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# challenge writeup content-type shenanigans

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-18_challenge-writeup-content-type-shenanigans.md
- Source Type: markdown
- Detected Topics: sso, xss, command-injection, automation-abuse, clickjacking
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `9dd013c908419c635aca1f6ecddbf7f55cc0a7252614eef0fd4364e7a58bae20`
- Text SHA256: `6ddd61fbf925c51337715e2b5c4e9041c98131d649babc6d3d36a15da2170b83`


## Content

---
title: "challenge writeup content-type shenanigans"
page_title: "challenge writeup content-type shenanigans · GitHub"
url: "https://gist.github.com/avlidienbrunn/8db7f692404cdd3c325aa20d09437e13"
final_url: "https://gist.github.com/avlidienbrunn/8db7f692404cdd3c325aa20d09437e13"
authors: ["Mathias Karlsson (@avlidienbrunn)"]
programs: ["k-"]
bugs: ["XSS"]
publication_date: "2023-09-18"
added_date: "2023-10-03"
source: "pentester.land/writeups.json"
original_index: 767
---

## Description

This was a challenge to demonstrate how the content-type header can be used to fool the browser into treating the HTTP response body in unexpected ways.

## Source

As the harder solution works for both, heres source:
  
  
  <?php
  /*
  FROM php:7.0-apache
  
  RUN a2dismod status
  
  COPY ./files/index.php /var/www/html
  COPY ./files/harder.php /var/www/html
  EXPOSE 80
  
  */
  $message = isset($_GET['message']) ? $_GET['message'] : 'hello, world';
  $type = isset($_GET['type']) ? $_GET['type'] : die(highlight_file(__FILE__));
  header("Content-Type: text/$type");
  header("X-Frame-Options: DENY");
  
  if($type == "plain"){
  die("the message is: $message");
  }
  
  ?>
  <html>
  <h1>The message is:</h1>
  <hr/>
  <pre>
  <input type="text" value="<?php echo preg_replace('/([^\s\w!-~]|")/','',$message);?>">
  </pre>
  <br>
  solved by:
  <li> nobody yet!</li>
  </html>

## Solution

**The first part** : it was made to demonstrate the fact that modern browsers still support multiple-byte (or other) encodings that dont treat standard ASCII characters as their ASCII counterpart.

For example, in a `UTF-16` world, the byte `\x3c` is not equivalent to ASCII `<`, but `\x00\x3c` is. No surprise there, but this means that if an attacker controls even just the end of the `Content-Type` (or meta http-equiv, in some cases, exercise for the reader), they can have the browser treat the document in one way, while the server treats it in another.

[http://avlidienbrunn.se/easier.php?type=html;charset=UTF-16LE&message=%00%00%3C%00i%00m%00g%00/%00s%00r%00c%00/%00o%00n%00e%00r%00r%00o%00r%00=%00a%00l%00e%00r%00t%00(%00d%00o%00m%00a%00i%00n%00)%00%3E%00%00](http://avlidienbrunn.se/easier.php?type=html;charset=UTF-16LE&message=%00%00%3C%00i%00m%00g%00/%00s%00r%00c%00/%00o%00n%00e%00r%00r%00o%00r%00=%00a%00l%00e%00r%00t%00\(%00d%00o%00m%00a%00i%00n%00\)%00%3E%00%00)

**The second part** : Multiple HTTP response headers with the same name should be treated as concatenated with the `,`/`\x2c` character. Browsers support the sequence `, `/`\x2c\x20` too, but that's just for convenience, or whitespaces are stripped, or something, I think.

This means that if we add `x,image/gif` to our parameter, the header sent by the server will be:
  
  
  Content-Type: text/x,image/gif
  

As `text/x` is not a recognized MIME type, the user agent will use `image/gif` which is recognized and supported.

So, we can control "the entire content-type header". So what? Well, there are some older (see O'Reilly's HTML The Definitive Guide vol2 from 1997, [chapter 14.3](https://docstore.mik.ua/orelly/web/html/ch14_03.html)) MIME types that can make the browser treat the document in other ways too!

The `multipart/mixed` MIME type acts like a standard multipart message where the server can supply multiple parts with different Content-Types (and other headers), and the user agent should render whichever part it has support for:
  
  
  HTTP/1.1 200 OK
  Content-type: multipart/mixed;boundary="8ormorebytes"
  
  
  ignored_first_part_before_boundary
  
  --8ormorebytes
  Content-Type: text/html
  
  <img src=x onerror=alert(domain)>
  
  --8ormorebytes
  
  ignored_last_part
  
  

As you can imagine, this allows us to make the browser ignore parts of the document, as it scans for the multipart boundary, specified in the `Content-Type` header. That means we don't need any `"` character to solve the challenge (firefox):

[http://avlidienbrunn.se/harder.php?type=asdasd,multipart/x-mixed-replace;%20boundary=12345678&message=%0D%0A%0D%0A--12345678%0D%0AContent-Type:%20text/html%0D%0A%0D%0A%3Cimg%20src=x%20onerror=alert(domain)%3E%0D%0A%0D%0A--12345678%0D%0A](http://avlidienbrunn.se/harder.php?type=asdasd,multipart/x-mixed-replace;%20boundary=12345678&message=%0D%0A%0D%0A--12345678%0D%0AContent-Type:%20text/html%0D%0A%0D%0A%3Cimg%20src=x%20onerror=alert\(domain\)%3E%0D%0A%0D%0A--12345678%0D%0A)

## Final words

There are other ways to confuse the user agent to start treating the "start of body" later in the message, via information in the HTTP Response first line or headers, such as `Content-Encoding`, `HTTP/1.1 100 Continue` and `Content-Range`. Try it out!

Also, [fun stuff happens](https://random-server-stuff.glitch.me/multipart-mixed-replace) if the server doesn't close the connection but instead keeps sending parts :)

"HTTP/1.1 had support for HTTP Push before it was cool"
