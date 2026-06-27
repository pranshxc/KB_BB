---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '163812'
original_report_id: '163812'
title: Insecure Transportation Security Protocol Supported (TLS 1.0)
weakness: Violation of Secure Design Principles
team_handle: gratipay
created_at: '2016-08-27T13:33:55.447Z'
disclosed_at: '2017-07-10T09:58:26.373Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# Insecure Transportation Security Protocol Supported (TLS 1.0)

## Metadata

- HackerOne Report ID: 163812
- Weakness: Violation of Secure Design Principles
- Program: gratipay
- Disclosed At: 2017-07-10T09:58:26.373Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Description: Its observed that that insecure transportation security protocol (TLS 1.0) is supported by your web server. TLS 1.0 has several flaws. An attacker can cause connection failures and they can trigger the use of TLS 1.0 to exploit vulnerabilities like BEAST.
Websites using TLS 1.0 will be considered non-compliant by PCI after 30 June 2018.

Impact: Attackers can perform man-in-the-middle attacks and observe the encryption traffic between your website and its visitors.

Recommended Fix: Configure your web server to disallow using weak ciphers. You need to restart the web server to enable changes.

By fingerprinting server, found that its Nginx Web server. So below is solution for Nginx
For Nginx, locate any use of the directive ssl_protocols in the nginx.conf file and remove TLSv1.
ssl_protocols TLSv1.1 TLSv1.2;

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
