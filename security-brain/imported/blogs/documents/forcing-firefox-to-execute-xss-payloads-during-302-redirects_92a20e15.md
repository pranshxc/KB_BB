---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-30_forcing-firefox-to-execute-xss-payloads-during-302-redirects.md
original_filename: 2020-09-30_forcing-firefox-to-execute-xss-payloads-during-302-redirects.md
title: Forcing Firefox to Execute XSS Payloads during 302 Redirects
category: documents
detected_topics:
- xss
- command-injection
- mfa
- api-security
tags:
- imported
- documents
- xss
- command-injection
- mfa
- api-security
language: en
raw_sha256: 92a20e151bd3c20fd7abc3ce22ed94f60195250cbb8bb506399432a03cb941a0
text_sha256: 5fa76a2252c6e5520eeff0337b9845c465f9f4d8f0118115f60b7b392c4600dc
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Forcing Firefox to Execute XSS Payloads during 302 Redirects

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-30_forcing-firefox-to-execute-xss-payloads-during-302-redirects.md
- Source Type: markdown
- Detected Topics: xss, command-injection, mfa, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `92a20e151bd3c20fd7abc3ce22ed94f60195250cbb8bb506399432a03cb941a0`
- Text SHA256: `5fa76a2252c6e5520eeff0337b9845c465f9f4d8f0118115f60b7b392c4600dc`


## Content

---
title: "Forcing Firefox to Execute XSS Payloads during 302 Redirects"
page_title: "Forcing Firefox to Execute XSS Payloads during 302 Redirects | Gremwell"
url: "https://www.gremwell.com/firefox-xss-302"
final_url: "https://www.gremwell.com/firefox-xss-302"
authors: ["Quentin Kaiser (@QKaiser)"]
bugs: ["XSS"]
publication_date: "2020-09-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4227
---

Submitted by quentin on Wed, 09/30/2020 - 14:49

### Initial Discovery

During a recent engagement I identified an open redirect where a GET parameter would be reflected as-is in the HTTP response Location header without any kind of sanitization. Something similar to this:

![open_redirect](https://www.gremwell.com/sites/default/files/Screenshot%20from%202020-09-30%2014-53-31.png)

Trying multiple kinds of injections, I discovered that newlines and carriage returns characters could be inserted, leading to header injection:

![header_injection](https://www.gremwell.com/sites/default/files/Screenshot%20from%202020-09-30%2015-35-26.png)

Even more interesting, we can inject arbitrary content in the HTTP response body by inserting two newline characters, leading to reflected cross-site scripting:

![body_inject](https://www.gremwell.com/sites/default/files/Screenshot%20from%202020-09-30%2015-36-54.png)

However, modern browsers (Google Chrome, Internet Explorer, Firefox) do not interpret the HTTP response body if the HTTP response status code is a 302, so our cross-site scripting payload is useless. Time to find a bypass !

### Prior Work

By searching for prior bypasses, I stumbled upon this [blog post](https://www.fortinet.com/blog/threat-research/multiple-plone-cross-site-scripting-vulnerabilities) where Fortinet describes how they bypassed the execution block by setting the Location header to a URI starting with 'mailto://'. [Bugcrowd forums](https://forum.bugcrowd.com/t/how-to-trigger-js-execution-on-302-page/3449/5) also provides some insight into bypasses that may have worked in the past. And this excellent [HackerOne report](https://hackerone.com/reports/260744) on XSS affecting Twitter, where they used a Location header starting with '//x:1/' definitely sent me in the right direction.

### Let's Fuzz

Given that none of the already documented bypasses worked, I decided to write a dumb fuzzer that would generate a list of URLs and open them with xdg-open. To do so, I downloaded the [IANA URI schemes list](https://www.iana.org/assignments/uri-schemes/uri-schemes.txt) and generated a list of URLs following this format: <http://acme.corp/?redir=>[URI_SCHEME]://gremwell.com%0A%0A[XSS_PAYLOAD]. Google Chrome and Firefox were tested in this way, Internet Explorer was also tested but with a PowerShell script rather than simply calling xdg-open.

I then spent quite some time closing browser tabs, hoping to be greeted with an alert box :)

### A Valid Candidate

Two candidates out of the full IANA URI scheme list worked, and only on Firefox:

  * ws:// (WebSocket)
  * wss:// (Secure WebSocket).

It simply looks like this:

![valid_bypass](https://www.gremwell.com/sites/default/files/Screenshot%20from%202020-09-30%2015-38-33.png)

Opening the link in the latest version of Firefox (version 81 at the time of writing) and we see we are executing JavaScript under the right domain, without being redirected:

![xss_trigger](https://www.gremwell.com/sites/default/files/Screenshot%20from%202020-09-30%2014-48-27.png)

### Proof-of-Concept

If you want to test this at home, you can download the [302_server](https://www.gremwell.com/sites/default/files/302_server.py) script. It will launch a Python3 HTTP server on port 8000, mimicking the behavior I just described.

### Update - October 1st 2020

[Sergey Bobrov](https://twitter.com/@Black2Fan) just [pointed out](https://twitter.com/Black2Fan/status/1311630481084026881) that using an empty Location header will work to force Google Chrome to execute the payload. Nice find !

### Update - October 2nd 2020

[Maxim Rupp](https://twitter.com/@mmrupp) just [pointed out](https://twitter.com/mmrupp/status/1311786461419585537) that using an resource:// URI in the Location header will work to force Firefox 81 to execute the payload. Nice find !
