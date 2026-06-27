---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1442017'
original_report_id: '1442017'
title: Self XSS in Create New Workspace Screen
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mattermost
created_at: '2022-01-05T20:10:49.968Z'
disclosed_at: '2022-02-20T09:08:08.589Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 40
asset_identifier: h1-*your-own-instance*.cloud.mattermost.com
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Self XSS in Create New Workspace Screen

## Metadata

- HackerOne Report ID: 1442017
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mattermost
- Disclosed At: 2022-02-20T09:08:08.589Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi team,
I have found an vulnerability on your website .
step to reproduce :

1.firstly i want to say sorry for this .please read carefully
when im testing on your website .i was redirected to  : https://customers.mattermost.com/cloud/connect-workspace
2.then navigate to create new workspace 
3.on workspace name input this payload : "/><img src=x onerror=alert(document.cookie)>
4.xss will trigger 

I know this domain is in out of scope ,but attacker can steal user cookies . I dont want any rewards for this i just want to aware you guys for this vulnerability .Hope you can understand .
Thanks for reading my report

## Impact

attacker can steal user cookies

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
