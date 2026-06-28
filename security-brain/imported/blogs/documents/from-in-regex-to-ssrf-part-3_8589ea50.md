---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-07_from-in-regex-to-ssrf-part-3.md
original_filename: 2020-07-07_from-in-regex-to-ssrf-part-3.md
title: From . in regex to SSRF — part 3
category: documents
detected_topics:
- ssrf
- command-injection
- api-security
- mobile-security
- supply-chain
tags:
- imported
- documents
- ssrf
- command-injection
- api-security
- mobile-security
- supply-chain
language: en
raw_sha256: 8589ea5069d76f3cbdc9851dbebe62ead4cd7b73665263b33ae82880006cf392
text_sha256: 90af38ea66607daeccd268d176fd68e60a8750973c6b26ab1698a5ba20a128ca
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# From . in regex to SSRF — part 3

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-07_from-in-regex-to-ssrf-part-3.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, api-security, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `8589ea5069d76f3cbdc9851dbebe62ead4cd7b73665263b33ae82880006cf392`
- Text SHA256: `90af38ea66607daeccd268d176fd68e60a8750973c6b26ab1698a5ba20a128ca`


## Content

---
title: "From . in regex to SSRF — part 3"
page_title: "From . in regex to SSRF - part 3 - xvnpw personal blog"
url: "https://xvnpw.github.io/posts/from-dot-in-regex-to-ssrf-part-3/"
final_url: "https://xvnpw.github.io/posts/from-dot-in-regex-to-ssrf-part-3/"
authors: ["Niemiec Marcin (@xvnpw)"]
bugs: ["SSRF", "CRLF injection"]
bounty: "400"
publication_date: "2020-07-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4430
---

# From . in regex to SSRF - part 3

Posted on Jul 7, 2020

This is last part of my stories about exploiting service with SSRF bug. Part 1 is available [here](https://xvnpw.github.io/posts/from-dot-in-regex-to-ssrf-part-1/), and part 2 [here](https://xvnpw.github.io/posts/from-dot-in-regex-to-ssrf-part-2/).

This part is focused on abusing Node.js and _node-fetch_ library. I will try to “talk” with Redis service using CRLF injection in http parser.

For convenience Redis service will be simulated by `nc -vvlp 6379`.

Test environment from my Kali 2020.1b:

  * Node.js version 10.19.0
  * node-fetch version 2.6.0

## CRLF Injection

Lets start with PayloadsAllTheThings. It contains couple of CRLF Injection payloads. I will loop over them and check result in second console:

![](https://user-images.githubusercontent.com/17719543/139583089-ecf56f8e-5c1a-465d-b0ff-01204ef313aa.png)

None success here. All payloads failed 🙁

Next step is to check payloads from two great articles by Orange Tsai: [first from Red Hat 2017](https://www.blackhat.com/docs/us-17/thursday/us-17-Tsai-A-New-Era-Of-SSRF-Exploiting-URL-Parser-In-Trending-Programming-Languages.pdf) and [second from his blog](https://blog.orange.tw/2017/07/how-i-chained-4-vulnerabilities-on.html). It’s giving few more options to test:
  
  
  －＊Set-Cookie:injection－＊ (Unicode U+FF0D U+FF0A)
  http://0\r\n SET foo 0 60 5\r\n :6379/
  https://0\r\nSET foo 0 60 5\r\n:6379/
  

Still no success here. I seams that this version of Node.js is not vulnerable for CRLF attacks.

Let’s try harder and dig dipper into node-fetch, maybe something interesting will be in code 😃

## Investigation of node-fetch code

What am I trying to achieve here? I have in mind two types of possible errors:

  1. Url parsing
  2. Handling url input as object not as _string_

Let’s see what I will find.

Debug of Node.js code is quite nice with Visual Studio Code:

![](https://user-images.githubusercontent.com/17719543/139583200-2686e457-092e-4385-8a01-f7716babf711.png)

Problem number one is not existing as node-fetch is using standard Node.js `Url.parse` for input. There are not doing much fancy stuff with it.

For second problem I needed to do more investigation.

First of all I will explain why I’m interested in processing _object_ instead of _string_. In many dynamic languages you can make valid request like this:

`http://localhost:3000/c?url[href]=localhost&url[method]=POST`

This leads to created object instead of string. Could be quite handy for some scenarios. Especially if developers didn’t predict it 😃 See below example of parsing such url in Node.js Express framework.

![](https://user-images.githubusercontent.com/17719543/139583272-0e1f3070-7ec9-44a3-8df7-ac9cf858d883.png)

In node-fetch I have found one possible attacking vector:

![](https://user-images.githubusercontent.com/17719543/139583293-12f60351-0548-41c5-a92b-45711eac279f.png)

It look like possible to use object instead of string for input parameter. This `input.method` could change method type in some specific conditions. After spending some time in debugger it turn out as **dead end**.

## Summary

I didn’t manage to escalate blind SSRF to anything more. I have spent couple of days trying different approaches. Nevertheless after submitting report I was awarded with **400$** and bug was marked as **medium**.

* * *

Thanks for reading! You can follow me on [Twitter](https://twitter.com/xvnpw).

  * [SSRF](/tags/ssrf)
  * [bugbounty](/tags/bugbounty)
