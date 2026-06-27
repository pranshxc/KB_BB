---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1714563'
original_report_id: '1714563'
title: Jolokia Reflected XSS
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: mars
created_at: '2022-09-27T17:29:15.550Z'
disclosed_at: '2022-10-27T17:36:02.153Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
asset_identifier: '*.mars.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Jolokia Reflected XSS

## Metadata

- HackerOne Report ID: 1714563
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: mars
- Disclosed At: 2022-10-27T17:36:02.153Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

(salam)
Hi team i hope you are well , after doing some recon on mars.com i saw that the website use jolkia 1.3.5 it's vulnerable to reflected XSS  

## Steps To Reproduce:

  1. Vuln Link : https://couponsmanager-uat.b2b.mars.com/jolokia/read%3Csvg%20onload=alert(document.cookie)%3E?mimeType=text/html

## Supporting Material/References:
CVE-2018-1000129

Jolkia - Version
{F1957663}


##POC 

{F1957668}

## Impact

If an attacker can control a script that is executed in the victim's browser, then they can typically fully compromise that user. Amongst other things, the attacker can:
Perform any action within the application that the user can perform.
View any information that the user is able to view.
Modify any information that the user is able to modify.
Initiate interactions with other application users, including malicious attacks, that will appear to originate from the initial victim user.

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
