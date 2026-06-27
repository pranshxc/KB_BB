---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '33432'
original_report_id: '33432'
title: BROKEN AUTHENTICATION IN MOBILE VERIFICATION
weakness: Violation of Secure Design Principles
team_handle: x
created_at: '2014-10-31T22:16:21.896Z'
disclosed_at: '2014-12-14T23:09:59.959Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# BROKEN AUTHENTICATION IN MOBILE VERIFICATION

## Metadata

- HackerOne Report ID: 33432
- Weakness: Violation of Secure Design Principles
- Program: x
- Disclosed At: 2014-12-14T23:09:59.959Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hey Team
this is geekboy :)

this report is about broken authentication in mobile section .

Description : 
when user want to add any mobile number to his account , he will go mobile section and twitter will ask the user to select the country and enter the mobile number .

so when testing i entered the random mobile number and twitter says that verification code sent to the mobile number , and asking for the verification code >> http://sd.uploads.im/NsmJl.png

i cant provide the code coz i entered the random number .

now i logged out my account and came to forget password page .

the issue is here , twitter asking me to send the verification code on the mobile number which i didn't verified and  its not associated with my account .  >> http://sd.uploads.im/LRUhA.png

so without verification Twitter should not associate the mobile number with account for the password reset purpose ! 

Thanks
geekboy :)

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
