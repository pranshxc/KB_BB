---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7915'
original_report_id: '7915'
title: Uninitialized variable error message leaks information
weakness: Information Disclosure
team_handle: localize
created_at: '2014-04-17T20:08:15.653Z'
disclosed_at: '2014-04-18T22:07:00.047Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- information-disclosure
---

# Uninitialized variable error message leaks information

## Metadata

- HackerOne Report ID: 7915
- Weakness: Information Disclosure
- Program: localize
- Disclosed At: 2014-04-18T22:07:00.047Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

An uninitialized variable `$alert` at line 630 in `index.php` shows an error message. This happens after a `POST /pages/create_project`. The error message does not appear in the browser because the user is redirected to the new project immediately, but it is there in the HTTP response (see error.png).

This is probably fixed with something like this at line 630.
`if(isset($alert)) echo UI::getPage(UI::PAGE_CREATE_PROJECT, array($alert));`

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
