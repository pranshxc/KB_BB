---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '174449'
original_report_id: '174449'
title: Researcher gets email updates on a private program after he/she quits that
  program.
weakness: Information Disclosure
team_handle: security
created_at: '2016-10-07T06:40:41.033Z'
disclosed_at: '2016-11-21T08:12:53.406Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- information-disclosure
---

# Researcher gets email updates on a private program after he/she quits that program.

## Metadata

- HackerOne Report ID: 174449
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2016-11-21T08:12:53.406Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
I found out that after I quit private program, I still gets update about that program, e.g. new scope changes/amount of money and etc.

**Description (Include Impact):**
I noticed that if I quit program I still gets email updates about the private program, private data can be leak on that email.

### Steps To Reproduce
1. I got invite to █████ private program.
2. After period of time I quit that program.
3. I still get email updates about that program.

### soultions
1. Remove email address from program once hacker quit.
2. Set boolean flag, true/false once the user quit. (The flag can help once the user gets invite again or if he/she wants to rejoin).

Thanks,
Sasi

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
