---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '38890'
original_report_id: '38890'
title: stored XSS in concrete5 5.7.2.1
weakness: Cross-site Scripting (XSS) - Generic
team_handle: concretecms
created_at: '2014-12-10T01:15:36.706Z'
disclosed_at: '2016-04-26T23:28:43.317Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# stored XSS in concrete5 5.7.2.1

## Metadata

- HackerOne Report ID: 38890
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: concretecms
- Disclosed At: 2016-04-26T23:28:43.317Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello.

I found stored XSS in concrete5 5.7.2.1.

If the user have file upload permission
the user can upload the file named like 
"><img src=0 onerror=confirm(document.cookie)>.txt
or 
change title like below
<svg onload=confirm(document.cookie)>
on the properties page.

and when other user access the file manager page,
and open the delete page or open the properties page,
Javascript execute.

I reported same issue in 5.7.0.4. and fixed [#30019]
but this fix is not sufficient.

Regards.

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
