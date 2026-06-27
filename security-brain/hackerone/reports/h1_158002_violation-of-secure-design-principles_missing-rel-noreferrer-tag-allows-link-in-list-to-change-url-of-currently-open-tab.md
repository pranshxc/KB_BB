---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '158002'
original_report_id: '158002'
title: Missing rel=noreferrer tag allows link in list to change url of currently open
  tab
weakness: Violation of Secure Design Principles
team_handle: instacart
created_at: '2016-08-09T22:40:36.532Z'
disclosed_at: '2016-09-12T19:59:15.545Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# Missing rel=noreferrer tag allows link in list to change url of currently open tab

## Metadata

- HackerOne Report ID: 158002
- Weakness: Violation of Secure Design Principles
- Program: instacart
- Disclosed At: 2016-09-12T19:59:15.545Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

When adding links to lists, there is no rel=noreferrer tag present, allowing a linked page to change the url of the currently open tab. This can open the doors for phishing attacks, as users trust the tab that contained instacart.

As an example, see my list at https://inst.cr/t/1QmLPG. Clicking the link, which opens in a new tab, will change the url of the currently open tab to http://example.com.

Thank you for your time, and please let me know if you have any questions.

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
