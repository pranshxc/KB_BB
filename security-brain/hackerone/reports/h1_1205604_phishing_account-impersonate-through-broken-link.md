---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1205604'
original_report_id: '1205604'
title: account impersonate through broken link
weakness: Phishing
team_handle: qiwi
created_at: '2021-05-22T04:01:13.957Z'
disclosed_at: '2021-06-04T13:17:36.064Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 39
asset_identifier: '*.qiwi.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- phishing
---

# account impersonate through broken link

## Metadata

- HackerOne Report ID: 1205604
- Weakness: Phishing
- Program: qiwi
- Disclosed At: 2021-06-04T13:17:36.064Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

hi  team,
hope you are good,

A link in qiwi.com was broken and anyone could create that account which leads to account impersonate

poc:- 
{F1310817}
Steps To Reproduce
1) Visit https://qiwi.com/sm
2) the link will redirect you to http://unbouncepages.com/savemyphone/ (which is throwing a error "The requested URL was not found on this server.")
3)  now visit https://unbounce.com/ and create a page with a name of savemyphone
4) When someone visits https://qiwi.com/sm They are redirected to my page
similar report
https://hackerone.com/reports/265696
To solve this issue
put this link http://unbouncepages.com/savemyphone/
or remove the redirection 
Please let me know if you have any questions. I am happy to help

## Impact

broken link hijacking
Moreover it leads to the loss in the reputation of the company

thanks.

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
