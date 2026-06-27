---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223343'
original_report_id: '223343'
title: Already Registered Email Disclosure
weakness: Information Disclosure
team_handle: weblate
created_at: '2017-04-24T09:42:39.568Z'
disclosed_at: '2017-05-17T14:50:20.259Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- information-disclosure
---

# Already Registered Email Disclosure

## Metadata

- HackerOne Report ID: 223343
- Weakness: Information Disclosure
- Program: weblate
- Disclosed At: 2017-05-17T14:50:20.259Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,
In the registration at https://hosted.weblate.org/accounts/register/ , I found that trying an already used email would inform the register that you are trying used one, so with a dictionary of emails a hacker can determine the emails of all users in database and use that in phishing.

Note:I thought that I should report this because I found that all other functionalities don't reveal that the email is already used. Eg: Forget Password

Thanks.

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
