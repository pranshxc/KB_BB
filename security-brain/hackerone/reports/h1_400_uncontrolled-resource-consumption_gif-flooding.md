---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '400'
original_report_id: '400'
title: GIF flooding
weakness: Uncontrolled Resource Consumption
team_handle: security
created_at: '2013-11-15T01:35:22.622Z'
disclosed_at: '2013-11-30T12:44:26.582Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 38
tags:
- hackerone
- uncontrolled-resource-consumption
---

# GIF flooding

## Metadata

- HackerOne Report ID: 400
- Weakness: Uncontrolled Resource Consumption
- Program: security
- Disclosed At: 2013-11-30T12:44:26.582Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Current limits
---------------------
Image size: 1 MB
Image dimensions: 2048x2048px
File types: jpg/png/gif

Another image hack
---------------------
A GIF composed of 40k 1x1 images made Paperclip freeze until timeout.

As attachments I sent the file composed of 40k images, and a screenshot of the timeout.

Possible Fix
---------------------
Check if:
file size / (width * height) != ridiculous amount

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
