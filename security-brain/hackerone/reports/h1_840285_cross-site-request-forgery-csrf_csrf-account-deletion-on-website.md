---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '840285'
original_report_id: '840285'
title: CSRF Account Deletion on ███ Website
weakness: Cross-Site Request Forgery (CSRF)
team_handle: deptofdefense
created_at: '2020-04-05T00:58:26.478Z'
disclosed_at: '2020-07-09T04:23:40.660Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 23
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF Account Deletion on ███ Website

## Metadata

- HackerOne Report ID: 840285
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: deptofdefense
- Disclosed At: 2020-07-09T04:23:40.660Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

A CSRF vulnerability against the [███████](████) allows attackers to delete user accounts. 

## Impact

Users who visit a malicious website could find their ████████ account deleted. 

## Step-by-step Reproduction Instructions

1. Create and login to a new account on the [██████](███████)
2. Open the provided HTML file and press the "POC" button. Note that the POC button is used only to make testing easier, and is not necessary in an actual attack scenario. 
3. Refresh the page on the ███ website. You should find that you have been logged out, and are unable to sign back into your account. 

██████

## Product, Version, and Configuration (If applicable)

**Website**: [███████](██████████)

## Suggested Mitigation/Remediation Actions

Enforce proper CSRF control on the ██████, for example with Google captcha (which is already implemented through much of the site).

## Impact

Users who visit a malicious website could find their account deleted.

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
