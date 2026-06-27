---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1443567'
original_report_id: '1443567'
title: html injection via invite members can be leads account takeover
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mattermost
created_at: '2022-01-07T17:24:01.456Z'
disclosed_at: '2022-03-22T10:15:21.944Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 33
asset_identifier: h1-*your-own-instance*.cloud.mattermost.com
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# html injection via invite members can be leads account takeover

## Metadata

- HackerOne Report ID: 1443567
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mattermost
- Disclosed At: 2022-03-22T10:15:21.944Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi team,
I have found an vulnerability on your website .
step to reproduce :
1.navigate to : yourworkspace.cloud.mattermost.com
2.create new channel F1571445
3.there you will find a functionality invite members F1571448
4.click on invite members 
5 input your email address 
6.scroll down & click on invite as guest F1571456
7. on Add to channels input your channel name 
8.click on set a custom message , input this html payloads : <a href=evil.com>click</a>
<input type=x>
9. invite 
10.open inbox of  email that you have invited
as you can see  html injected & there's an input field & click button 

follow my video poc for better understanding & if you need any info let me know .
thanks for reading my report .God bless you

## Impact

As HTML injection worked in email an attacker can trick victim to click on such hyperlinks to redirect him to any malicious site and also can host a XSS page. All this will surely cause some damage to victim. This could lead to users being tricked into giving logins away to malicious attackers.

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
