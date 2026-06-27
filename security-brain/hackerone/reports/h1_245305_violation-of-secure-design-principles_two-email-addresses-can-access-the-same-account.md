---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '245305'
original_report_id: '245305'
title: Two email addresses can access the same account
weakness: Violation of Secure Design Principles
team_handle: wakatime
created_at: '2017-07-02T10:48:40.090Z'
disclosed_at: '2017-07-03T06:55:29.972Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- violation-of-secure-design-principles
---

# Two email addresses can access the same account

## Metadata

- HackerOne Report ID: 245305
- Weakness: Violation of Secure Design Principles
- Program: wakatime
- Disclosed At: 2017-07-03T06:55:29.972Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,

When I was testing your web application I found that we can change the email address to a new email address.  I tested that feature and noticed that after changing the email to a new email and then back to the old email, I can still access the account using both the email addresses.  
Doing so doesn't allow the email holder of the second email address to create an account on Wakatime using the same email address, as the error shows that the email address has already been taken. I presume that this can be done for a number of emails as I haven't tested that yet. 
One account clearly shouldn't be accessible by 2 email address and is a violation of secure design principles.

Let me know if you need anything else. 

Best Regards,
Streaak2

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
