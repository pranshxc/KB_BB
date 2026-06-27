---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '123027'
original_report_id: '123027'
title: Edit Auto Response Messages
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2016-03-14T17:11:26.289Z'
disclosed_at: '2016-03-15T03:01:18.257Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# Edit Auto Response Messages

## Metadata

- HackerOne Report ID: 123027
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2016-03-15T03:01:18.257Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Not completely sure if this is by design due to encountering it for the first time.

When a company has `auto response` turned on, the reporter can change the contents of the message without any problems.
The reporter should not be able to change the contents of the companies auto response in any way due to the fact that they should not have privileges to that feature.

PoC:
Users can abuse this by changing the contents of the auto response to something else.

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
