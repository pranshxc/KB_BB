---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '150078'
original_report_id: '150078'
title: SSL certificate public key less than 2048 bit
weakness: Cryptographic Issues - Generic
team_handle: iandunn-projects
created_at: '2016-07-08T19:35:31.552Z'
disclosed_at: '2016-08-18T01:18:31.094Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 4
tags:
- hackerone
- cryptographic-issues-generic
---

# SSL certificate public key less than 2048 bit

## Metadata

- HackerOne Report ID: 150078
- Weakness: Cryptographic Issues - Generic
- Program: iandunn-projects
- Disclosed At: 2016-08-18T01:18:31.094Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

One of the SSL certificates used by your SSL server (On your personal website: https://iandunn.name/ ) contains a public key less than 2048 bit long. 

New Standard for SSL Certificates Industry standards set by the Certification Authority/Browser (CA/B) Forum require that certificates issued after January 1, 2014 MUST be at least 2048-bit key length.1 As computer power increases, anything less than 2048-bit certificates are at risk of being compromised by hackers with sophisticated processing capabilities. The cybersecurity industry is moving to stronger 2048-bit encryption to help preserve internet security.

Any certificate with a public key less than 2048-bit are at risk of being compromised by hackers with sophisticated processing capabilities.

If you have any 1024-bit certificates or certificates with less than 2048-bit key length, you will need to migrate to 2048-bit key length.

http://www.geotrust.com/resources/2048-bit-compliance/

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
