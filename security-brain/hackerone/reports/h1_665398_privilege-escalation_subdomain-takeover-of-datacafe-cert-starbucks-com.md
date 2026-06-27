---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '665398'
original_report_id: '665398'
title: Subdomain takeover of datacafe-cert.starbucks.com
weakness: Privilege Escalation
team_handle: starbucks
created_at: '2019-08-01T10:49:53.145Z'
disclosed_at: '2019-08-28T16:43:06.664Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 303
asset_identifier: Other non domain specific items
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Subdomain takeover of datacafe-cert.starbucks.com

## Metadata

- HackerOne Report ID: 665398
- Weakness: Privilege Escalation
- Program: starbucks
- Disclosed At: 2019-08-28T16:43:06.664Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
The subdomain datacafe-cert.starbucks.com had an CNAME record pointing to an unclaimed Azure webservice. This is a high severity security issue because an attacker can register the subdomain on Azure and therefore can own the subdomain datacafe-cert.starbucks.com.

**Description:**
The dangling CNAME record of datacafe-cert.starbucks.com is pointing to s00397nasv101-datacafe-cert.azurewebsites.net which was not claimed by you. I registered a service with this name and therefore was able to takeover the subdomain. Every attacker doing this has afterwords full control over the contents served on this subdomain.

**Platform(s) Affected:** 
http://datacafe-cert.starbucks.com/
https://datacafe-cert.starbucks.com/

## Supporting Material/References:
view-source:http://datacafe-cert.starbucks.com/

## How can the system be exploited with this bug?
The full domain can be taken over. Arbitrary content can be served under it.

## How did you come across this bug ?
I noticed the dangling CNAME record of datacafe-cert.starbucks.com.

## Recommendations for fix
1) Remove the dangling CNAME record from datacafe-cert.starbucks.com
2) I release s00397nasv101-datacafe-cert.azurewebsites.net
3) You can reclaim it if you want

## Impact

This issue can be exploited in several ways, for example but not limited to: XSS, Phishing, Session Hijacking due to bypassing of SOP

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
