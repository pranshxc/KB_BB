---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1168198'
original_report_id: '1168198'
title: Versa Director is susceptible to Command Injection attacks (e.g., SQL, LDAP,
  XML, Xpath)
weakness: Command Injection - Generic
team_handle: versa-networks
created_at: '2019-04-02T00:00:00.000Z'
disclosed_at: '2021-05-05T20:21:55.596Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- command-injection-generic
---

# Versa Director is susceptible to Command Injection attacks (e.g., SQL, LDAP, XML, Xpath)

## Metadata

- HackerOne Report ID: 1168198
- Weakness: Command Injection - Generic
- Program: versa-networks
- Disclosed At: 2021-05-05T20:21:55.596Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

In Versa Director, the command injection is an attack in which the goal is execution of arbitrary commands on the host operating system via a vulnerable application. Command injection attacks are possible when an application passes unsafe user supplied data (forms, cookies, HTTP headers etc.) to a system shell. In this attack, the attacker-supplied operating system commands are usually executed with the privileges of the vulnerable application. Command injection attacks are possible largely due to insufficient input validation.

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
