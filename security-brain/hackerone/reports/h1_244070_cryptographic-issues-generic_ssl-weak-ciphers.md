---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '244070'
original_report_id: '244070'
title: SSl Weak Ciphers
weakness: Cryptographic Issues - Generic
team_handle: gratipay
created_at: '2017-06-28T17:23:04.200Z'
disclosed_at: '2017-07-10T09:58:33.536Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 0
tags:
- hackerone
- cryptographic-issues-generic
---

# SSl Weak Ciphers

## Metadata

- HackerOne Report ID: 244070
- Weakness: Cryptographic Issues - Generic
- Program: gratipay
- Disclosed At: 2017-07-10T09:58:33.536Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

# Summary
Websites using TLS 1.0 will be considered non-compliant by PCI after 30 June 2018.

# Description
TLS 1.0 has several flaws. An attacker can cause connection failures and they can trigger the use of TLS 1.0 to exploit vulnerabilities like BEAST (Browser Exploit Against SSL/TLS).

# Steps To Reproduce

-Nginx, locate any use of the directive ssl_protocols in the nginx.conf file and remove TLSv1.

ssl_protocols TLSv1.1 TLSv1.2;
  
-Configure your web server to disallow using weak ciphers. You need to restart the web server to enable changes.

# Supporting Material/References:
https://blog.pcisecuritystandards.org/migrating-from-ssl-and-early-tls

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
