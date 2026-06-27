---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '450315'
original_report_id: '450315'
title: XSS on www.██████ alerts and a number of other pages
weakness: Cross-site Scripting (XSS) - Generic
team_handle: deptofdefense
created_at: '2018-11-27T08:08:02.043Z'
disclosed_at: '2019-12-02T19:10:17.263Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS on www.██████ alerts and a number of other pages

## Metadata

- HackerOne Report ID: 450315
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: deptofdefense
- Disclosed At: 2019-12-02T19:10:17.263Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** If an action on ███████ results in an error, an error dialog is shown. This 
dialog, in certain scenarios, is vulnerable to stored XSS due to a lack of sanitization.

**Description:** In this specific example, I'll be using a GET endpoint that attempts to delete alerts based on an ID supplied. If the ID does not belong to the user, an error is displayed containing the ID. This ID is not sanitized when displayed in the error dialog.

Example PoC: `https://www.██████████/alerts/delete/id/1234<img+src+onerror%3d'alert(1)'>`

The previous PoC appears to be reflected but it is actually stored. Here's a PoC to prove that: `https://████████pythonanywhere.com/poc/xss/dod/4rspEdWG1tqA2pQ4bY4C`

## Impact
XSS

## Step-by-step Reproduction Instructions

1. Trick victim to visiting attacker.com
2. Attacker.com makes a GET request to `https://www.████/alerts/delete/id/1234<img+src+onerror%3d'<PAYLOAD>'>`
3. Redirect victim to `https://www.██████████/alerts/` or similar (like `https://www.████████/member/options`)

## Product, Version, and Configuration (If applicable)
https://www.█████

## Suggested Mitigation/Remediation Actions
Sanitization of the error message.

## Impact

XSS

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
