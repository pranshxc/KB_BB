---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-15_encoding-differentials-why-charset-matters.md
original_filename: 2024-07-15_encoding-differentials-why-charset-matters.md
title: 'Encoding Differentials: Why Charset Matters'
category: documents
detected_topics:
- xss
- sqli
- command-injection
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- xss
- sqli
- command-injection
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: 135de2e5a662af4b8748445bfb40b7249fd65a5befe2e3548ec40f624db4b40c
text_sha256: 78f7c922ae898f4f166e548bee2106a9c6209804c80f93d1d0160e1a9d44465b
ingested_at: '2026-06-28T07:32:35Z'
sensitivity: unknown
redactions_applied: false
---

# Encoding Differentials: Why Charset Matters

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-15_encoding-differentials-why-charset-matters.md
- Source Type: markdown
- Detected Topics: xss, sqli, command-injection, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:35Z
- Redactions Applied: False
- Raw SHA256: `135de2e5a662af4b8748445bfb40b7249fd65a5befe2e3548ec40f624db4b40c`
- Text SHA256: `78f7c922ae898f4f166e548bee2106a9c6209804c80f93d1d0160e1a9d44465b`


## Content

---
title: "Encoding Differentials: Why Charset Matters"
page_title: "Encoding Differentials: Why Charset Matters | Sonar"
url: "https://www.sonarsource.com/blog/encoding-differentials-why-charset-matters/"
final_url: "https://www.sonarsource.com/blog/encoding-differentials-why-charset-matters/"
authors: ["Stefan Schiller (@scryh_)"]
bugs: ["XSS"]
publication_date: "2024-07-15"
added_date: "2024-07-15"
source: "pentester.land/writeups.json"
original_index: 165
---

## TL;DR overview

  * Encoding differentials occur when different layers of a web application interpret the same byte sequence under different character sets, creating security gaps that bypass input validation.
  * Charset mismatches between the browser, server, and database can allow attackers to smuggle malicious payloads—such as XSS or SQL injection—past filters that rely on consistent encoding.
  * Developers should explicitly declare character sets at every layer of the stack and avoid relying solely on content-type headers, which can be overridden or ignored by certain browsers.
  * Sonar's static analysis can detect charset-related misconfigurations in source code before they become exploitable vulnerabilities in production.

Do you notice something in the following HTTP response?

Copy to clipboard
  
  
  HTTP/1.1 200 OK
  Server: Some Server
  Content-Type: text/html
  Content-Length: 1337
  
  <!DOCTYPE html>
  <html>
  <head><title>Some Page</title></head>
  <body>
  ...

Based on this small portion of the HTTP response, you can assume that this web application is **likely prone to an XSS vulnerability**.

How is this possible? Did you notice something?

If you have doubts about the `Content-Type` header, you are right. There is only a minor imperfection here: the header is **missing** a `charset` attribute. This does not sound like a big deal, however, this blog post will explain how attackers can exploit this to inject arbitrary JavaScript code into a website by **consciously changing the character set** that the browser assumes.

This blog post's content was also presented at the [TROOPERS24 conference](https://troopers.de/troopers24/talks/r3hxdq/). A recording of the talk can be found here: [From ASCII to UTF-16: Leveraging Encodings to Break Software](https://www.youtube.com/watch?v=z-ug2dwcSz8).

## Character Encodings

A common `Content-Type` header in an HTTP response looks like this:

Copy to clipboard
  
  
  HTTP/1.1 200 OK
  Server: Some Server
  Content-Type: text/html; {% mark yellow %}charset=utf-8{% mark %}
  ...

The `charset` attribute tells the browser that UTF-8 was used to encode the HTTP response body. A character encoding like UTF-8 defines a **mapping between characters and bytes**. When a web server serves an HTML document, it maps the characters of the document to the corresponding bytes and transmits these in the HTTP response body. This process turns characters into bytes (_encode_):

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/03789676-77cd-427e-90d8-d4451da66a27/encode.png)

When the browser receives these bytes in the HTTP response body, it can translate them back to the characters of the HTML document. This process turns bytes into characters (_decode_):

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/6fe42fba-f2a0-4d0a-a461-aaf690ddcae3/decode.png)

