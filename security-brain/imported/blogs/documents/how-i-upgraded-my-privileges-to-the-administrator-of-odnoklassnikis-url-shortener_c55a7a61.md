---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-20_how-i-upgraded-my-privileges-to-the-administrator-of-odnoklassnikis-url-shortene.md
original_filename: 2019-08-20_how-i-upgraded-my-privileges-to-the-administrator-of-odnoklassnikis-url-shortene.md
title: How I upgraded my privileges to the administrator of Odnoklassniki’s url shortener
category: documents
detected_topics:
- sso
- access-control
- command-injection
- api-security
- supply-chain
tags:
- imported
- documents
- sso
- access-control
- command-injection
- api-security
- supply-chain
language: en
raw_sha256: c55a7a61b9065297819aa1724f19752a695729af16e185e913776d1687a542fb
text_sha256: 105baa41f168fc5490b5ef7fe21f1ecca5dbeb2b837b113a62b6367fa15efb33
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# How I upgraded my privileges to the administrator of Odnoklassniki’s url shortener

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-20_how-i-upgraded-my-privileges-to-the-administrator-of-odnoklassnikis-url-shortene.md
- Source Type: markdown
- Detected Topics: sso, access-control, command-injection, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `c55a7a61b9065297819aa1724f19752a695729af16e185e913776d1687a542fb`
- Text SHA256: `105baa41f168fc5490b5ef7fe21f1ecca5dbeb2b837b113a62b6367fa15efb33`


## Content

---
title: "How I upgraded my privileges to the administrator of Odnoklassniki’s url shortener"
url: "https://medium.com/@iframe_h1/how-i-upgraded-my-privileges-to-the-administrator-of-odnoklassnikis-url-shortener-2c58f996d02c"
authors: ["Sergey Kashatov (@iframe0x01)"]
programs: ["ok.ru"]
bugs: ["Privilege escalation"]
bounty: "500"
publication_date: "2019-08-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5072
scraped_via: "browseros"
---

# How I upgraded my privileges to the administrator of Odnoklassniki’s url shortener

How I upgraded my privileges to the administrator of Odnoklassniki’s url shortener
Sergey Kashatov
Follow
2 min read
·
Aug 20, 2019

41

Hi, today I will tell you how I hacked one service and successfully managed to get administrator rights.

(This issue has been reported to company’s bug bounty program at https://hackerone.com/ok and is now fixed)

There is a service for shortening links “https://okl.lt”
I searched for something there for a long time but my attempts were unsuccessful, since the average user has practically no functionality there

And suddenly it occurred to me to look at the scripts/styles associated with the site

I found an interesting js script: https://okl.lt/js/2236ccc.js

I saw the Jquery library there, and thought that there would be very little interesting or nothing at all… 😓

Nevertheless, I decided to look, and it was not in vain, I saw all the API methods, and the functions of this service 😻

OMG

It was there that I saw the functions of the administrator…

Press enter or click to view image in full size
Adm Func

I decided to make a request and try to perform one of the functions (I was sure that this would not work because everyone makes very cruel checks)

{"result":true,"people":null}

I did not show you the request itself, but it was successfully completed! and I saw this answer! 😂🤗

Get Sergey Kashatov’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I immediately ran to write my report to this program

Timeline:

changed the status to Triaged. (Apr 24th)

Fix (Apr 25th)

Bounty( Apr 26th) $500

The guys made a correction very quickly, the vulnerability was aggravated by the fact that absolutely any user could see
this and take advantage for their own purposes.

Report: https://hackerone.com/reports/547145
Twitter: https://twitter.com/iframe0x01

Happy hunting :)
