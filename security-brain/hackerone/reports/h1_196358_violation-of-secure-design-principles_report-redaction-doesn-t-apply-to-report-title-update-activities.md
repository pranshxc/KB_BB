---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '196358'
original_report_id: '196358'
title: Report redaction doesn't apply to report title update activities
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2017-01-06T18:54:28.012Z'
disclosed_at: '2017-02-25T03:17:48.704Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 27
tags:
- hackerone
- violation-of-secure-design-principles
---

# Report redaction doesn't apply to report title update activities

## Metadata

- HackerOne Report ID: 196358
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2017-02-25T03:17:48.704Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
The *Redact* option doesn't redact all keywords identified in the report- which may leave sensitive information unredacted.

**Description (Include Impact):**
The option only search through reporter's initial report & follow-up comments, leaving other comments untouched. Furthermore, it doesn't search in changes to report status. For better clarity, please refer to my screenshot attached.   
For example, if a team member has changed the report title, it fails to redact changes. Any such status changes are left untouched which is insufficient prior to full disclosure IMO.  

### Steps To Reproduce
For easier reproduction, please;  
1. Change report Title prior to redact keywords  
2. Now, redact some texts from report title as in screenshot  

Screenshots:  
{F149867}

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
