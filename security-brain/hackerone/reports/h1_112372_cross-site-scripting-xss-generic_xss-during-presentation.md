---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '112372'
original_report_id: '112372'
title: XSS during presentation
weakness: Cross-site Scripting (XSS) - Generic
team_handle: zaption
created_at: '2016-01-23T00:26:03.038Z'
disclosed_at: '2017-10-28T17:34:20.471Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS during presentation

## Metadata

- HackerOne Report ID: 112372
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: zaption
- Disclosed At: 2017-10-28T17:34:20.471Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

It is possible for a presenter to xss a viewer
Video attached:

## Recreation steps
Create publish lesson and start a presentation (join presentation in another browser)
Select "Quick question"
Open response
Insert the question 
asdf"><img src=x onerror=prompt(1)>

The Javascript will fire on the presenter's side and the viewers side.

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
