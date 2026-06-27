---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '212721'
original_report_id: '212721'
title: 'javascript: and mailto: links are allowed in JIRA integration settings'
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2017-03-01T20:18:26.269Z'
disclosed_at: '2017-04-10T17:49:55.366Z'
has_bounty: true
visibility: full
substate: duplicate
vote_count: 12
tags:
- hackerone
- violation-of-secure-design-principles
---

# javascript: and mailto: links are allowed in JIRA integration settings

## Metadata

- HackerOne Report ID: 212721
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2017-04-10T17:49:55.366Z
- Has Bounty: Yes
- Visibility: full
- Substate: duplicate

## Original Report

**Summary:**
For new feature settings, you accept website URLs like javascript:// or data:// in base urls. Even https://evil.com works, this needs to be stripped, this can be used to create another integrations without 

### Steps To Reproduce

1. https://hackerone.com/(Team)/integrations/jira/edit
2. Try in Base URL: javascript:// or data://
3. It will save and opens it everytime when escalate

### Optional: Your Environment (Browser version, Device, etc)
Works in all browsers

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
