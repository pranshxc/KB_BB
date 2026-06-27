---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '189726'
original_report_id: '189726'
title: Websites opened from reports can change url of report page
weakness: Open Redirect
team_handle: security
created_at: '2016-12-09T04:49:18.556Z'
disclosed_at: '2017-02-25T11:57:56.523Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 50
tags:
- hackerone
- open-redirect
---

# Websites opened from reports can change url of report page

## Metadata

- HackerOne Report ID: 189726
- Weakness: Open Redirect
- Program: security
- Disclosed At: 2017-02-25T11:57:56.523Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This issue is similar to #124889, but it is only exploitable via MS Edge or Internet Explorer 11

Proof Of Concept:
Clicking on a link set to "http://d214mfsab.org/same.html" (including this one) will change the still-open report page to http://example.com. This works on current versions of MS Edge and Internet Explorer 11.

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
