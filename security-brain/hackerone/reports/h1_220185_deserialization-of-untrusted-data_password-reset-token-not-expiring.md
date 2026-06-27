---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '220185'
original_report_id: '220185'
title: Password reset Token not expiring
weakness: Deserialization of Untrusted Data
team_handle: skyliner
created_at: '2017-04-11T11:51:16.888Z'
disclosed_at: '2017-04-11T18:04:47.153Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- deserialization-of-untrusted-data
---

# Password reset Token not expiring

## Metadata

- HackerOne Report ID: 220185
- Weakness: Deserialization of Untrusted Data
- Program: skyliner
- Disclosed At: 2017-04-11T18:04:47.153Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,

Here in this scenario, I've found that the there's a kind of server side side invalidation of Password Reset tokens. Like if I've requested for password reset token (token1) and I don't use it,  after I will make another request for password reset token (token2). This time I'll use the token2 means the link that I requested for the second time, so the first token (token1) should explicitly expire by the server. But here I can use the token1 also after password change by token2, this is unusual behavior of web application.

Exploit Scenario:
 If victim's email account is still logged into his/her Office Computers or any public Internet Cafe. Then any external attacker can use the unused token to reset victims token.

Proof of Concept:  
1. Go to https://www.skyliner.io/forgot-password and ask for password reset link.
2. Don't use the link keep it in Email inbox.
3. After some time repeat the step 1.
4. This time use the password reset link which was asked in step 3. means the 2nd link.
5. After changing the password, use the password reset link that was captured in step 1.
6. You'll see the password reset link is not expired even after password change.

I've also explained you the Exploit Scenario, now its all upto you.

Regards,
Sahil Tembhare

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
