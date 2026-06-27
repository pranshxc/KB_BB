---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '260941'
original_report_id: '260941'
title: 'UX: JS error on Password Safety link'
weakness: Business Logic Errors
team_handle: legalrobot
created_at: '2017-08-17T06:13:18.954Z'
disclosed_at: '2017-09-17T23:36:28.951Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: app.legalrobot.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# UX: JS error on Password Safety link

## Metadata

- HackerOne Report ID: 260941
- Weakness: Business Logic Errors
- Program: legalrobot
- Disclosed At: 2017-09-17T23:36:28.951Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**steps**
https://app.legalrobot.com/account

I just signed up to legal robot 
In my  account settings 
There is a div that contains 

Password Safety
To keep your information secure, Legal Robot periodically checks your password against public lists of hacked passwords (**here's how**). Since your account is fairly new, we have not run this check yet.


In that **here's how** is displayed in <a> tag without any href associated to it 
{F213603}

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
