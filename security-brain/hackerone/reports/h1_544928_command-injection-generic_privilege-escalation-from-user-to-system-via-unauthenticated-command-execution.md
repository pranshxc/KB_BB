---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '544928'
original_report_id: '544928'
title: Privilege Escalation From user to SYSTEM via unauthenticated command execution
weakness: Command Injection - Generic
team_handle: ui
created_at: '2019-04-22T00:58:17.010Z'
disclosed_at: '2019-11-08T16:37:35.196Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 541
asset_identifier: UniFi Video Server
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: none
tags:
- hackerone
- command-injection-generic
---

# Privilege Escalation From user to SYSTEM via unauthenticated command execution

## Metadata

- HackerOne Report ID: 544928
- Weakness: Command Injection - Generic
- Program: ui
- Disclosed At: 2019-11-08T16:37:35.196Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The vulnerability, or feature depending how you look at it, is the ability to execute commands using the 
evostream API interface that is exposed on localhost:7440. Since the evostream service is running as SYSTEM a user can use the launchprocess command,  http://docs.evostream.com/2.0/launchProcess.html, to execute any binary with supplied arguments. The only thing that is keeping this "feature" from allowing remote code execution is the fact that it listens on localhost only. However, if it were couple with an SSRF, an attacker could achieve full remote code execution.

## Impact

The ability to run arbitrary commands as SYSTEM from any user.

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
