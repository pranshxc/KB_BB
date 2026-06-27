---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '136720'
original_report_id: '136720'
title: don't leak server version of grtp.co in error pages
weakness: Information Disclosure
team_handle: gratipay
created_at: '2016-05-06T07:51:12.706Z'
disclosed_at: '2016-07-14T05:36:47.385Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- information-disclosure
---

# don't leak server version of grtp.co in error pages

## Metadata

- HackerOne Report ID: 136720
- Weakness: Information Disclosure
- Program: gratipay
- Disclosed At: 2016-07-14T05:36:47.385Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Open the latest Firefox web browser or google chrome.

Navigate to the following URL:
https://grtp.co/%pa

Note that the Invalid URL Encoded (%pa) has fired. after execution,It gives 404 error with server information and its version.

I’ve tested this in the latest Firefox and Chrome.

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
