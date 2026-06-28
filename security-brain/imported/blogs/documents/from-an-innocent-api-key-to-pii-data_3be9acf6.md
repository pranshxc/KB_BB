---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-30_from-an-innocent-api-key-to-pii-data.md
original_filename: 2023-03-30_from-an-innocent-api-key-to-pii-data.md
title: From an Innocent api-key to PII data
category: documents
detected_topics:
- otp
- api-security
- sso
- command-injection
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- otp
- api-security
- sso
- command-injection
- automation-abuse
- information-disclosure
language: en
raw_sha256: 3be9acf6a676fa0825d0b8790957229e8f1c65980a9f42ed86a3178fb0011da2
text_sha256: f9d150287e56c7b8ddd66289e3846f8d38c2e3dc5170915370951f1d64dea9e2
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: true
---

# From an Innocent api-key to PII data

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-30_from-an-innocent-api-key-to-pii-data.md
- Source Type: markdown
- Detected Topics: otp, api-security, sso, command-injection, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: True
- Raw SHA256: `3be9acf6a676fa0825d0b8790957229e8f1c65980a9f42ed86a3178fb0011da2`
- Text SHA256: `f9d150287e56c7b8ddd66289e3846f8d38c2e3dc5170915370951f1d64dea9e2`


## Content

---
title: "From an Innocent api-key to PII data"
page_title: "From an Innocent api-key to PII data | crypt0g30rgy.github.io"
url: "https://crypt0g30rgy.github.io/post/Journey2pII"
final_url: "https://crypt0g30rgy.github.io/post/Journey2pII"
authors: ["g30rgy th3 d4rk (@Crypt0g30rgy)"]
bugs: ["Information disclosure", "Hardcoded API keys"]
bounty: "200"
publication_date: "2023-03-30"
added_date: "2023-04-06"
source: "pentester.land/writeups.json"
original_index: 1317
---

# [crypt0g30rgy.github.io](https://crypt0g30rgy.github.io/)

# From an Innocent api-key to PII data

## How we got there

It was on a thursday of february 2023, i had just gotten of driving and i was feeling tired, at the same time i was feeling `meh` since i had not done any good hacking that week, just doing random stuffs. so i took out my laptop sat on the coach and hopped on [intigriti](https://app.intigriti.com/researcher) and started looking around on the `recently update` category as i sometimes do. I found this program that had updated the scope, lets call it jij0 [you know the drill my returning readers](/post/why) and i decided to tap into it lightly.

i enumerated subdomains, got several hits, i decided since they weren’t many subdomains i should just visit them one by one and check if maybe i could find anything. i visted one `https://customers.jij0.me/` that seemed prety normal, login and signup and a web shop but nothing really interesting to poke around at. I did my usual poking around with the `view-source:` so i could check out the js files for any hardcorded creds, tokens or api-keys. i found some config data inside a script tag;
  
  
  <script> REDACTED... apiurl":"https://customers.jij0.me/v2","env":"prod","YOTPO-MERCHANT-ID":"XXXXX","YOTPO-API-KEY":"API_KEY_HERE","YOTPO-GUID":"GUID_HERE"  ...REDACTED </script>
  

at first i didn’t think much of these keys as they seemed not interesting at all, but i decided to check online for any exploitation on api keys from yotpo but my search returned nothing.

I was about to give up when i remembered that most companies have `dev documentations`. so i googled `yotpo developer documentation`, after a few readings here and there i found this documentation page [Loyalty Docs](https://loyaltyapi.yotpo.com/reference). Turns out the api-keys i found earlier were for the loyalty api, and the juicy part was that the same api keys were the `auth keys`. Bingo. after some more digging i found that i could query customer data associated with the api keys [Get Customers Docs](https://loyaltyapi.yotpo.com/reference/fetch-all-recently-updated-customers), super bingo.

> TIP of the day :: Just because it hasn’t been exploited and documented publicly, doesn’t mean it isn’t vulnerable… Everything is vulnerable unless proven otherwise.

So after reading the docs i crafted the following burp request to the api with the exposed api keys, and boom ‘PII’.

I stopped testing here.
  
  
  GET /api/v2/customers/recent?per_page=100 HTTP/2
  Host: loyalty.yotpo.com
  User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0
  Accept: application/json
  X-Guid: GUID_HERE
  X-Api-Key=***REDACTED***
  

## Reproduction Steps

  1. Visit <https://customers.jij0.me/>
  2. Perform a view-source, either by rightclicking or ctrl + u (cmd + u [mac users])
  3. Scroll down to the bottom to find

  
  
  <script> REDACTED... apiurl":"https://customers.jij0.me/v2","env":"prod","YOTPO-MERCHANT-ID":"XXXXX","YOTPO-API-KEY":"API_KEY_HERE","YOTPO-GUID":"GUID_HERE"  ...REDACTED </script>
  

  1. VIsit <https://loyalty.yotpo.com/api/v2/customers/recent?per_page=100> and intercept with burp
  2. Send request from 4 to repeater and send it to observe the 401 error Alter the request to be;

  
  
  GET /api/v2/customers/recent?per_page=100 HTTP/2
  Host: loyalty.yotpo.com
  User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0
  Accept: application/json
  X-Guid: GUID_HERE
  X-Api-Key=***REDACTED***
  

  1. send request

## Quick Curl Repro Command
  
  
  curl -i -s -k -X $'GET' \
  -H $'Host: loyalty.yotpo.com' -H $'Accept: application/json' -H $'X-Guid: GUID_HERE' -H $'X-Api-Key=***REDACTED*** \
  $'https://loyalty.yotpo.com/api/v2/customers/recent?per_page=100'
  

So i wrote a report and sent it to the program at intigriti. The report was triaged as a critical.

After waiting for a few days i recieved a €200 bonus.

![basic](/images/poc/yotpo.png)

## Contacts

### @[github](https://github.com/crypt0g30rgy) @[twitter](https://twitter.com/crypt0g30rgy) @[LinkedIn](https://www.linkedin.com/in/george-maina-waithaka-95a465214/) @[Intigriti](https://app.intigriti.com/profile/g30rgyth3d4rk) @[hackerone_old](https://hackerone.com/crypt0p3n3tr4t0r?type=user)
