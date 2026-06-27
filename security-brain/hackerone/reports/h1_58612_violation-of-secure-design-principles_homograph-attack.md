---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '58612'
original_report_id: '58612'
title: Homograph attack
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2015-04-26T17:58:53.549Z'
disclosed_at: '2015-05-02T22:34:51.056Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# Homograph attack

## Metadata

- HackerOne Report ID: 58612
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2015-05-02T22:34:51.056Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello!

I would like to report that fix of report #29491 is incomplete. There is another way to reproduce homograph attack: <http:ebаy.com> or <http:/ebаy.com>

IDNs are displayed in unicode and there is no encoding into Punycode on external link warning page

Thanks!

\- Matvejs

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
