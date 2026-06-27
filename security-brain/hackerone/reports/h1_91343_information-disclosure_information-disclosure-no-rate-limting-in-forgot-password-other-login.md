---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '91343'
original_report_id: '91343'
title: Information disclosure (No rate limting in forgot password & other login)
weakness: Information Disclosure
team_handle: imgur
created_at: '2015-09-30T23:59:00.486Z'
disclosed_at: '2018-04-14T08:47:26.902Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 28
tags:
- hackerone
- information-disclosure
---

# Information disclosure (No rate limting in forgot password & other login)

## Metadata

- HackerOne Report ID: 91343
- Weakness: Information Disclosure
- Program: imgur
- Disclosed At: 2018-04-14T08:47:26.902Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi there,
I noticed a small information leak which allows an attacker to check whether an email address is associated with an account.If your account is not associated with website then an error will become raise that **"That username or email was not found."**
You should always return a status message like: **"If your email exists in our database, you'll receive a reset link"**. That way an attacker cannot distinguish between the two cases.
Also you should add rate limiting :)

Thanks,

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
