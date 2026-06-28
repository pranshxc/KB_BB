---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-26_a-classical-account-takeover-case-via-multiple-bypasses.md
original_filename: 2023-06-26_a-classical-account-takeover-case-via-multiple-bypasses.md
title: A Classical Account Takeover Case via Multiple Bypasses
category: documents
detected_topics:
- command-injection
- password-reset
- api-security
tags:
- imported
- documents
- command-injection
- password-reset
- api-security
language: en
raw_sha256: 5c647455ed70a85f4312a49302fe22140317cb51eef98ad07706f425f9ba62b3
text_sha256: aee850569d8106896b2b5cfd73f8afcb17944641491d8282ab9e489ac31b8e08
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# A Classical Account Takeover Case via Multiple Bypasses

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-26_a-classical-account-takeover-case-via-multiple-bypasses.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, api-security
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `5c647455ed70a85f4312a49302fe22140317cb51eef98ad07706f425f9ba62b3`
- Text SHA256: `aee850569d8106896b2b5cfd73f8afcb17944641491d8282ab9e489ac31b8e08`


## Content

---
title: "A Classical Account Takeover Case via Multiple Bypasses"
page_title: "A Classical Account Takeover Case via Multiple Bypasses - Kamil Onur Özkaleli as ko2sec"
url: "http://www.kamilonurozkaleli.com/posts/a-classical-account-takeover-case-via-multiple-bypasses/"
final_url: "http://www.kamilonurozkaleli.com/posts/a-classical-account-takeover-case-via-multiple-bypasses/"
authors: ["Kamil Onur Özkaleli (@ko2sec)"]
bugs: ["Account takeover", "Password reset", "Host header injection", "URL validation bypass"]
publication_date: "2023-06-26"
added_date: "2023-06-27"
source: "pentester.land/writeups.json"
original_index: 1007
---

# [Kamil Onur Özkaleli as ko2sec](http://www.kamilonurozkaleli.com/)

## This blog is mostly about security writeups and research articles.

[__](https://github.com/ko2sec "Github")[__](https://twitter.com/ko2sec "Twitter")[__](https://linkedin.com/kamilonurozkaleli "LinkedIn")

  * [Home](/)
  * [All posts](/posts)
  * [Tags](/tags)

# A Classical Account Takeover Case via Multiple Bypasses

Posted at — Jun 26, 2023

### **Introduction**

Recently I found a password reset/recovery flaw in a program at Synack. The vulnerability is the classical password reset link manipulation via Host Header Injection but rather than the vulnerability itself, the way how I managed to exploit it might be interesting. As a summary, this write-up contains a _CDN Bypass_ \+ _Regex Bypass_ \+ _Host Header Injection_ resulting an account takeover vulnerability.

### **CDN Bypass**

![What is a CDN?](/images/ato-1.png)

While testing the target, I found out that the web application is behind [Akamai CDN](https://www.akamai.com/glossary/what-is-a-cdn) which is pretty reasonable for a modern web application. CDNs not only provide distributed servers that speed up the delivery of web content but also brings some security features as well. One of those security feature is preventing Host Header Injection vulnerability which is not so remarkable if you cannot chain it with another attack vector.

![CDN preventing Host Header Injection](/images/ato-2.png)

CDNs are pretty hardened and not easy to bypass their security features but it might be easier to find origin IP of the web application and access it directly. This is a common misconfiguration not to restrict direct access to public applications which are behind CDN/WAF/LB like components when there are thousands of assets in a company. As an approach, I collected subdomains of the target company via amass and sent HTTP requests with `Host: target.com` to specific `login.html` page to check if any of the subdomains responds with same page.

![Sending HTTP Requests](/images/ato-3.png)

I got 3 matches with 200 OK response code. 2 of them were false positives but other one was responding with same login page when a HTTP request is sent with proper Host header. So we bypassed the CDN and found the origin IP of the web application.

### **Regex Bypass**

On the other hand, while testing I have found out that web application was served by IBM HTTP Server. I searched a little and came up with a documentation by IBM as _[Protecting from host header injection](https://www.ibm.com/docs/en/odm/8.9.2?topic=configuring-protecting-from-host-header-injection)_.

![IBM HTTP Server](/images/ato-4.png) ![IBM Protecting From Host Header Injection Documentation](/images/ato-5.png)

As a consequence of given example host regex list, it cannot prevent host header injection and it still matches with host headers like _[www.target.com.test](https://www.target.com.test)_. So if you are following the given documentation you are still vulnerable.

![IBM Protecting From Host Header Injection Documentation](/images/ato-10.png) ![IBM Protecting From Host Header Injection Documentation](/images/ato-9.png)

_[www.target.co](https://www.target.co)_ NOT VALID

![NOT VALID](/images/ato-6.png)

_[www.target.com.test](https://www.target.com.test)_ VALID

![VALID](/images/ato-7.png)

Improper validation is result of a missing _$_ sign at the end of the regex validation which should only return a match when the text or string is ended with given value.

### **Account Takover**

Here is the boring part actually. This is a classical password recovery flaw, which is relying on user controlled Host input and generates password reset link respective to it. For detailed information please see [PortSwigger](https://portswigger.net/web-security/host-header/exploiting/password-reset-poisoning).

![Account Takeover](/images/ato-8.png)

### **Takeaways**

  1. Restricting direct access to assets behind CDN/WAF/LB like components is a must, especially if you are relying on their security features. Use the IP whitelisting approach and only allow access from component IPs.
  2. Never trust user controlled data, if needed validate and sanitize properly.
  3. Do not underestimate security issues. Even if there are minor oneslike Host Header Injection, it can be chained with other attack vectors and misconfigurations.

  * [bug bounty](/tags/bug-bounty)
  * [synack](/tags/synack)

kamilonurozkaleli.com © all rights reserved. | [Ezhil theme](https://github.com/vividvilla/ezhil) | Built with [Hugo](https://gohugo.io)
