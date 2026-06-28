---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-24_sop-bypass-via-browser-cache.md
original_filename: 2019-12-24_sop-bypass-via-browser-cache.md
title: SOP Bypass via browser-cache
category: documents
detected_topics:
- cors
- access-control
- command-injection
- password-reset
- otp
- csrf
tags:
- imported
- documents
- cors
- access-control
- command-injection
- password-reset
- otp
- csrf
language: en
raw_sha256: e4fbcd2f88e86131140ea6c5246779e9b740a5c9118ae68c9e19766451477e3d
text_sha256: 4b4ff31037c4601ccf79df41c9794008d5e5ac41832110df77d4f0ea89336757
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# SOP Bypass via browser-cache

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-24_sop-bypass-via-browser-cache.md
- Source Type: markdown
- Detected Topics: cors, access-control, command-injection, password-reset, otp, csrf
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `e4fbcd2f88e86131140ea6c5246779e9b740a5c9118ae68c9e19766451477e3d`
- Text SHA256: `4b4ff31037c4601ccf79df41c9794008d5e5ac41832110df77d4f0ea89336757`


## Content

---
title: "SOP Bypass via browser-cache"
page_title: "SOP Bypass via browser-cache – enumerated"
url: "https://enumerated.wordpress.com/2019/12/24/sop-bypass-via-browser-cache"
final_url: "https://enumerated.wordpress.com/2019/12/24/sop-bypass-via-browser-cache/"
authors: ["Aaron Costello (@ConspiracyProof)"]
programs: ["Keybase"]
bugs: ["SOP bypass"]
bounty: "1,500"
publication_date: "2019-12-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4865
---

# SOP Bypass via browser-cache

[December 24, 2019December 24, 2019](https://enumerated.wordpress.com/2019/12/24/sop-bypass-via-browser-cache/) ~ [Dantalion](https://enumerated.wordpress.com/author/dantalion4040/)

## Introduction

Whilst hunting for security issues on Keybase.io’s public HackerOne program, I noticed that several API endpoints had CORS enabled. For those who are not familiar with CORS, it allows for a site to relax the [SOP ](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)so that other domains may interact with (most often) a web API. In this article I’ll discuss how I was able to manipulate the browser cache into returning private user data through a misconfiguration of Keybase’s CORS policy.

## Overview

Keybase provides an API that allows users to perform a lookup of other Keybase users when encrypting a message, similar to a contact book lookup. It provided publicly accessible information on other users that is required when encrypting a message such as their public PGP key. So far so safe right?

The CORS policy implemented on this endpoint looked like the following:
  
  
  Access-Control-Allow-Origin: *
  Access-Control-Allow-Methods: GET
  Access-Control-Allow-Headers: Content-Type, Authorization, Content-Length, X-Requested-With
  Access-Control-Allow-Credentials: false

There is some important aspects to understand here in order to be able to make sense of the issue: 

  1. The wildcard (*) value for Access-Control-Allow-Origin allows for any external domain to interact with the API and perform queries cross-origin
  2. Using the wildcard value implements ‘Access-Control-Allow-Credentials: false’ meaning authenticated requests cross-origin are disallowed (For security reasons). The Authorization header exposed here for an authenticated request is not overly relevant for the exploit, as it is not required to query the public API.

## The issue

No CSRF token is required in order for these cross-origin requests to work, naturally, since the API is considered public. Users utilizing Keybase.io are authenticated and their session is stored in cookies, while more sensitive API endpoints require an Authorization token in a header. 

What I noticed was that if I performed a lookup on myself while authenticated (had a keybase.io session set in my cookies), or even entered a letter contained in my name, my own account would be returned in the search results along with private information. This included:

  * Email Address
  * How many invitation codes I had used / left to use
  * Billing plan information
  * Timestamps relating to last logged in, and time / date of email verification
  * Private PGP key (Encrypted with TripleSec)

I had no private PGP key stored on Keybase, and I later learned that private PGP key hosting on Keybase.io is in fact a legacy feature from 2015-2016 that is no longer implemented. 

Once the cookies were removed from my request to the endpoint, my private information mentioned above was no longer returned. However one thing I did notice in the response returned by the endpoint was an ‘Etag’ header. This header is an indicator of browser caching, instructing a browser to fetch from its cache if the content in the response had not changed.

## Payload and Result

I recalled a trick I learned from [@Bitk_](https://twitter.com/bitk_?lang=en), in which it’s possible to use javascript’s fetch API to force a request cross-origin to retrieve from the browser cache directly. Keybase did not implement any cache-control headers in the response, so I created a payload locally (The null origin won’t matter) like so:
  
  
  <html>
  <script>  
  var url = "https://keybase.io/_/api/1.0/user/lookup.json?username={YOUR_USERNAME}";  
  fetch(url, {  
  method: 'GET',  
  cache: 'force-cache'
  });
  </script>
  </html>

I knew that if this request succeeded, it would likely return the cached response given by Keybase after I had made an **authenticated** request, which would likely contain my private information.

And voila! 

![](https://enumerated.wordpress.com/wp-content/uploads/2019/12/sensitive2.png?w=1024)

In order to confirm that the payload was successful, we can see below that fetch had pulled the response directly from the browser cache.

![](https://enumerated.wordpress.com/wp-content/uploads/2019/12/sensitive1.png?w=558)

## Timeline

19/12/2019 – Issue reported to Keybase

19/12/2019 (2 hours later) – Issue remediated with implementation of the ‘Cache-Control: no-store’ header in the response as advised.

24/12/2019 – Public disclosure of [HackerOne report](https://hackerone.com/reports/761726)

### Share this:

  * [ Share on X (Opens in new window) X ](https://enumerated.wordpress.com/2019/12/24/sop-bypass-via-browser-cache/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://enumerated.wordpress.com/2019/12/24/sop-bypass-via-browser-cache/?share=facebook)
  * 

Like Loading...

### _Related_

[CORs](https://enumerated.wordpress.com/tag/cors/)[HackerOne](https://enumerated.wordpress.com/tag/hackerone/)[SOP](https://enumerated.wordpress.com/tag/sop/)

![Unknown's avatar](https://2.gravatar.com/avatar/b4f8d77b183e297e33889c4bcfb858506ed79424b22c0512d25ca9d2d523fc76?s=60&d=identicon&r=G)

##  Published by Dantalion

[ View all posts by Dantalion ](https://enumerated.wordpress.com/author/dantalion4040/)
