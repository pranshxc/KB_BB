---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2421'
original_report_id: '2421'
title: Value of JSESSIONID  and XSRF token parameter in cookie remains same before
  and after login
weakness: Violation of Secure Design Principles
team_handle: relateiq
created_at: '2014-02-28T13:01:01.487Z'
disclosed_at: '2014-05-14T21:58:04.296Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# Value of JSESSIONID  and XSRF token parameter in cookie remains same before and after login

## Metadata

- HackerOne Report ID: 2421
- Weakness: Violation of Secure Design Principles
- Program: relateiq
- Disclosed At: 2014-05-14T21:58:04.296Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Here are two same values captured via intercepting the request and the value of JSESSIONID and XSRF remains same before and after login
JSESSIONID=m8u0pm8mjvckm1ya8da4oqlfb0pd34iw38lr; 
XSRF-TOKEN=6B025F41D13BC02E9D658409BAC23F84;

This could lead to further threats such as session hijacking etc

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
