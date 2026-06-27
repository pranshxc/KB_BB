---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1065964'
original_report_id: '1065964'
title: Stored XSS in the banner block description
weakness: Cross-site Scripting (XSS) - Stored
team_handle: stripo
created_at: '2020-12-24T18:23:13.040Z'
disclosed_at: '2021-03-09T10:11:48.691Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 25
asset_identifier: my.stripo.email
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in the banner block description

## Metadata

- HackerOne Report ID: 1065964
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: stripo
- Disclosed At: 2021-03-09T10:11:48.691Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Steps To Reproduce:

- Create a new template and add a banner block

{F1128944}

- Add a description to the banner block description: `"><img src=1 onerror=alert(document.domain)>`

- Malicious code executed

{F1128945}

## Proof Of Concept:

{F1128942}

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
