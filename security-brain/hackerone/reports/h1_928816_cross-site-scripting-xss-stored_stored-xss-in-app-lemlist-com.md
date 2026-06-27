---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '928816'
original_report_id: '928816'
title: Stored XSS in app.lemlist.com
weakness: Cross-site Scripting (XSS) - Stored
team_handle: lemlist
created_at: '2020-07-21T18:32:17.979Z'
disclosed_at: '2020-07-23T13:20:13.506Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: app.lemlist.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in app.lemlist.com

## Metadata

- HackerOne Report ID: 928816
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: lemlist
- Disclosed At: 2020-07-23T13:20:13.506Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
[add summary of the vulnerability]

## Steps To Reproduce:
  - Go to Company > Buddies-to-Be > Custom variables
  - Add malicious code: `" onmouseover="confirm(document.domain)" a="`

{F915718}

  -  Go to Company > Messages > Blank email
  - In the WYSIWYG  editor select `Custom variables`
  - Malicious code executed

{F915719}

## Impact

With this vulnerability, an attacker can for example steal users cookies or redirect users on malicious website.

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
