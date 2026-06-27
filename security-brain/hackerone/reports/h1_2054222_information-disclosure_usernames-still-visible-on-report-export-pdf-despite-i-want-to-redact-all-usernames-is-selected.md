---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2054222'
original_report_id: '2054222'
title: Usernames still visible on report export pdf despite "I want to redact all
  usernames" is selected
weakness: Information Disclosure
team_handle: security
created_at: '2023-07-06T22:57:40.265Z'
disclosed_at: '2023-08-08T08:24:05.630Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 70
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Usernames still visible on report export pdf despite "I want to redact all usernames" is selected

## Metadata

- HackerOne Report ID: 2054222
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2023-08-08T08:24:05.630Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

Hi Team,

Export report via .pdf still disclosing the reporter username despite I exported it with __"I want to redact all usernames"__ being selected to redact all the usernames.

{F2475645}

### Steps To Reproduce

1. Login and try to export any report using export as .pdf
2. Select "I want to redact all usernames"
3. Check the exported .pdf report is still disclosing the username of researcher

https://hackerone.com/reports/<REPORT-ID>.pdf?redact_usernames=true&pdf_type=reporter

PoC screenshot below:

█████

The .pdf looks messy (maybe design issue) but if you will take a look at __Reported by:__ section at the report header, you will see: `<REDACTED> (<REDACTED>j<REDACTED>a<REDACTED>p<REDACTED>z<REDACTED>)` If you removed the `<REDACTED>` it will show the username `japz`.

If you removed all `<REDACTED>`, you will see something like the screenshot below:

█████

## Impact

Information Disclosure

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
