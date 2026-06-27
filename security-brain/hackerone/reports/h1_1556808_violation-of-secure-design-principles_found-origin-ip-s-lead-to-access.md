---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1556808'
original_report_id: '1556808'
title: Found Origin IP's Lead To Access ████
weakness: Violation of Secure Design Principles
team_handle: deptofdefense
created_at: '2022-05-02T20:03:07.415Z'
disclosed_at: '2022-10-14T14:28:10.096Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# Found Origin IP's Lead To Access ████

## Metadata

- HackerOne Report ID: 1556808
- Weakness: Violation of Secure Design Principles
- Program: deptofdefense
- Disclosed At: 2022-10-14T14:28:10.096Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Discovered that the ██████ site exposed its Non-Cloudflare IP which could allow bypassing of anti-DDoS mechanisms.
Your origin servers are not blocking access from non-Cloudflare servers.This way crawlers can find your origin servers' IPs by checking random IPs until they found your origin server(s).
What makes this especially easy are tools like shodan.io(which can find your origin servers).

## Impact

This attack vector can be extremely bad because with the IP found out an attacker could attack the servers by DDoS or other attacks without being stopped by CloudFlare.

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Visit these link:
https://www.shodan.io/search?query=hostname%3A████+200

IP:
-███

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
