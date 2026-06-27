---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '124975'
original_report_id: '124975'
title: Cross-site Scripting (XSS) autocomplete generation in https://www.uber.com/
weakness: Cross-site Scripting (XSS) - Generic
team_handle: uber
created_at: '2016-03-22T15:27:39.222Z'
disclosed_at: '2016-03-24T18:52:24.629Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Cross-site Scripting (XSS) autocomplete generation in https://www.uber.com/

## Metadata

- HackerOne Report ID: 124975
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: uber
- Disclosed At: 2016-03-24T18:52:24.629Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Description:
The website located at https://www.uber.com/ suffers from a generated Cross-site Scripting (XSS) vulnerability in the "find a city" input field. 

Reproduction Steps:

Open the latest Chrome web browser

Navigate to the following URL's "find a city input field":
https://www.uber.com/

Type in the following:
<script>alert(1)</script>

Note that the autocomplete result being generated from the server side is raw javascript and payload was fired.

I’ve tested this in the latest Chrome. Attached to this report are screenshots of this issue occurring in chrome.

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
