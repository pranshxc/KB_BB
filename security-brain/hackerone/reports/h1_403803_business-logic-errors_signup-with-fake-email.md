---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '403803'
original_report_id: '403803'
title: SignUp With Fake Email
weakness: Business Logic Errors
team_handle: khanacademy
created_at: '2018-09-01T10:44:35.069Z'
disclosed_at: '2018-09-05T23:16:50.949Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
- business-logic-errors
---

# SignUp With Fake Email

## Metadata

- HackerOne Report ID: 403803
- Weakness: Business Logic Errors
- Program: khanacademy
- Disclosed At: 2018-09-05T23:16:50.949Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello KhanAcademy Security Team,

I'm rootbakar, I found an oddity that allows a user to register with Khanacademy using an invalid or fake email.

In this trial I used the email 'rootbakar@rootbakar.rootbakar' and after pressing the **SIGN UP** button it will automatically enter the user dashboard page, not through the account verification process first.

This will enable someone to create multiple accounts at once without verification.

**PoC**
This is Video Link
https://youtu.be/mvxF1vQigLI
(Not Public Video)

Best Regards,

**RootBakar**

## Impact

**This will enable someone to create multiple accounts at once without verification.**

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
