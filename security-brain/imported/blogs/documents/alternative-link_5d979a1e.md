---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-09-30_alternative-link.md
original_filename: 2019-09-30_alternative-link.md
title: Alternative link
category: documents
detected_topics:
- xss
- command-injection
- csrf
tags:
- imported
- documents
- xss
- command-injection
- csrf
language: en
raw_sha256: 5d979a1e61d9c82f5fa441bfa01be34b0e6720e301e0a9f59346b771e4026fed
text_sha256: 85940df21027b5e1d0b95e36734901ef382af15b6ec3758a2765befbe6784fad
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Alternative link

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-09-30_alternative-link.md
- Source Type: markdown
- Detected Topics: xss, command-injection, csrf
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `5d979a1e61d9c82f5fa441bfa01be34b0e6720e301e0a9f59346b771e4026fed`
- Text SHA256: `85940df21027b5e1d0b95e36734901ef382af15b6ec3758a2765befbe6784fad`


## Content

---
title: "Alternative link"
page_title: "XSS on Cookie Pop-up - Bug Bounty - 0x00sec - The Home of the Hacker"
url: "https://0x00sec.org/t/xss-on-cookie-pop-up/19580"
final_url: "https://archive.0x00sec.org/t/xss-on-cookie-pop-up/19580"
authors: ["vict0ni (@vict0ni)"]
bugs: ["Reflected XSS"]
publication_date: "2019-09-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5004
---

#  [XSS on Cookie Pop-up](19580.html)

[ Bug Bounty ](../../c/bug-bounty/108.html)

[vict0ni](../../u/vict0ni.html) March 2, 2020, 9:33pm  1

> Never trust pop-ups

While doing some bug hunting (actually, in this case it was just a responsible disclosure) on a website, I entered a XSS payload as a subdirectory in the URL, in order to see if and how it was reflected on the source code. It’s one of the first things I do when I manual test a site for XSS. For this I always use a payload with common characters used in XSS payloads that are filtered under the fear of inserting js code. After entering the

`https://website.com/"></>{}()vict0ni`

I got a custom 404 response page. Looking at the source code, the URL was reflected in 3 places. In the two of them the payload was sanitized, but on the third one everything were getting reflected as they were. The source code for the third reflection looked something like this:
  
  
  <input type="hidden" name="DismissCookieNotice" value="true" />
  <input type="hidden" name="redirected" value="https://www.website.com/"></>{}()vict0ni" />
  <input type="hidden" name="csrf" value=[something] />
  

So by entering the payload

`https://website.com/"/><svg onload=alert(document.cookie)>`

an XSS was triggered.

Everything was really simple. I browsed the website a little bit just to see how it was structured and then I went back to retest the XSS, just to be sure. Only this time… it didn’t work.

I tried to think of what could have changed between now and the time I triggered the XSS. I was changing parameters, payloads, user agents, basically everything. Still nothing.  
Then, after some tries, I thought of re-entering the URL on a private session. That’s where the XSS got triggered again!

![wut](../../uploads/default/original/2X/b/bab7eae36842a2d016e878744dcfa30619b12a08.html)

This happened because on the private session I didn’t click the “Accept Cookies” option on the pop-up that now every website is forced to provide. But I did it while browsing the website **after** finding the XSS. To be honest, I could have probably noticed that earlier in the **DismissCookieNotice** name in the source code.

_To recall:_
  
  
  ...
  <input type="hidden" name="DismissCookieNotice" value="true" />
  ...
  

The vulnerability was inside the code for the pop-up (after accepting the cookies, the page refreshed and the pop-up source code was missing from the new page). So the XSS could be reproduced only by ignoring the Cookie pop-up (not dismissing it, just by ignoring it).  
The logic behind this pop-up was that after accepting the cookies, the website would redirect the user to the URL he already was. That’s why the URL was reflected in the “redirected” hidden input. But they forgot to filter the user input.

Next time you test for a reflected XSS, make sure to test it **before** you accept the cookies. You never know!

18 Likes

[aits](../../u/aits.html) (AITS)  September 14, 2020, 8:31pm  2

Ow… That’s a great idea for xss .

2 Likes

[vict0ni](../../u/vict0ni.html) September 15, 2020, 9:17am  3

It’s based on the way the application is displaying the pop-up and how it handles the agreement. After this I always check for XSS without dismissing the pop-up
