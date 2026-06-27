---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '46952'
original_report_id: '46952'
title: Markdown code block sequence makes report unreadable
team_handle: security
created_at: '2015-02-06T22:47:30.029Z'
disclosed_at: '2015-06-29T15:01:36.668Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
---

# Markdown code block sequence makes report unreadable

## Metadata

- HackerOne Report ID: 46952
- Weakness: 
- Program: security
- Disclosed At: 2015-06-29T15:01:36.668Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Proof of Concept**

Submitting a report/comment with an input like the following

"Three backticks followed by a newline followed by `-d*{d}d/<<d`"

will cause the report to be unreadable (I think it's because the parser is crashing?)

The attached file includes the input that I'm trying (with difficulty) to describe with text, since I can't actually include the crasher in the report.

This may have no security implications; the worst I can imagine doing with this is annoying people by creating reports that can't easily be closed.

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
