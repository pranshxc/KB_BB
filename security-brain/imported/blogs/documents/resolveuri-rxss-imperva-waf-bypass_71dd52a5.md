---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-10_resolveuri-rxss-imperva-waf-bypass.md
original_filename: 2022-05-10_resolveuri-rxss-imperva-waf-bypass.md
title: ResolveURI RXSS Imperva Waf Bypass
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: 71dd52a51c1923763dbb931fe60658ff02d756d6ec4fe6b17bd16cb828a0bd64
text_sha256: 8183da9d493c7d2df70d7c2071794bb960b20470f4f91300eea1c4c4a36c52da
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# ResolveURI RXSS Imperva Waf Bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-10_resolveuri-rxss-imperva-waf-bypass.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `71dd52a51c1923763dbb931fe60658ff02d756d6ec4fe6b17bd16cb828a0bd64`
- Text SHA256: `8183da9d493c7d2df70d7c2071794bb960b20470f4f91300eea1c4c4a36c52da`


## Content

---
title: "ResolveURI RXSS Imperva Waf Bypass"
url: "https://systemweakness.com/resolveuri-rxss-imperva-waf-bypass-c834ca573bd4"
authors: ["Ahsan Shahid (@hunter0x8)"]
bugs: ["XSS"]
publication_date: "2022-05-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2650
scraped_via: "browseros"
---

# ResolveURI RXSS Imperva Waf Bypass

ResolveURI RXSS Imperva Waf Bypass
Ahsan Shahid
Follow
2 min read
·
May 10, 2022

105

1

Hi, Asslam-o-Alaikum

My Name is Ahsan. This is my first writeup ignore mistakes, English is not my first language. I’m not going into detail with what ResolveURI XSS is. If you want to know about ResolveURI XSS visit this blog https://blog.isec.pl/all-is-xss-that-comes-to-the-net/

I got a message from a friend that he was not able to execute URI-based XSS due to Imperva waf. The value got reflected in link href tag.

<link href=”/AdminNet/Reflected-Value/App_Themes/Default/filename.css” rel=”stylesheet” type=”text/css” />
====================================================================
(A("onerror="alert`1`"))

Without waf this payload will work and you were able to execute Cross-Site Scripting. But In this case, the waf is blocking “alert”, “confirm”, ”prompt” keywords.

This is ResolveURI XSS I cannot use + and am not able to use concatenations and global variables to bypass the waf.

Get Ahsan Shahid’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After Trying I was able to Bypass the waf with “print” keyword. I use this payload for bypassing Waf.

(Z("onerror="a=print,a`1`"))
https://domain.com/AdminNET/(Z("onerror="a=print,a`1`"))/filename.aspx

The print keyword with brackets”print(1)” and backticks print`1` were getting blocked so I used the above payload.

<link href="/AdminNet/(Z("onerror="a=print,a`1`"))/App_Themes/Default/filename.css" rel="stylesheet" type="text/css" />

I Obtained XSS waf bypassed. But the program I was working on does not accept XSS with alert 1 or print you need to access DOM to prove the XSS.

I tried various things but not able to access DOM due to waf. The next thing i tried is using console.log

(Z("onerror="console.log"))

The waf blocked the console.log. The next thing I tried is

(Z("onerror="a=console,a.log`1`"))
https://domain.com/AdminNET/(Z("onerror="a=console,a.log`1`"))/filename.aspx

Again I was able to prove XSS but not able to access DOM. When I tried putting (Z(“onerror=”a=console,a.log()”)) When I put a() the page redirects to another page without my value reflecting there. But this payload (Z(“onerror=”a=console.log,a`1`”)) works fine.

I need to prove DOM Access to accept the vulnerability here. After Some tries I was able to access DOM via console.log with this final payload

(Z("onerror="a=console,a.log`${cookie}`"))
https://domain.com/AdminNET/(Z("onerror="a=console,a.log`${cookie}`"))/filename.aspx

I was able to access DOM via `${cookie}` or `${domain}`. I Send the payload to the friend and he reported the bug. Later We got rewarded for the bug. We split the bounty 50/50. I spend a whole day to bypass this. Because there were limitations you can not use + and If I use console.log() like this it will redirect me to another page where my value is not reflected. But I came up with an interesting Bypass.
