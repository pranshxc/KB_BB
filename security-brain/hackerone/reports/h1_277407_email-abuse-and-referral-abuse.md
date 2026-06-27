---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '277407'
original_report_id: '277407'
title: Email abuse and Referral Abuse
team_handle: unikrn
created_at: '2017-10-15T13:44:43.993Z'
disclosed_at: '2019-06-12T16:27:26.873Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
asset_identifier: unikrn.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Email abuse and Referral Abuse

## Metadata

- HackerOne Report ID: 277407
- Weakness: 
- Program: unikrn
- Disclosed At: 2019-06-12T16:27:26.873Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

**Summary:** Abuse of Email Invite and Referral Abuse
**Description:** 

Logic Flaws :
1. Users have been provided with an option to invite friends as referrals. It is possible to abuse your email invite service by repeating the same request. It is a discredit to unikrn if someone repeatedly sends the referral mail to same account. A simple php script will do that work and also loss of server resources. 

2. It is possible to invite myself from my referral link and even verify account and get coins.
Using same emails to produce multiple accounts on Unikrn:

3. The above flaw is more serious than self referring.
  I can get verified account by using someone else's alias email (krishn.akrish759213@gmail.com ) which Unikrn thinks is unregistered. The user with email(krishna.krish759213@gmail.com ) gets a verification link. He thinks it is a normal verification of his own account and verifies by clicking on it.



## Steps To Reproduce:
  1. Create an account with own email say "Krishna.krish759213@gmail.com"
  2. Verify it! Get your referral link.
  3. Clear cookies and create a new account with email like "krishn.akrish759213@gmail.com"
  4. Even though unikrn considers it as a new email, it is same in terms of gmail.
  5. Therefore same account get a mail saying to verify.  Just verify it.

Krishna.krish759213@gmail.com and krishnak.rish759213@gmail.com are same and it is possible to fake as many times as all possible permutation of dot in the email.

It is possible to write automate the entire process of referral abuse using single email with a simple php CURL script.

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
