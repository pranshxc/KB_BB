---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-03_my-story-with-xss.md
original_filename: 2020-09-03_my-story-with-xss.md
title: My Story With XSS
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 3ece42116b12f77e2e1411ad34265cf9934b5890ca9d57bacbefbe78e185eb7e
text_sha256: 0454d36bf53dd3970da48af75fe283509cd9d0b523c64b0f14b850b534181e2c
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# My Story With XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-03_my-story-with-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `3ece42116b12f77e2e1411ad34265cf9934b5890ca9d57bacbefbe78e185eb7e`
- Text SHA256: `0454d36bf53dd3970da48af75fe283509cd9d0b523c64b0f14b850b534181e2c`


## Content

---
title: "My Story With XSS"
url: "https://medium.com/@soufianehabti/my-story-with-xss-ed017bdc44c4"
authors: ["Soufiane Habti (@wld_basha)"]
bugs: ["XSS"]
publication_date: "2020-09-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4281
scraped_via: "browseros"
---

# My Story With XSS

My Story With XSS
Soufiane Habti
Follow
3 min read
·
Sep 3, 2020

236

As you know every bugbounty hunter has a story with xss and i have one too

Before starting this write up i just want to mention i started my bug bounty journey 2 months ago and they were full of adventures (btw i mean N/A and informatives and dupes ), anyways i learned bunch of stuff, one of my them is that one (it was a dupe too)

without further ado let’s talk about how i hunted this XSS

Press enter or click to view image in full size

its all started when i picked a VDP from hackerone list and i start my recon where i started with creating an account and i watched the whole flow thru burp cause i love understanding the application logic and how it handles every step.

Some Findings on the signup point :

the application was sending after an user finishes filling the signup form a request to /v3/users contains a json body that has bunch of informations about the user and there was one parameter that caught my eyes [afteractivationurl] that will lead you to the main page after you click that url sent to your email .

so i first followed the application process as a normal user (no injections no changes) .

Get Soufiane Habti’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then i noticed one thing about that process which was a redirection page after the activation and the juicy thing is our vulnerable page is rendering the path into html after url decoding it.

So i immediately went and created a new account and this time i change the path given by the client with my favorite simple url encoded payload

‘<img src=”” onerror=”javascript:alert(document.cookie)”>’

then when i went back to my email inbox i found the malicious link i sent

Press enter or click to view image in full size

i clicked it and i had the beautiful pop up contains all the user cookie cause there was no httponly on setcookie

Press enter or click to view image in full size

Sadly i got a Dupe for this one but it helped me to get other valide bugs and get bounty cause this one made me understand that every step made by a web application maybe vulnerable you just need to dig deeper to find it
