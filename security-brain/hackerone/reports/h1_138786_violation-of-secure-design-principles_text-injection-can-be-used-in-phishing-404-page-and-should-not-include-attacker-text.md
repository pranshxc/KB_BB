---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '138786'
original_report_id: '138786'
title: Text injection can be used in phishing 404 page and should not include attacker
  text
weakness: Violation of Secure Design Principles
team_handle: veris
created_at: '2016-05-14T12:58:45.635Z'
disclosed_at: '2016-05-17T06:23:20.042Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# Text injection can be used in phishing 404 page and should not include attacker text

## Metadata

- HackerOne Report ID: 138786
- Weakness: Violation of Secure Design Principles
- Program: veris
- Disclosed At: 2016-05-17T06:23:20.042Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello i want to report a text injection and a missconfiguration of the 404 page which can be used in phishing

the bug exists at :

http://veris.in/test/%2f../It%20has%20been%20changed%20by%20a%20new%20one%20https://www.crowdcurity.com%20so%20go%20to%20the%20new%20one%20since%20this%20one

As you can see attacker text is included 
"It has been changed by a new one https://www.crowdcurity.com so go to the new one since this one was not found on this server."

Fix : just use a 404 page that don't include attacker text just as : hackerone do (a 404 page that don't include any external text 

Hope you fix it

Thanks,
Kanwar

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
