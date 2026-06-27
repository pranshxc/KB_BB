---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1055823'
original_report_id: '1055823'
title: SSRF By adding a custom integration on console.helium.com
weakness: Server-Side Request Forgery (SSRF)
team_handle: helium
created_at: '2020-12-10T14:38:28.109Z'
disclosed_at: '2021-05-26T19:26:24.778Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 48
asset_identifier: https://helium-console-dev.herokuapp.com/
asset_type: URL
max_severity: high
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# SSRF By adding a custom integration on console.helium.com

## Metadata

- HackerOne Report ID: 1055823
- Weakness: Server-Side Request Forgery (SSRF)
- Program: helium
- Disclosed At: 2021-05-26T19:26:24.778Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

A Server Side Request Forgery vulnerability was found in the *Add a custom Integration* feature on *console.helium.com*. By creating a custom HTTP integration, and setting the integration endpoint to http://169.254.169.254/latest/meta-data private meta-data from the AWS EC2 instance running can be retrieved.

{F1111768}

{F1111767}

The server makes the HTTP request and sets the response body  as the integration message every time that the device sends a packet. As the endpoint input is not validated, this makes the application vulnerable to a critical SSRF.

{F1111779}

{F1111780}

Endpoint set as: http://169.254.169.254/latest/meta-data/ami-id

{F1111781}

## Impact

By exploiting this vulnerability an attacker can get access to the server internal network and access private and critical information.

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
