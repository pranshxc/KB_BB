---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '128685'
original_report_id: '128685'
title: SSRF on testing endpoint
weakness: Privilege Escalation
team_handle: apitest
created_at: '2016-04-06T10:39:49.602Z'
disclosed_at: '2016-09-14T20:32:06.836Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- privilege-escalation
---

# SSRF on testing endpoint

## Metadata

- HackerOne Report ID: 128685
- Weakness: Privilege Escalation
- Program: apitest
- Disclosed At: 2016-09-14T20:32:06.836Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

# Synopsis

The form at https://www.apitest.io/request accepts (among others) the "url" parameter. This feature allows to reach internal services (like the OpenStack metadata server) or services running on loopback.

# Identified services

http://0x7f.1/ (nginx) => "If you see this page, the nginx web server is successfully installed and
working. Further configuration is required."

http://169.254.169.254/meta-data (OpenStack metada) => directoty listing (instance-id, mac, local-ipv4, public-ipv4, network_config/content_path, SUBID, ipv6-addr, ipv6-prefix)

http://0x7f.1:8081/ (vestacp admin panel) => <a href="http://vestacp.com/">Powered by VESTA</a>

# Impacts

The metadata server does't seem to host any sensitive data. However, access to port 8081 may allow to reconfigure the OS or services (untested). Additional services may exist, but it seems that my IP address (81.56.184.117) was just blacklisted on your side.

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
