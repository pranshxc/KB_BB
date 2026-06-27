---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '106350'
original_report_id: '106350'
title: text injection can be used in phishing 404 page should not include attacker
  text
weakness: Violation of Secure Design Principles
team_handle: withinsecurity
created_at: '2015-12-21T19:38:25.518Z'
disclosed_at: '2016-01-16T01:05:51.443Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- violation-of-secure-design-principles
---

# text injection can be used in phishing 404 page should not include attacker text

## Metadata

- HackerOne Report ID: 106350
- Weakness: Violation of Secure Design Principles
- Program: withinsecurity
- Disclosed At: 2016-01-16T01:05:51.443Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello i want to report a text injection and a missconfiguration of the 404 page which can be used in phishing

the bug exists at :

https://withinsecurity.com/test/%2f../It%20has%20been%20changed%20by%20a%20new%20one%20https://www.crowdcurity.com%20so%20go%20to%20the%20new%20one%20since%20this%20one

as you can see attacker text is included 
"It has been changed by a new one https://www.crowdcurity.com so go to the new one since this one was not found on this server."

Fix : just use a 404 page that don't include attacker text just as : hackerone do (a 404 page that don't include any externel text 
hope you fix it
thanks

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
