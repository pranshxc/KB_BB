---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '975024'
original_report_id: '975024'
title: Reflected XSS in https://███████ via search parameter
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2020-09-05T03:13:30.456Z'
disclosed_at: '2020-11-02T21:41:37.622Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS in https://███████ via search parameter

## Metadata

- HackerOne Report ID: 975024
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2020-11-02T21:41:37.622Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Reflected XSS in https://█████████

**Description:**
I noticed I got an error when visiting https://███.mil stating
```The provided hostname is not valid for this server```

I pinged the site to see that it resolves to https://██████

 ██████

Based on the content of the site I believe this asset is a DOD asset due to the logos and verbiage. The staff page has all @mail.mil email contacts. If I should report this to https://www.us-cert.gov/report instead, please allow me to self close this as the owner/operator on this one is tough to determine.

 ██████████

The search parameter is subject to Reflected XSS

 - Visit https://█████/search?search_text=%3Cscript%3Ealert%28document.domain%29%3C%2Fscript%3E
 - See the response in browser

 ████

## Impact

Reflected XSS allows an attacker to send seemingly legitimate links to a victim, potentially stealing cookies or other sensitive session data via unwanted javascript execution

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
