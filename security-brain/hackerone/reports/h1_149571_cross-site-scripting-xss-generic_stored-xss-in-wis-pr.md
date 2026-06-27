---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '149571'
original_report_id: '149571'
title: Stored XSS in wis.pr
weakness: Cross-site Scripting (XSS) - Generic
team_handle: whisper
created_at: '2016-07-06T15:10:27.616Z'
disclosed_at: '2016-10-16T07:14:47.698Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in wis.pr

## Metadata

- HackerOne Report ID: 149571
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: whisper
- Disclosed At: 2016-10-16T07:14:47.698Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I detected a Stored XSS in wis.pr. These are the steps to reproduce the bug:

1. Create a new group named: Test>"<script>alert('test');</script>
2. Copy the sharing URL (http://wis.pr/*****).
3. Open this URL in a browser.

Please find the attached screenshots.

Fix: Sanitize the output in twitter:description meta. Please find attached the screenshot named "fix.jpg".

Don't hesitate to contact me if you need further details.

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
