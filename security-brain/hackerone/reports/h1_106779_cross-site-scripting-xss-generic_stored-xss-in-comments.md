---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '106779'
original_report_id: '106779'
title: Stored XSS in comments
weakness: Cross-site Scripting (XSS) - Generic
team_handle: zendesk
created_at: '2015-12-24T14:13:35.294Z'
disclosed_at: '2016-01-01T20:09:21.751Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in comments

## Metadata

- HackerOne Report ID: 106779
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: zendesk
- Disclosed At: 2016-01-01T20:09:21.751Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

Here are the steps to reproduce:

1) Go to any help articles or some place where you can comment

2) Type in the comment as: `[click this link](data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K)`

3) Now click on the text `click this link` on your comments and XSS is executed !

This is quite similar to #82725 but with a slight different payload.

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
