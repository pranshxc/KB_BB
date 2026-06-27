---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1799562'
original_report_id: '1799562'
title: Reflected XSS on ██████.mil
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2022-12-11T14:19:02.316Z'
disclosed_at: '2023-01-27T18:38:36.662Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 18
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on ██████.mil

## Metadata

- HackerOne Report ID: 1799562
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2023-01-27T18:38:36.662Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
While looking for *.mil, I found a website that is vulnerable to reflected XSS.

## Impact

An attacker can use it to fetch cookies/tokens from any website which requires login by using a CORS bug if the site is vulnerable to CORS.

## System Host(s)
████.mil

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Go to this URL: https://███████████████████html
2. On the search bar, write this payload. <script>alert(document.cookie)</script>
3. & you'll see the pop-up.

## Suggested Mitigation/Remediation Actions

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
