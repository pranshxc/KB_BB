---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1031321'
original_report_id: '1031321'
title: Github Account hijack through broken link in developer.twitter.com
weakness: Phishing
team_handle: x
created_at: '2020-11-11T06:59:11.822Z'
disclosed_at: '2021-02-04T06:25:16.411Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 210
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- phishing
---

# Github Account hijack through broken link in developer.twitter.com

## Metadata

- HackerOne Report ID: 1031321
- Weakness: Phishing
- Program: x
- Disclosed At: 2021-02-04T06:25:16.411Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Description
A link in    https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries   was broken and anyone could create that account which leads to account impersonate

Steps To Reproduce
1) Visit https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries
2) Scroll down to Javascript/Node.js and click on by @HunterLarco (v2)
3)  Create github username HunterLarcol
4) When someone visits and scroll down to  javascript/Node.js and click on @HunterLarco (v2). They are redirected to my account

similar report
https://hackerone.com/reports/265696



To solve this issue 
put this link https://github.com/HunterLarco

Please let me know if you have any questions. I am happy to help

## Impact

Impact
The users are coming from developer.twitter.com So, the attacker can put malicious content on the github  and many users will be the victim for example https://github.com/HunterLarcol/twitter-v2. Moreover it leads to the loss in the reputation of the company

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
