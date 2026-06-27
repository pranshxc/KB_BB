---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '112304'
original_report_id: '112304'
title: 'owncloud.help: Text  Injection'
weakness: Violation of Secure Design Principles
team_handle: owncloud
created_at: '2016-01-22T16:56:06.557Z'
disclosed_at: '2016-01-23T07:47:37.354Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 0
tags:
- hackerone
- violation-of-secure-design-principles
---

# owncloud.help: Text  Injection

## Metadata

- HackerOne Report ID: 112304
- Weakness: Violation of Secure Design Principles
- Program: owncloud
- Disclosed At: 2016-01-23T07:47:37.354Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello i want to report a text injection and a missconfiguration of the 404 page which can be used in phishing Text injection can be used in phishing 404 page should not include attacker text

The bug exists at :

https://owncloud.help/test/%2f../It%20has%20been%20changed%20by%20a%20new%20one%20https://www.crowdcurity.com%20so%20go%20to%20the%20new%20one%20since%20this%20one

as you can see attacker text is included
"It has been changed by a new one https://www.crowdcurity.com so go to the new one since this one was not found on this server."

Fix : just use a 404 page that don't include attacker text just as : hackerone.com,bugcrowd.com do (a 404 page that don't include any externel text
hope you fix it

Thanks

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
