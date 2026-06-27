---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '461345'
original_report_id: '461345'
title: 'Security issue: Github repo''s wiki publicly editable'
weakness: Improper Access Control - Generic
team_handle: iandunn-projects
created_at: '2018-12-12T17:12:29.436Z'
disclosed_at: '2018-12-12T18:06:50.611Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
asset_identifier: GitHub repositories
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Security issue: Github repo's wiki publicly editable

## Metadata

- HackerOne Report ID: 461345
- Weakness: Improper Access Control - Generic
- Program: iandunn-projects
- Disclosed At: 2018-12-12T18:06:50.611Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello Team,

Github repo's wiki page is publicly editable. This enables an attacker to edit the wiki pages of the affected repo's. Adding content that may link to malicious code libraries that would be installed and used by developers or information that may mislead users.

**POC Links:**
https://github.com/iandunn/MU-Migration/wiki
https://github.com/iandunn/wp-hammer/wiki
https://github.com/iandunn/gutenberg/wiki
https://github.com/iandunn/dotfiles/wiki

## Impact

This enables an attacker to edit the wiki pages of the affected repo's. Adding content that may link to malicious code libraries that would be installed and used by developers or information that may mislead users.

Thank you.

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
