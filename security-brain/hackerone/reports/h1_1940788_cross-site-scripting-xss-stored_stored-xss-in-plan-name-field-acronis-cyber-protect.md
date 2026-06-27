---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1940788'
original_report_id: '1940788'
title: Stored XSS in plan name field (Acronis Cyber Protect)
weakness: Cross-site Scripting (XSS) - Stored
team_handle: acronis
created_at: '2023-04-10T13:47:41.741Z'
disclosed_at: '2023-10-09T09:49:10.984Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
asset_identifier: Acronis Cyber Protect
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in plan name field (Acronis Cyber Protect)

## Metadata

- HackerOne Report ID: 1940788
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: acronis
- Disclosed At: 2023-10-09T09:49:10.984Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary
It has been identified that a known and previously reported stored XSS vulnerability is still possible to be exploited and abused in the recent version of Acronis Cyber Protect (*15.0.31791*), released last March 7, 2023, (*evidence attached*).
This report is for no other purpose than to make it known that the vulnerability still persists.

## Steps To Reproduce
Be sure to follow the steps below to replicate this vulnerability:

  1. Create a new plan. Add a valid device.
  1. As plan name type the following payload: `<img src=x onerror=alert(/Stored_XSS/)>`
  1. Save the changes and wait for the plan to be created.
  1. Now stop the plan by pressing the "Stop" button.
  1. Before stopping it will ask for confirmation. Press the red "Confirm" button and the vulnerability will be triggered immediately.

Note that just below the browser window a bubble will appear with a temporary message trying to render our payload.

## Recommendations
You can avoid such vulnerabilities by escaping, validating data entries in fields and sanitizing suspicious and/or malicious entries. This text field is not supposed to contain/accept special characters or payloads.

## Impact

An XSS attack allows an attacker to execute arbitrary JavaScript in the context of the attacked website and the attacked user. This can be abused to steal session cookies, perform requests in the name of the victim or for phishing attacks.

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
