---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1196945'
original_report_id: '1196945'
title: Reflected XSS at [████████]
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2021-05-14T03:04:47.759Z'
disclosed_at: '2021-06-30T20:45:54.165Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS at [████████]

## Metadata

- HackerOne Report ID: 1196945
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2021-06-30T20:45:54.165Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
Reflected XSS was found on the URL which can be used to steal cookies or perform any action on the behalf of the user.

## Impact

Cookie stealing, browser hijacking or any action can be performed on the behalf of the victim user

## System Host(s)
███

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Go to `https://███████%22%20onclick=%22/%3E%22%3Cimg%20src=x%20onerror=alert(1);%3E&pt=PT-15951-Pv0qVVSOyrbtIuulh8prGw8eNt4-██████████`
2. It will execute the XSS payload in the `███=` parameter in the URL.

## Suggested Mitigation/Remediation Actions
Sanitize the `███=` URL parameter properly.

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
