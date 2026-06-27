---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1607645'
original_report_id: '1607645'
title: Add me email address Authentication bypass
team_handle: linkedin
created_at: '2022-06-20T14:37:18.023Z'
disclosed_at: '2022-07-15T16:33:19.782Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 6
asset_identifier: www.linkedin.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Add me email address Authentication bypass

## Metadata

- HackerOne Report ID: 1607645
- Weakness: 
- Program: linkedin
- Disclosed At: 2022-07-15T16:33:19.782Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

hi, this vulnerability can able to access user account without email verification in linkedins' add me email address function page. user add mail2 email address. without mail2 email address verification user can fully access mail1 linkedin account using mail2 email address. 

In linkedin mobile application, we can add second email address, and its display "We can't use this email for your account until you verify it." so, it'll play authentication logic error.

TO REPRODUCE :
1. have account mail1 & mail2.
2. login to mail1 linkedin account.
3. go to https://www.linkedin.com/psettings/email , add mail2 email address.
4. then remove mail2 email address.
5. linkedin sent verification link to mail2s' gmail.
6. copy this link, open private tab and paste it.
7. click signin button and type  mail1s' password.
8. will login successfully.

ATTACHED Detailed Reproduce Video below

## Impact

User/attacker can login successfully without email verification and also, authentication logic error happened. login using unverified email address, can't notify login successful message in the primary email address. email2 login n-no. of time without verification, and also can't notify login message to mail1(primary email) gmail account.

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
