---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-05_a-tale-of-verbose-error-message-and-a-jwt-token.md
original_filename: 2020-05-05_a-tale-of-verbose-error-message-and-a-jwt-token.md
title: A tale of verbose error message and a JWT token
category: documents
detected_topics:
- information-disclosure
- sso
- jwt
- idor
- access-control
- ssrf
tags:
- imported
- documents
- information-disclosure
- sso
- jwt
- idor
- access-control
- ssrf
language: en
raw_sha256: 21373607754c9b3a069b2435d369fe532e7a719821073837df9432c7b38be5ff
text_sha256: e07e73b4b7c46c5477ab39a3dcbd05db598d0e9b4ff8328a16259ba70ac40938
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# A tale of verbose error message and a JWT token

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-05_a-tale-of-verbose-error-message-and-a-jwt-token.md
- Source Type: markdown
- Detected Topics: information-disclosure, sso, jwt, idor, access-control, ssrf
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `21373607754c9b3a069b2435d369fe532e7a719821073837df9432c7b38be5ff`
- Text SHA256: `e07e73b4b7c46c5477ab39a3dcbd05db598d0e9b4ff8328a16259ba70ac40938`


## Content

---
title: "A tale of verbose error message and a JWT token"
page_title: "A tale of verbose error message and a JWT token | marek.geleta"
url: "https://geleta.eu/2020/a-tale-of-verbose-error-message-and-jwt-token/"
final_url: "https://geleta.eu/2020/a-tale-of-verbose-error-message-and-jwt-token/"
authors: ["Marek Geleta (@marek_geleta)"]
bugs: ["Information disclosure", "Broken authorization"]
publication_date: "2020-05-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4605
---

# A tale of verbose error message and a JWT token

Written by [Marek Geleta](https://geleta.eu) with ♥  on 5 May 2020 in __ [ Bug Bounty ](https://geleta.eu/categories/bug-bounty/) __3 min

Unlike probably all web developers I love HTTP 500 errors - they often indicate that something went terribly wrong and there might be a vulnerability. In most cases, you are left with something like this

![Cute but doesn't say much about the error :\(](/images/ring.svg)Cute but doesn't say much about the error :(

But in some, the errors are more verbose and sometimes disclose a little more information than they should about what’s actually happening behind the scenes and what went wrong. And this was the case with this bug.

## Intro

I had burp running with [Autorize](https://github.com/Quitten/Autorize) extension - it automatically sends every request that went through proxy again with cookies of another user and without any cookies whatsoever.

The app I was testing can be compared to something like GitHub - You can create public/private projects, collaborate, etc.

## A bit of information gathering

There was this feature to duplicate a project. It was a bit weird because it required a JWT token although the rest of the app used cookie-based auth. I tried to mess with it a bit but didn’t find anything useful. Next, I played with a bunch of other endpoints and found another two that were using JWT auth - “download project as zip” and “write files to project”. (Didn’t find any vulnerabilities in them, just noted that they were using JWT)

## Some bugs are hidden where you least expect them

Then I looked into Autorize, scrolled a bit, inspected responses, and then noticed that the unauthenticated request to “duplicate project” endpoint returned error 500 and **much** longer response than any other request. I don’t have a screenshot of that but I think it was something about 8Kb

![](/images/ring.svg)

So I did what any other person would do. Clicked on the response aaand there was a LOT of stuff

![](/images/ring.svg)

There were JWT tokens everywhere! After a while of base64-decoding and comparing stuff, I found out that this was basically a God token. If someone requested `/api/{project_id}/duplicate` without any authorization it would then create a new user and issue a token with write permission for the supplied project.

This was the base64decoded token:
  
  
  {
  "userId":"9e46fac3-e0c6-4532-af6c-3fe78444cef2",
  "projectId":"5e822a7b-9563-4ae4-9820-c39bad8b715d",
  "accessType":"edit",
  "iat":158196154
  }
  

Then the app would for some reason error out and throw this token at me, I don’t really know what went wrong because the token was working!

### Remember those two JWT endpoints I was talking about earlier?

So now with this token I was able to read or write every project and needed just its uuid to do it - that limits the impact a bit but I still had r/w access to practically every project on the app

![](/images/ring.svg)

## Lessons learned

  * Note weird things, patterns of behavior of the app - it can be useful later
  * Learn to use burp extensions
  * Using UUIDs instead of numeric IDs can be a pretty good defense in depth against IDORS (Not perfect though)

Author: Marek Geleta 

Words: 463

Share: [ __](//twitter.com/share?url=https%3a%2f%2fgeleta.eu%2f2020%2fa-tale-of-verbose-error-message-and-jwt-token%2f&text=A%20tale%20of%20verbose%20error%20message%20and%20a%20JWT%20token&via=marek_geleta "Share on Twitter") [ __](//reddit.com/submit?url=https%3a%2f%2fgeleta.eu%2f2020%2fa-tale-of-verbose-error-message-and-jwt-token%2f&title=A%20tale%20of%20verbose%20error%20message%20and%20a%20JWT%20token "Share on Reddit")

Released under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

__Tag:[ #bugbounty](https://geleta.eu/tags/bugbounty/) [ #ssrf](https://geleta.eu/tags/ssrf/) [ #writeup](https://geleta.eu/tags/writeup/) [ #security](https://geleta.eu/tags/security/) [ #bug](https://geleta.eu/tags/bug/) [ #bounty](https://geleta.eu/tags/bounty/) [Back](javascript:window.history.back\(\);) · [Home](https://geleta.eu)

[__My First SSRF Using DNS Rebinding](https://geleta.eu/2019/my-first-ssrf-using-dns-rebinfing/ "My First SSRF Using DNS Rebinding")

[comments powered by Disqus](https://disqus.com/)
