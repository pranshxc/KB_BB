---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1105673'
original_report_id: '1105673'
title: Origin IP found, Cloudflare bypassed
weakness: Violation of Secure Design Principles
team_handle: cs_money
created_at: '2021-02-17T15:36:35.514Z'
disclosed_at: '2021-03-30T10:51:42.976Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 8
asset_identifier: 3d.cs.money
asset_type: URL
max_severity: medium
tags:
- hackerone
- violation-of-secure-design-principles
---

# Origin IP found, Cloudflare bypassed

## Metadata

- HackerOne Report ID: 1105673
- Weakness: Violation of Secure Design Principles
- Program: cs_money
- Disclosed At: 2021-03-30T10:51:42.976Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Greetings!, Hope Y'all good and fine.

## Summary:
I would like to report another vulnerability very Similar to my other report in #975991


Due to lack of secure design, I was able to find the origin IPs behind Cloludflare WAF.

The IPs I found belong to :

3d.cs.money

## Description:

I was able to find and access the Origin IPs behind the WAF due to lack of access control,
I could also port scan the IP 

The IP found :
51.83.253.82

## Steps To Reproduce:
simply visit:

https://51.83.253.82/

## Impact

As reported in many other submissions, Cloudflare bypasses can have a significant impact, as any adversary is now able to communicate with the origin server directly, enabling them to perform unfiltered attacks (such as denial-of-service), and data retrieval.

This attack vector can be extremely bad because with the IP found out an attacker could attack the servers by DDoS or other attacks without being stopped by CloudFlare.]

Thanks!

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
