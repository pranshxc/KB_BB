---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '244287'
original_report_id: '244287'
title: 'Password token validation in Weblate Bypass #2'
team_handle: weblate
created_at: '2017-06-29T07:34:18.907Z'
disclosed_at: '2017-08-21T17:39:18.924Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
---

# Password token validation in Weblate Bypass #2

## Metadata

- HackerOne Report ID: 244287
- Weakness: 
- Program: weblate
- Disclosed At: 2017-08-21T17:39:18.924Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I also found the bypass to #229987 and #243842. 

Reproduction Steps:
1. Add multiple emails to an account
2. Request password reset for all emails
3. Use the link in each to make the change
4. All link works!

Shuaib

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
