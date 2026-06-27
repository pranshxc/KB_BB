---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '44052'
original_report_id: '44052'
title: Hadoop Node available to public
weakness: Information Disclosure
team_handle: mailru
created_at: '2015-01-16T15:30:28.845Z'
disclosed_at: '2015-09-13T12:17:30.116Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- information-disclosure
---

# Hadoop Node available to public

## Metadata

- HackerOne Report ID: 44052
- Weakness: Information Disclosure
- Program: mailru
- Disclosed At: 2015-09-13T12:17:30.116Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Собственно, вот они:

185.5.139.34-37

http://185.5.139.35:50075/logs/hadoop-hadoop-datanode-tank15.log
http://185.5.139.37:50075/logs/userlogs/application_1404372048187_0617/container_1404372048187_0617_01_000015/syslog

Ну и в том же духе. Там наружу __все__ логи.

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
