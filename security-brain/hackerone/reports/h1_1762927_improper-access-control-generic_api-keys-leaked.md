---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1762927'
original_report_id: '1762927'
title: api keys leaked
weakness: Improper Access Control - Generic
team_handle: reddit
created_at: '2022-11-05T05:59:55.052Z'
disclosed_at: '2022-11-10T14:40:41.784Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 10
asset_identifier: '*.redditinc.com'
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
- improper-access-control-generic
---

# api keys leaked

## Metadata

- HackerOne Report ID: 1762927
- Weakness: Improper Access Control - Generic
- Program: reddit
- Disclosed At: 2022-11-10T14:40:41.784Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
[Disclosure of valid private keys may lead to unauthorized access to any systems that use them for authentication. Verify whether any keys disclosed are actually valid, and whether their disclosure within the application is appropriate]

## Impact:
[Disclosure of valid private keys may lead to unauthorized access to any systems that use them for authentication. Verify whether any keys disclosed are actually valid, and whether their disclosure within the application is appropriate]

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1.  open the url  redditinc.com
  2. copy the "redditinc" from url  
  3. using gitdork ("redditinc" apikey)
   4.open github search the gitdork 
 5.check the results

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

Disclosure of valid private keys may lead to unauthorized access to any systems that use them for authentication. Verify whether any keys disclosed are actually valid, and whether their disclosure within the application is appropriate

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
