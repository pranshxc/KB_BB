---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '213114'
original_report_id: '213114'
title: Gitlab.com is vulnerable to reverse tabnabbing via AsciiDoc links. (#3)
weakness: UI Redressing (Clickjacking)
team_handle: gitlab
created_at: '2017-03-13T16:17:14.804Z'
disclosed_at: '2017-05-09T19:11:56.301Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- ui-redressing-clickjacking
---

# Gitlab.com is vulnerable to reverse tabnabbing via AsciiDoc links. (#3)

## Metadata

- HackerOne Report ID: 213114
- Weakness: UI Redressing (Clickjacking)
- Program: gitlab
- Disclosed At: 2017-05-09T19:11:56.301Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Dear GitLab bug bounty team,

# Summary
---
Gitlab.com is vulnerable to reverse tabnabbing in AsciiDoc files. 

# Why does this vulnerability exist?
---

In AsciiDoc the following `http://example.com[Reverse Tabnabbing^]` is equivalent to `<a href="http://example.com" target="_blank">Reverse Tabnabbing</a>`.

# How can this exploited?
---

Same scenario as https://hackerone.com/reports/211065. ;)

Best regards,
Ed

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
