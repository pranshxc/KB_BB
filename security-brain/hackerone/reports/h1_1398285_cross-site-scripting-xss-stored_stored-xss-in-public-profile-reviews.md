---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1398285'
original_report_id: '1398285'
title: Stored XSS in Public Profile Reviews
weakness: Cross-site Scripting (XSS) - Stored
team_handle: judgeme
created_at: '2021-11-11T13:59:07.071Z'
disclosed_at: '2023-02-01T03:30:06.150Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 23
asset_identifier: judge.me
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in Public Profile Reviews

## Metadata

- HackerOne Report ID: 1398285
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: judgeme
- Disclosed At: 2023-02-01T03:30:06.150Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Summary:
Stored XSS found in public profile review in which we can add product details in shop addition options. In description of shop product we can add data URI XSS in HTML format which is led to XSS once user click on HTML.
In data URI XSS payload is encrypted in base64

Steps To Reproduce:
  1. Login with registered username and go to profile.
  2. After that click on add recommendation and add product details and in it's description add below payload:
<a href="data:text/html;charset=utf-7;base64,PHNjcmlwdD5hbGVydCgiWFNTIik8L3NjcmlwdD4=">Click Here</a>
{ Data URI XSS: data:text/html;charset=utf-7;base64,PHNjcmlwdD5hbGVydCgiWFNTIik8L3NjcmlwdD4=
(PHNjcmlwdD5hbGVydCgiWFNTIik8L3NjcmlwdD4=) : <script>alert('XSS')</script> }
  3. Now save the form by filling rest columns.
  4. If any one views public profile and click on HTML tag, it will trigger XSS.

Proof Of Concept:
Video POC attached

## Impact

Attacker can execute XSS in the victim user using judge platform

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
