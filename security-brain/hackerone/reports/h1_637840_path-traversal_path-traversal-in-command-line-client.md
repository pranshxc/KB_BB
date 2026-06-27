---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '637840'
original_report_id: '637840'
title: Path traversal in command line client
weakness: Path Traversal
team_handle: mariadb
created_at: '2019-07-08T19:17:44.126Z'
disclosed_at: '2020-05-28T18:59:16.286Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: MariaDB Server & Connectors - Data corruption, exfiltration, disclosure
asset_type: SOURCE_CODE
max_severity: medium
tags:
- hackerone
- path-traversal
---

# Path traversal in command line client

## Metadata

- HackerOne Report ID: 637840
- Weakness: Path Traversal
- Program: mariadb
- Disclosed At: 2020-05-28T18:59:16.286Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The command line client has a directory traversal bug which allows server chosen files to be dlopened when it connects to a malicious server.

The path can also be padded with `/` characters so that `strxnmov` drops the `.so` extension.

The `dlopen` call is performed here: <https://github.com/MariaDB/server/blob/10.5/sql-common/client_plugin.c#L368>

## Impact

In rare situations where the attacker controls a file at a known location on the victim's machine this can lead to code execution using `init/fini` functions. See attached `dlopen.sh`.

Other side effects present in commonly installed software are not to be neglected. The mecanism is far from being uncommon in C files alone according to this search:

<https://codesearch.debian.net/search?q=__attribute__.*constructor+filetype%3Ac&perpkg=1>

Without abusing the path traversal bug the dialog plugin might also be used to fool a user into sending its password unhashed. See attached `dialog.sh`.

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
