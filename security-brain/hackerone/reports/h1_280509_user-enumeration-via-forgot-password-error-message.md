---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '280509'
original_report_id: '280509'
title: User enumeration via forgot password error message
team_handle: infogram
created_at: '2017-10-24T17:36:07.917Z'
disclosed_at: '2017-10-27T08:05:08.652Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 1
asset_identifier: infogram.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# User enumeration via forgot password error message

## Metadata

- HackerOne Report ID: 280509
- Weakness: 
- Program: infogram
- Disclosed At: 2017-10-27T08:05:08.652Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Hi Team,

Vulnerable URL :
https://infogram.com/forgot

Description:
During testing forgot password field whether it's rate limiting is working or not, I noticed forgot password field is vulnerable to user enumeration. When user enter email id which is not available into database it shows an error " E-mail not recognized".

Mitigation: handle the above situation correctly, e.g.: "Reset link is send to email : xxxx@xxx.xxx". This doesn't inform the attacker  E-mail not recognized and make enumeration more difficult

Thanks and regards,
Kiddie

Refer Ticket : #77067
#123496

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
