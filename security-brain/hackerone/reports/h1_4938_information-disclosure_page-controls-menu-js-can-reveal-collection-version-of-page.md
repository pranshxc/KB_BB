---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '4938'
original_report_id: '4938'
title: page_controls_menu_js can reveal collection version of page
weakness: Information Disclosure
team_handle: concretecms
created_at: '2014-03-27T18:14:29.271Z'
disclosed_at: '2014-03-31T22:35:37.749Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# page_controls_menu_js can reveal collection version of page

## Metadata

- HackerOne Report ID: 4938
- Weakness: Information Disclosure
- Program: concretecms
- Disclosed At: 2014-03-31T22:35:37.749Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

By visiting the url /tools/required/page_controls_menu_js?cID=<cID>&cvID=<cvID>

Where cID = page cID and cvID is unknown,

If for cvID you start at 1 (and the currently approved version is not the first version) the code `$(function() { ccmAlert.hud('This page is pending approval.', 5000); });` is added to the header.

If they increment the cvID to what the current approved version of a page, that line of code will go away. This discloses the currently approved version of a page (cvID of it).

This disclosure could be used with another attack to do harm to a site.

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
