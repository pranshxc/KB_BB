---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2293731'
original_report_id: '2293731'
title: Command Injection using malicious hostname in expanded proxycommand
weakness: Code Injection
team_handle: ibb
created_at: '2023-12-20T22:05:47.401Z'
disclosed_at: '2024-02-28T16:28:01.972Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 34
asset_identifier: https://git.libssh.org/
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- code-injection
---

# Command Injection using malicious hostname in expanded proxycommand

## Metadata

- HackerOne Report ID: 2293731
- Weakness: Code Injection
- Program: ibb
- Disclosed At: 2024-02-28T16:28:01.972Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Using the ProxyCommand or the ProxyJump feature enables users to exploit
unchecked hostname syntax on the client, which enables to inject malicious code
into the command of the above-mentioned features through the hostname parameter.

User interaction is required to exploit this issue.

Advisory from libssh: https://www.libssh.org/security/advisories/CVE-2023-6004.txt

Advisory from OpenSSH which also suffered from this flaw: https://www.openssh.com/txt/release-9.6

## Impact

Code execution via malicious input hostname or other tokens

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
