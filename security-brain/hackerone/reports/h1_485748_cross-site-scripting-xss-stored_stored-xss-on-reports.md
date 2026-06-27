---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '485748'
original_report_id: '485748'
title: Stored XSS on reports.
weakness: Cross-site Scripting (XSS) - Stored
team_handle: x
created_at: '2019-01-25T08:22:50.228Z'
disclosed_at: '2019-04-01T16:39:45.718Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 216
asset_identifier: mopub.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS on reports.

## Metadata

- HackerOne Report ID: 485748
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: x
- Disclosed At: 2019-04-01T16:39:45.718Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** 
Stored XSS can be submitted on reports, and anyone who will check the report the XSS will trigger. 

**Description:**
Stored XSS, also known as persistent XSS, is the more damaging than non-persistent XSS. It occurs when a malicious script is injected directly into a vulnerable web application. 

## Steps To Reproduce:

  1. Go to https://app.mopub.com/reports/custom/
  2. Click **New network report**.
  3. On the name, enter payload: **"><img src=x onerror=alert(document.domain)>**
  4. Click **Run and save** then XSS will trigger. 

**Demonstration of the vulnerability:**
PoC: ████


Tested on Firefox and chrome.

## Impact

The attacker can steal data from whoever checks the report.

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
