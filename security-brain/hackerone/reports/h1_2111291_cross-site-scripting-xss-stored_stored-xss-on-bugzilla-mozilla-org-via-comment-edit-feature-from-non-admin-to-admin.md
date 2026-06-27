---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2111291'
original_report_id: '2111291'
title: Stored Xss on bugzilla.mozilla.org via comment edit feature from non-admin
  to admin.
weakness: Cross-site Scripting (XSS) - Stored
team_handle: mozilla
created_at: '2023-08-16T05:14:13.798Z'
disclosed_at: '2023-09-20T10:16:33.329Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
asset_identifier: bugzilla.mozilla.org
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored Xss on bugzilla.mozilla.org via comment edit feature from non-admin to admin.

## Metadata

- HackerOne Report ID: 2111291
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: mozilla
- Disclosed At: 2023-09-20T10:16:33.329Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi There !
There is Stored xss on comment feature.
The XSS executed when admin tries to edit the comment. The XSS fires.
I tried to Bypass the CSP But was not able to.

Steps To Reproduce.
1. Create a report in bugzilla.mozilla.org as users.
2.  Comment this xss payload as users ``</base</sTyle/</scRIpt/</textArea/</noScript/</tiTle/-->＜h1/<h1><image/onerror="import('data:application/javascript;charset=utf-8;base64,YWxlcnQoZG9jdW1lbnQuZG9tYWluKTtjb25zb2xlLmxvZyhkb2N1bWVudC5kb21haW4pOy8v')//%27"src><script>``
3. Now as admin, TRy to edit the comment, you will see xss popup with document.domain when csp disabled.

I am working on to bypass the csp
I have filed a bug report on bugzilla with my xss containing comment.
https://bugzilla.mozilla.org/show_bug.cgi?id=1848911
Try to edit and  check your browser console if csp is enabled. if csp isn't enabled, you will be able to see popup.
I tested this on my local instance, and this worked.

Thanks
Best Regards
r3dpars3c

## Impact

Client side javascript execution.

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
