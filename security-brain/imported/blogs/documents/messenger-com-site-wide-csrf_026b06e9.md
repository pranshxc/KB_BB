---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-07-26_messengercom-site-wide-csrf.md
original_filename: 2016-07-26_messengercom-site-wide-csrf.md
title: Messenger.com Site-Wide CSRF
category: documents
detected_topics:
- csrf
- xss
- command-injection
- otp
- cloud-security
tags:
- imported
- documents
- csrf
- xss
- command-injection
- otp
- cloud-security
language: en
raw_sha256: 026b06e96bda201454e120ae32a53d456ba152d2d93f28d91b8c993e8f1a0027
text_sha256: 5495b8cd8e0467be5225b91f093958cefc9844b2760dd455386999bccc647fd7
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Messenger.com Site-Wide CSRF

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-07-26_messengercom-site-wide-csrf.md
- Source Type: markdown
- Detected Topics: csrf, xss, command-injection, otp, cloud-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `026b06e96bda201454e120ae32a53d456ba152d2d93f28d91b8c993e8f1a0027`
- Text SHA256: `5495b8cd8e0467be5225b91f093958cefc9844b2760dd455386999bccc647fd7`


## Content

---
title: "Messenger.com Site-Wide CSRF"
page_title: "Messenger.com Site-Wide CSRF – Jack"
url: "https://whitton.io/articles/messenger-site-wide-csrf/"
final_url: "https://whitton.io/articles/messenger-site-wide-csrf/"
authors: ["Jack Whitton (@fin1te)"]
programs: ["Meta / Facebook"]
bugs: ["CSRF"]
publication_date: "2016-07-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6274
---

# [Messenger.com Site-Wide CSRF](https://whitton.io/articles/messenger-site-wide-csrf/ "Messenger.com Site-Wide CSRF")

## July 26, 2015

__Reading time ~1 minute

_I originally wasn’t going to publish this, but[@phwd](https://twitter.com/phwd) wanted to hear about some of my recent bugs so this post is dedicated to him._

_This issue was also found by[@mazen160](https://twitter.com/mazen160), who [blogged about it](http://blog.mazinahmed.net/2015/06/facebook-messenger-multiple-csrf.html) back in June._

When [Messenger.com](https://www.messenger.com) launched back in April, I quickly had a look for any low-hanging fruit.

One of the first things to do is check end-points for [Cross-Site Request Forgery](https://en.wikipedia.org/wiki/Cross-site_request_forgery) issues. This is whereby an attacker can abuse the fact that cookies are implicity sent with a request (regardless of where the request is made from), and perform actions on another users behalf, such as sending a message or updating a status.

There are different ways of mitigating this (with varying results), but usually this is achieved by sending a non-guessable token with each request, and comparing it to a value stored server-side/decrypting it and verifying the contents.

The way I normally check for these is as follows:

  1. Perform the request without modifying the parameters, so we can see what the expected result is
  2. Remove the CSRF token completely (in this case, the `fb_dtsg` parameter)
  3. Modify one of the characters in the token (but keep the length the same)
  4. Remove the value of the token (but leave the parameter in place)
  5. Convert to a GET request

If any of the above steps produce the same result as #1 then we know that the end-point is likely to be vulnerable (there are _some_ instances where you might get a successful response, but in fact no data has been modified and therefore the token hasn’t been checked).

Normally, on Faceboook, the response is one of two, depending on if the request is an AJAX request or not (indicated by the `__a` parameter).

Either a redirect to `/common/invalid_request.php`:

[ ![](/images/messengercsrf/messenger-csrf-1.png) ](/images/messengercsrf/messenger-csrf-1.png)

Or an error message:

[ ![](/images/messengercsrf/messenger-csrf-2.png) ](/images/messengercsrf/messenger-csrf-2.png)

I submitted the following request to change the `sound_enabled` setting, without `fb_dtsg`:
  
  
  POST /settings/edit/ HTTP/1.1
  Host: www.messenger.com
  Content-Type: application/x-www-form-urlencoded
  
  settings[sound_enabled]=false&__a=1

Which surprisingly gave me the following response:
  
  
  HTTP/1.1 200 OK
  Content-Type: application/x-javascript; charset=utf-8
  Content-Length: 3559
  
  for (;;);{"__ar":1,"payload":[],"jsmods":{"instances":[["m_a_0",["MarketingLogger"],[null,{"is_mobile":false,"controller_name":"XMessengerDotComSettingsEditController"
  ...

I tried another end-point, this time to remove a user from a group thread.
  
  
  POST /chat/remove_participants/?uid=100...&tid=153... HTTP/1.1
  Host: www.messenger.com
  Content-Type: application/x-www-form-urlencoded
  
  __a=1

Which _also_ worked:
  
  
  HTTP/1.1 200 OK
  Content-Type: application/x-javascript; charset=utf-8
  Content-Length: 136
  
  for (;;);{"__ar":1,"payload":null,"domops":[["replace","^.fbProfileBrowserListItem",true,null]],"bootloadable":{},"ixData":{},"lid":"0"}

After trying one more I realised that the check was missing on **every** request.

#### Fix

Simple and quick fix - tokens are now properly checked on every request.

[websec](https://whitton.io/tags/#websec "Pages tagged websec")[bugbounty](https://whitton.io/tags/#bugbounty "Pages tagged bugbounty")[csrf](https://whitton.io/tags/#csrf "Pages tagged csrf")[facebook](https://whitton.io/tags/#facebook "Pages tagged facebook")[messenger](https://whitton.io/tags/#messenger "Pages tagged messenger") Updated on July 26, 2015 Jack

  * [__Like](https://www.facebook.com/sharer/sharer.php?u=https://whitton.io/articles/messenger-site-wide-csrf/ "Share on Facebook")
  * [__Tweet](https://twitter.com/intent/tweet?text=https://whitton.io/articles/messenger-site-wide-csrf/ "Share on Twitter")
  * [__+1](https://plus.google.com/share?url=https://whitton.io/articles/messenger-site-wide-csrf/ "Share on Google Plus")

[Read More](https://whitton.io/articles/bypassing-google-authentication-on-periscopes-admin-panel/)

### [From Bug Bounty Hunter, to Engineer, and Beyond](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/ "From Bug Bounty Hunter, to Engineer, and Beyond")

A couple weeks ago I had my last day on Facebook's Product Security team. Abittersweet moment, but one which marks a "new chapter" in my ...… [Continue reading](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/)

#### [Obtaining Login Tokens for an Outlook, Office or Azure Account](https://whitton.io/articles/obtaining-tokens-outlook-office-azure-account/ "Obtaining Login Tokens for an Outlook, Office or Azure Account")

Published on April 03, 2016

#### [Uber Bug Bounty: Turning Self-XSS into Good-XSS](https://whitton.io/articles/uber-turning-self-xss-into-good-xss/ "Uber Bug Bounty: Turning Self-XSS into Good-XSS")

Published on March 22, 2016
