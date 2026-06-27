---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '394861'
original_report_id: '394861'
title: Incorrect Permission Assignment for Critical Resource
weakness: Privilege Escalation
team_handle: mariadb
created_at: '2018-08-14T10:20:51.773Z'
disclosed_at: '2018-11-14T09:03:30.215Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: MariaDB Server & Connectors - Access control bypass
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Incorrect Permission Assignment for Critical Resource

## Metadata

- HackerOne Report ID: 394861
- Weakness: Privilege Escalation
- Program: mariadb
- Disclosed At: 2018-11-14T09:03:30.215Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Dear Team, 

Product Affected: https://github.com/MariaDB/server

File:
 /server/blob/10.3/sql/mysqld.cc#L2761

```
}
    if (!SetSecurityDescriptorDacl(&sdPipeDescriptor, TRUE, NULL, FALSE))
{
```

This was purely identified on code review, Never create NULL ACLs.

A mail was sent to security@mariadb.org and MariaDB team is working on this and a fix will be pushed in next version, attached mail headers for your reference.

## Impact

An attacker can set it to Everyone (Deny All  Access), which would even forbid administrator access and may lead to privilege escalation.

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
