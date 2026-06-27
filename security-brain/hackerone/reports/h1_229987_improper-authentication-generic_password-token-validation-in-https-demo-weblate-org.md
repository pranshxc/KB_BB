---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '229987'
original_report_id: '229987'
title: Password token validation in https://demo.weblate.org/
weakness: Improper Authentication - Generic
team_handle: weblate
created_at: '2017-05-19T20:01:42.397Z'
disclosed_at: '2017-06-27T15:10:22.144Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# Password token validation in https://demo.weblate.org/

## Metadata

- HackerOne Report ID: 229987
- Weakness: Improper Authentication - Generic
- Program: weblate
- Disclosed At: 2017-06-27T15:10:22.144Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi team,

I noticed that when requesting multiple reset links at https://demo.weblate.org/ all tokens are valid and can be used.

In numerous applications the following policy is adopted as an additional security measure:

- keep valid only that token with shorter lifetime (last requested)

or

- invalidate all reset links generated after successful use of one of these tokens

Please check it.

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
