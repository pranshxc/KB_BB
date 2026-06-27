---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '30019'
original_report_id: '30019'
title: Stored XSS in concrete5 5.7.0.4.
weakness: Cross-site Scripting (XSS) - Generic
team_handle: concretecms
created_at: '2014-10-05T05:02:05.988Z'
disclosed_at: '2015-03-11T21:35:38.386Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in concrete5 5.7.0.4.

## Metadata

- HackerOne Report ID: 30019
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: concretecms
- Disclosed At: 2015-03-11T21:35:38.386Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello.

I found stored XSS in concrete5 5.7.0.4.

If the user have file upload permission
the user can upload the file named like 
"><svg onload=confirm(document.cookie)>.txt
and the file name is displayed without being escaped.

and when other user access the file manager page,
Execute Javascript code on page load.

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
