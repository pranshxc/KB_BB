---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '709072'
original_report_id: '709072'
title: Null byte Injection in https://████/
weakness: Improper Null Termination
team_handle: deptofdefense
created_at: '2019-10-07T15:36:44.075Z'
disclosed_at: '2020-05-14T17:17:48.736Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- improper-null-termination
---

# Null byte Injection in https://████/

## Metadata

- HackerOne Report ID: 709072
- Weakness: Improper Null Termination
- Program: deptofdefense
- Disclosed At: 2020-05-14T17:17:48.736Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

#Description:
Microsoft .NET Framework is prone to multiple NULL-byte injection vulnerabilities because it fails to adequately sanitize user-supplied data.

#Vulnerable URL: https://████/%2F%20This%20website%20is%20vulnerable%20to%20NULL%20BYTE%20INJECTION/

#Steps to Reproduce:
1) An attacker can exploit this issue via a browser.

The following example URI request is available:
https://███████/%2F%20This%20website%20is%20vulnerable%20to%20NULL%20BYTE%20INJECTION%00

#Mitigation: https://www.securityfocus.com/bid/24791/solution

#See Also: https://www.exploit-db.com/exploits/30281

#Proof of Concept: Screenshots attached.

## Impact

An attacker can exploit these issues to access sensitive information that may aid in further attacks; other attacks are also possible.

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
