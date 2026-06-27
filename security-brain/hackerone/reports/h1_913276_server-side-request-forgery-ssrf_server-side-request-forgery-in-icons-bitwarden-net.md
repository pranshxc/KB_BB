---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '913276'
original_report_id: '913276'
title: Server-Side Request Forgery in "icons.bitwarden.net"
weakness: Server-Side Request Forgery (SSRF)
team_handle: bitwarden
created_at: '2020-07-01T17:22:01.865Z'
disclosed_at: '2020-08-07T14:39:01.676Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
asset_identifier: bitwarden.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# Server-Side Request Forgery in "icons.bitwarden.net"

## Metadata

- HackerOne Report ID: 913276
- Weakness: Server-Side Request Forgery (SSRF)
- Program: bitwarden
- Disclosed At: 2020-08-07T14:39:01.676Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

As, I already checked with support team via portal, due to domain confirmation I checked with them. Here, adding the required information: 

##Title: Server-Side Request Forgery in "icons.bitwarden.net".
##URL: https://icons.bitwarden.net/spoofed.burpcollaborator.net/icon.png
##Parameter: REST based in "https://icons.bitwarden.net/{DOMAIN-HERE}/icon.png"
##Summary: The application failed to validate the vulnerable URL which led to internal port scanning through SSRF vulnerability. 
##Severity: High

##Proof of Concept: 
1. The application shows "https://icons.bitwarden.net/localhost/icon.png". - 400 Bad Request.
2. The application shows https://icons.bitwarden.net/spoofed.burpcollaborator.net/icon.png - 404 Not Found.
Note: Furthermore, an attacker would be able to perform host discovery and internal port scanning which I did not perform as the scope was not mentioned in the list so better that you can proceed with the above Proof of Concept steps. 

##Recommendation:
In the above steps, localhost was restricted but was able to bypass using domain "spoofed.burpcollaborator.net" which resolves "127.0.0.1". The application should resolve the domain and restrict access to internal resources.

## Impact

* An attacker would be able to perform SSRF attack to retrieve internal infrastructure information.

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
