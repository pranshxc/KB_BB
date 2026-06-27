---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '181810'
original_report_id: '181810'
title: HTML Injection in email /webApp/lahti (viestinta.lahitapiola.fi)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: localtapiola
created_at: '2016-11-12T19:13:49.070Z'
disclosed_at: '2016-12-10T10:57:20.253Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# HTML Injection in email /webApp/lahti (viestinta.lahitapiola.fi)

## Metadata

- HackerOne Report ID: 181810
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: localtapiola
- Disclosed At: 2016-12-10T10:57:20.253Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Steps to reproduce**
1. Open link http://viestinta.lahitapiola.fi/webApp/lahti
2. Set "Etunimi" `<a href="//bf.am">Welcome</a>`
3. Set "Sähköposti" to victim email
4. Other fields may be arbitrary
5. Submit form

{F134348}

**Result**
Victim receive an email from tilaisuudet.markkinointi@lahitapiola.fi which contains a link to a fake site.

{F134349}

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
