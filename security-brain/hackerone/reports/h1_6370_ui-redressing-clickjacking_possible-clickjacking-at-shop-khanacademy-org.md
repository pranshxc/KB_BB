---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6370'
original_report_id: '6370'
title: Possible clickjacking at shop.khanacademy.org
weakness: UI Redressing (Clickjacking)
team_handle: khanacademy
created_at: '2014-04-08T00:35:32.249Z'
disclosed_at: '2014-05-08T03:33:17.909Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- ui-redressing-clickjacking
---

# Possible clickjacking at shop.khanacademy.org

## Metadata

- HackerOne Report ID: 6370
- Weakness: UI Redressing (Clickjacking)
- Program: khanacademy
- Disclosed At: 2014-05-08T03:33:17.909Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello there,

the website at shop.khanacademy.org isn't protected against clickjacking properly.

###PoC

```
curl -L -I http://shop.khanacademy.org/ 
HTTP/1.1 200 OK
Server: nginx
Date: Tue, 08 Apr 2014 00:33:39 GMT
Content-Type: text/html; charset=utf-8
Vary: Accept-Encoding
Status: 200 OK
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-UA-Compatible: chrome=1
X-ShopId: 1494466
X-ShardId: 0
X-Stats-Unique-Token: 2dd016682529fa6dc0ac02f03b41cb145bdeb1906793867d2f763e05dad4a464
X-Stats-Visit-Token: d52a2198c1a197fb3535f0ea5db92ee9381f41ad8a910d9997859a4a7d21a6bb
ETag: cacheable:8709c7da7c24e09f7f45bab2c9d17d6a
X-Alternate-Cache-Key: cacheable:214f21e7ce7fcc794113ab6ec2eac291
X-Cache: miss
Set-Cookie: _shopify_y=2dd016682529fa6dc0ac02f03b41cb145bdeb1906793867d2f763e05dad4a464; path=/; expires=Sat, 08 Apr 2034 00:33:39 -0000
Set-Cookie: _shopify_s=d52a2198c1a197fb3535f0ea5db92ee9381f41ad8a910d9997859a4a7d21a6bb; path=/; expires=Tue, 08 Apr 2014 01:03:39 -0000
Set-Cookie: request_method=HEAD; path=/
Set-Cookie: _session_id=289a218d076bea034b85e5e807e00aa9; path=/; HttpOnly
X-Request-Id: 6a3f8d62-4d9d-4303-af04-12e201856770
P3P: CP="NOI DSP COR NID ADMa OPTa OUR NOR"

```


You should add the ```X-Frame-Origin: sameorigin``` header to the server http responses. Otherwise you're vulnerable to clickjacking attacks.


Best regards,
Sebastian

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
