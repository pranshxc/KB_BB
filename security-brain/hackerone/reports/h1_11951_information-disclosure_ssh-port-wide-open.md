---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '11951'
original_report_id: '11951'
title: SSH Port Wide Open
weakness: Information Disclosure
team_handle: joola-io
created_at: '2014-05-13T19:48:08.983Z'
disclosed_at: '2014-07-08T10:00:34.475Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# SSH Port Wide Open

## Metadata

- HackerOne Report ID: 11951
- Weakness: Information Disclosure
- Program: joola-io
- Disclosed At: 2014-07-08T10:00:34.475Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

SSH port is wide open, this can give attackers additional information to coordinate an attack:

Nmap scan report for joola.io (178.79.174.108)
Host is up (0.033s latency).
rDNS record for 178.79.174.108: li311-108.members.linode.com
Not shown: 994 closed ports
PORT    STATE    SERVICE
20/tcp  filtered ftp-data
22/tcp  open     ssh
53/tcp  filtered domain
80/tcp  open     http
119/tcp filtered nntp
443/tcp open     https

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
