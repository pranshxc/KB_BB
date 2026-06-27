---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '4811'
original_report_id: '4811'
title: dashboard/pages/types [Unknown column 'Array' in 'where clause'] disclosure.
weakness: Information Disclosure
team_handle: concretecms
created_at: '2014-03-26T02:57:01.895Z'
disclosed_at: '2014-06-09T18:29:22.224Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# dashboard/pages/types [Unknown column 'Array' in 'where clause'] disclosure.

## Metadata

- HackerOne Report ID: 4811
- Weakness: Information Disclosure
- Program: concretecms
- Disclosed At: 2014-06-09T18:29:22.224Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

When I go to /index.php/dashboard/pages/types?ctID[]=4&task=edit I get thrown the following :
`mysqlt error: [1054: Unknown column 'Array' in 'where clause'] in EXECUTE("SELECT PageTypes.ctID, ComposerTypes.ctID as ctIDc, ctHandle, ctIsInternal, ctName, ctIcon, pkgID, ctComposerPublishPageMethod, ctComposerPublishPageTypeID, ctComposerPublishPageParentID from PageTypes left join ComposerTypes on PageTypes.ctID = ComposerTypes.ctID where PageTypes.ctID = Array")`

It's not a SQL Injection but it also shouldn't happen..

Best regards,

Olivier Beg

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
