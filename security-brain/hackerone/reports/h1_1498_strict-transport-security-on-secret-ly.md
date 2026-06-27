---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1498'
original_report_id: '1498'
title: Strict Transport Security on secret.ly
team_handle: secret
created_at: '2014-02-15T12:36:59.037Z'
disclosed_at: '2014-04-22T10:36:34.966Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
---

# Strict Transport Security on secret.ly

## Metadata

- HackerOne Report ID: 1498
- Weakness: 
- Program: secret
- Disclosed At: 2014-04-22T10:36:34.966Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Bug: Strict Transport Security.
Description: The application was not sending the Strict-Transport-Security header.

This header is used to force browsers to connect to the application trough a SSL connection.

Impact:
If the connections to the web application are not encrypted, an eavesdropper may be able to wiretap them and obtain any confidential information that is sent between the browser and the server.

References:
url: https://www.secret.ly/

Solution:
The web server should send the Strict Transport Security header along with every response.

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
