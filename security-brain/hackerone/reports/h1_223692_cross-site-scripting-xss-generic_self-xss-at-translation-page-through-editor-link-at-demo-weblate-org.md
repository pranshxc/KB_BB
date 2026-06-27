---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223692'
original_report_id: '223692'
title: Self XSS at translation page through Editor Link at demo.weblate.org
weakness: Cross-site Scripting (XSS) - Generic
team_handle: weblate
created_at: '2017-04-25T08:07:25.328Z'
disclosed_at: '2017-05-17T16:48:51.756Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Self XSS at translation page through Editor Link at demo.weblate.org

## Metadata

- HackerOne Report ID: 223692
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: weblate
- Disclosed At: 2017-05-17T16:48:51.756Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

User input is not sanitized properly at Editor link causing self xss.

**Steps to reproduce**
1) Navigate to https://demo.weblate.org/accounts/profile/#preferences
2) Provide Editor link as javaScript:alert(document.cookie);//confirm(1); and click on Save
3) Navigate to English Translation page of the project at https://demo.weblate.org/translate/hello/master/en_GB/?type=all
4) Click on the main.c under Source Information
5) Self XSS executes showing user cookie

Mitigation:
Proper server side filtering of user input

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