UTF-8 is only one of **many character encodings** that a modern browser must support according to the [HTML spec](https://html.spec.whatwg.org/#character-encodings). There are plenty of others like `UTF-16`, `ISO-8859-xx`, `windows-125x`, `GBK`, `Big5`, etc. It is essential that the browser knows which of those encodings the server used or it **cannot properly decode** the bytes in the HTTP response body.

But what if there is no `charset` attribute in the `Content-Type` header or it is invalid?

In that case, the browser looks for a `<meta>` tag in the HTML document itself. This tag can also have a `charset` attribute that indicates the character encoding (e.g., `<meta charset="UTF-8">`). This is already an act of balance for the browser: In order to read the HTML document, it needs to decode the HTTP response body. Thus, it needs to assume _some_ encoding, decode the HTTP body, look for a `<meta>` tag, and possibly re-decode the body with the indicated character encoding.

Another, less common way to indicate the character encoding is the [Byte-Order Mark](https://en.wikipedia.org/wiki/Byte_order_mark). This is a specific Unicode character (`U+FEFF`) that can be placed in front of a string to indicate the byte endianness and character encoding. It is mainly used in files, but since these might be served via a web server, modern browsers support it. A Byte-Order Mark at the beginning of an HTML document even takes precedence over a `charset` attribute in the `Content-Type` header and the `<meta>` tag.

In summary, there are three common ways that a browser uses to **determine the character encoding** of an HTML document, ordered by priority:

  1. Byte-Order Mark at the beginning of the HTML document
  2. `charset` attribute in the `Content-Type` header
  3. `<meta>` tag in the HTML document

## Missing Charset Information

The Byte-Order Mark is generally very uncommon and the `charset` attribute is not always present in a `Content-Type` header or might be invalid. Also - especially for partial HTML responses - there is usually no `<meta>` tag that indicates a character encoding. In these cases, the browser does not have any information about what character set to use:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/a1479d94-8cd4-4a1d-ae56-ff9617ae6725/missing_charset.png)

Have you ever seen this error message? Probably not, because **it does not exist**.

Similar to faulty HTML syntax, browsers try to recover from missing character set information when parsing the content served from a web server and **make the best of it**. This non-strict behavior contributes to a good user experience, but it may also **open doors for exploitation techniques** like [mXSS](https://www.sonarsource.com/blog/mxss-the-vulnerability-hiding-in-your-code/).

For missing character information, browsers try to make an educated guess based on the content, which is called [auto-detection](https://html.spec.whatwg.org/#encoding-sniffing-algorithm:~:text=The%20user%20agent%20may%20attempt%20to%20autodetect%20the%20character%20encoding%20from%20applying%20frequency%20analysis%20or%20other%20algorithms%20to%20the%20data%20stream.). This is similar to [MIME-type sniffing](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types#mime_sniffing) but operates on a character encoding level. Chromium’s rendering engine Blink, for example, uses the [Compact Encoding Detection (CED) library](https://github.com/google/compact_enc_det) to automatically detect the character encoding. From an attacker’s point of view, the **auto-detection feature is very powerful** as we will see.

At this point, we are familiar with the different mechanisms a browser may use to determine the character encoding of an HTML document. But how could attackers exploit this?

## Encoding Differentials

The purpose of character encoding is to translate characters into a computer-processable byte sequence. These bytes can be transmitted over a network and decoded back to characters by the receiver. This way, the **exact same characters** that the sender intended to transmit are restored:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/8e95f56e-cce8-4e6b-b6b6-ec6fd5f9648b/encode-decode-ok.png)

This only works fine, when the sender and receiver agree upon the character encoding they use. If there is a **mismatch** between the character encoding used for encoding and decoding, the receiver may _see_ different characters:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/1b7f0442-bc33-4a34-94ab-494792bd0bd9/encode-decode-not-ok.png)

Such a mismatch between the character encoding used for encoding and decoding is what we refer to as _Encoding Differential_ here.

For a web application, this becomes vital when user-controlled data is sanitized to prevent Cross-Site Scripting (XSS) vulnerabilities. If the character encoding that the browser assumes is different from what the web server intended, this could theoretically break the sanitization and lead to XSS vulnerabilities.

This itself is no big news and even Google was prone to an issue like this [back in 2005](https://seclists.org/fulldisclosure/2005/Dec/att-1107/google_xss_211205.txt#:~:text=Google%27s%20404%20NOT%20FOUND%20mechanism). Google’s 404 page did not provide charset information, which could be exploited by inserting a [UTF-7](https://en.wikipedia.org/wiki/UTF-7) XSS payload. In UTF-7, HTML special characters like angle brackets are encoded differently from ASCII which can be leveraged to bypass sanitization:

Copy to clipboard
  
  
  +ADw-script+AD4-alert(1)+ADw-+AC8-script+AD4-

This greatly demonstrated the dangers of this encoding, which was deprecated in the following years to prevent security issues like this. Nowadays, the HTML spec even explicitly [forbids the usage of UTF-7](https://html.spec.whatwg.org/#refsUTF7:~:text=For%20example%2C%20the%20restriction%20on%20using%20UTF%2D7%20exists%20purely%20to%20avoid%20authors%20falling%20prey%20to%20a%20known%20cross%2Dsite%2Dscripting%20attack%20using%20UTF%2D7.) to prevent XSS vulnerabilities.

Although there are still a lot of other supported character encodings, most of these are not really useful from an attacker’s point of view. All **HTML special characters** like angle brackets and quotes are **ASCII only** and since most character encodings are ASCII-compatible, there is **no difference** for these characters. Even for UTF-16, which is not ASCII-compatible due to its fixed amount of two bytes per character, it is usually not possible to smuggle ASCII characters, because their corresponding byte representation is the same, just with a trailing (little-endian) or leading (big-endian) zero byte.

However, there is a particularly interesting encoding: **ISO-2022-JP**.

## ISO-2022-JP

ISO-2022-JP is a Japanese character encoding defined in [RFC 1468](https://www.rfc-editor.org/rfc/rfc1468.html). It is one of the official character encodings that user agents must support, as defined by the [HTML standard](https://html.spec.whatwg.org/#character-encodings). Particularly interesting about this encoding is that it supports certain **escape sequences** to **switch between different character sets**.

For example, if a byte sequence contains the bytes `0x1b`, `0x28`, `0x42`, these bytes are not decoded to a character but instead indicate that all following bytes should be decoded using ASCII. In total, there are four different escape sequences that can be used to switch between the character sets ASCII, JIS X 0201 1976, JIS X 0208 1978 and JIS X 0208 1983:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/7b209ce6-241c-4340-a6e6-7c097c6b9c5d/iso-2022-jp.png)

This feature of ISO-2022-JP not only provides great flexibility but can also break fundamental assumptions. And there is another catch: at the time of writing, **Chrome (Blink) and Firefox (Gecko) auto-detect this encoding.** A single occurrence of one of these escape sequences is usually enough to convince the auto-detection algorithm that the HTTP response body is encoded with ISO-2022-JP.

The following sections explain two different exploitation techniques that attackers may use when they can make the browser assume an ISO-2022-JP charset. Depending on the capabilities of the attacker, this can for example be achieved by directly controlling the `charset` attribute in the `Content-Type` header or by inserting a `<meta>` tag via an HTML injection vulnerability. If a web server provides an invalid `charset` attribute or none at all, there are usually no other prerequisites since attackers can easily switch the charset to ISO-2022-JP via auto-detection.

### Technique 1: Negating Backslash Escaping

The scenario for this technique is that **user-controlled data** is placed **in a JavaScript string** :

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/7b29a332-aebf-4789-b64a-9171ea0f6f38/iso-2022-jp-teq1-01.png)

Let’s imagine a website that accepts two query parameters called `search` and `lang`. The first parameter is reflected in a plaintext context and the second parameter (`lang`) is inserted into a JavaScript string:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/539746f8-646a-4ed5-8a85-b2e73a724284/iso-2022-jp-teq1-02.png)

HTML special characters in the `search` parameter are HTML-encoded, and the `lang` parameter is properly sanitized by escaping double quotes (`"`) and backslashes (`\`). Thus, it is not possible to break out of the string context and inject JavaScript code:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/d0604dfd-fa98-46a7-b0cc-e6675d40744e/iso-2022-jp-teq1-03.png)

The default mode for ISO-2022-JP is ASCII. This means that all bytes of the received HTTP response body are decoded with ASCII and the resulting HTML document looks like what we would expect:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/f439bfb5-f73d-4ef5-b217-62d0f9f027ea/iso-2022-jp-teq1-04.png)

Now, let’s assume an attacker inserts the escape sequence to switch to the JIS X 0201 1976 charset in the `search` parameter (`0x1b`, `0x28`, `0x4a`):

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/f2440d8e-b63f-4c61-9664-9cb6632f0049/iso-2022-jp-teq1-05.png)

The browser now decodes all bytes following this escape sequence with JIS X 0201 1976:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/0652ec9c-2f13-4196-9258-13450dd0dae6/iso-2022-jp-teq1-06.png)

As we can see, this still results in the same characters as before, since JIS X 0201 1976 is _mainly_ ASCII-compatible. However, if we closely inspect [its code table](https://en.wikipedia.org/wiki/JIS_X_0201#Codepage_layout), we can notice that there are two exceptions (highlighted in yellow):

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/05df20d0-2049-4f37-8414-7f956f34d5df/jisx-0201-codetable.png)

The byte `0x5c` is mapped to the yen character (`¥`) and the byte `0x7e` to the overline character (`‾`). This is different from ASCII, where `0x5c` is mapped to the backslash character (`\`) and `0x7e` to the tilde character (`~`).

This means that when the web server tries to escape a double quote in the `lang` parameter with a backslash, the browser does not _see_ a backslash anymore, but instead a yen sign:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/5afd4276-5177-4545-841d-7cdd3a9dc31c/iso-2022-jp-teq1-07.png)

Accordingly, the inserted double quote actually designates the end of the string and allows an attacker to inject arbitrary JavaScript code:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/bba1d004-96c5-4d59-a7a2-abf407e53184/iso-2022-jp-teq1-08.png)

Although this technique is quite powerful, it is limited to bypassing sanitization in a JavaScript context since a backslash character does not have special meaning in HTML. The next section explains a more advanced technique that can be applied in a pure HTML context.

### Technique 2: Breaking HTML Context

The scenario for this second technique is that an attacker can control values in **two different HTML contexts**. A common use case would be a website that supports markdown. For example, let’s consider the following markdown text:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/fb805311-69de-4451-a242-741b2fda8228/iso-2022-jp-teq2-01.png)

The resulting HTML code looks like this:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/9466dd63-fe60-421e-9c5e-b069116cf47b/iso-2022-jp-teq2-02.png)

Essential for this technique is that an attacker can control values in two different HTML contexts. In this case, these are:

  * Attribute context (image description/source)
  * Plaintext context (text surrounding images)

By default, ISO-2022-JP is in ASCII mode and the browser _sees_ the HTML document as expected:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/9d4c1bda-1e1e-4f10-be3d-1ac4ef7adaa7/iso-2022-jp-teq2-03.png)

Now, let’s assume an attacker inserts the escape sequence to switch the charset to JIS X 0208 1978 in the first image description:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/d64afc3a-7339-466a-ab2d-49e9c9f3fae1/iso-2022-jp-teq2-04.png)

This makes the browser decode all bytes following with JIS X 0208 1978. This charset uses a fixed amount of 2 bytes per character and is not ASCII-compatible. This effectively breaks the HTML document:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/c6f350f6-d3c5-4e1c-abbb-b6f5bbfd01eb/iso-2022-jp-teq2-05.png)

However, a second escape sequence can be inserted in the plaintext context between both images to switch the charset back to ASCII:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/63b0ca03-7816-472f-b096-c28a53a68703/iso-2022-jp-teq2-06.png)

This way, all the following bytes are decoded using ASCII again:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/3836339d-258a-48af-8d95-e4ee95e880ec/iso-2022-jp-teq2-07.png)

When inspecting the HTML syntax, though, we can notice that something changed. The beginning of the second `img` tag is now part of the `alt` attribute value:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/12f5839b-8242-4437-a569-b470641b5bb0/iso-2022-jp-teq2-08.png)

The reason for this is that the 4 bytes in between both escape sequences were decoded using JIS X 0208 1978. This also **consumed the closing double-quote** of the attribute value:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/2c3d6366-c6bd-45dc-a782-e1a7c1df3ca1/iso-2022-jp-teq2-09.png)

At this point, the `src` attribute value of the second image is not an attribute value anymore. Thus, an attacker can replace this value with a JavaScript error handler:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/93dfbed8-51c1-42c6-a24e-1490e151b683/iso-2022-jp-teq2-10.png)

This, again, allows an attacker to inject arbitrary JavaScript code.

## Summary

In this blog post, we highlighted the importance of providing charset information when serving HTML documents. The absence of charset information can lead to severe XSS vulnerabilities when attackers are able to change the character set that the browser assumes.

We detailed how a browser determines the character set used to decode an HTTP response body and explained two different techniques that attackers may use to inject arbitrary JavaScript code into a website leveraging the ISO-2022-JP character encoding.

Although we consider a missing character set the actual vulnerability, a browser’s auto-detection greatly increases its impact. Because of this, we hope that browsers will disable the auto-detection mechanism according to our suggestion - at least for the ISO-2022-JP character encoding.

## Related Blog Posts

  * [mXSS: The Vulnerability Hiding in Your Code](https://www.sonarsource.com/blog/mxss-the-vulnerability-hiding-in-your-code/)
  * [Joomla: PHP Bug Introduces Multiple XSS Vulnerabilities](https://www.sonarsource.com/blog/joomla-multiple-xss-vulnerabilities/)
  * [Code Interoperability: The Hazards of Technological Variety](https://www.sonarsource.com/blog/avocado-nightmare-1/)
