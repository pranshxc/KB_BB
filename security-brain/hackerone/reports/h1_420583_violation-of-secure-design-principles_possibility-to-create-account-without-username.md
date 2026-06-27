---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '420583'
original_report_id: '420583'
title: possibility to create account without username
weakness: Violation of Secure Design Principles
team_handle: infogram
created_at: '2018-10-08T11:13:12.415Z'
disclosed_at: '2018-10-09T11:42:12.226Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
asset_identifier: infogram.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# possibility to create account without username

## Metadata

- HackerOne Report ID: 420583
- Weakness: Violation of Secure Design Principles
- Program: infogram
- Disclosed At: 2018-10-09T11:42:12.226Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

hi , 
infogram.com doesn't allow us to go next untill we give name of our account but i bypassed that. i am able to create an account without any name, just by modify response field.

#steps:-
1. create new account , when you reach page where you have to give your name.
2. give name and intercept the request , remove first name and last name and forward the request.
3. now you will get reponse with 400 bad gateway , you just need to remove it and modify with 200 and forward it , your account will be created.

here is the video poc  how to create account without any name 
{F357158}

regards

## Impact

bypass "name giving to account field to complete signup"

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
