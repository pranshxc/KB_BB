---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '299835'
original_report_id: '299835'
title: Link poisoning on https://secure.login.gov/ login page
weakness: Open Redirect
team_handle: gsa_bbp
created_at: '2017-12-21T15:13:50.828Z'
disclosed_at: '2019-03-25T18:06:44.434Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 56
tags:
- hackerone
- open-redirect
---

# Link poisoning on https://secure.login.gov/ login page

## Metadata

- HackerOne Report ID: 299835
- Weakness: Open Redirect
- Program: gsa_bbp
- Disclosed At: 2019-03-25T18:06:44.434Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This link leads to the genuine secure.login.gov login page, in French: 
https://secure.login.gov/fr?host=portswigger.net

However, if you try to change the language to English using the bar at the bottom you'll end up an external website of my choice. As users won't expect changing their language to place them on an external website, the attacker could launch a highly effective phishing attack from there by impersonating secure.login.gov

## Impact

This vulnerability makes it possible to launch phishing attacks originating from secure.login.gov

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
