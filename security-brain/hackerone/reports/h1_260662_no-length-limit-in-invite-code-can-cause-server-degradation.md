---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '260662'
original_report_id: '260662'
title: No length limit in invite_code can cause server degradation
team_handle: legalrobot
created_at: '2017-08-16T09:45:54.392Z'
disclosed_at: '2017-08-31T04:57:44.411Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
asset_identifier: app.legalrobot-test.com
asset_type: URL
max_severity: none
tags:
- hackerone
---

# No length limit in invite_code can cause server degradation

## Metadata

- HackerOne Report ID: 260662
- Weakness: 
- Program: legalrobot
- Disclosed At: 2017-08-31T04:57:44.411Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

I get to know that in every field is secured by restricted limit by length,
but, i can see that one place where you forget to add that security feature , which can cause server degradation.

https://app.legalrobot-uat.com/dmca-safe-harbor

Here, i can see feature to add invite-code , but i can see there is no length limit in that filed.

i can recommend to restrict limit to 10-12 character (as per business requirement ).

Thanks,
Vishal.

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
