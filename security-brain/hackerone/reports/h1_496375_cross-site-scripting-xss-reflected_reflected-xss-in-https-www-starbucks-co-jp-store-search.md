---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '496375'
original_report_id: '496375'
title: Reflected XSS in https://www.starbucks.co.jp/store/search/
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: starbucks
created_at: '2019-02-15T07:09:59.135Z'
disclosed_at: '2019-05-22T16:54:28.693Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 72
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS in https://www.starbucks.co.jp/store/search/

## Metadata

- HackerOne Report ID: 496375
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: starbucks
- Disclosed At: 2019-05-22T16:54:28.693Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Please indicate NA, if not applicable. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report!

**Summary:** 
I found a Refrect XSS in store locator pages.


**Description:**
This vulnerability would allow a user to insert javascript payloads which can be reflected in a browser.

## Steps To Reproduce:

1. Go to https://www.starbucks.co.jp/store/search/?free_word=%22%3E%3Cscript%3Ealert()%3C/script%3E%3E



## Reproduction environment
Firefox 65.0

## Impact

It is possible to run arbitrary javascript.


Thank you.

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
