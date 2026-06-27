---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1390093'
original_report_id: '1390093'
title: Subdomain Takeover - pmp.oneweb.net
weakness: Privilege Escalation
team_handle: oneweb
created_at: '2021-11-02T20:40:32.131Z'
disclosed_at: '2021-11-04T09:10:41.711Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
asset_identifier: '*.oneweb.net'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Subdomain Takeover - pmp.oneweb.net

## Metadata

- HackerOne Report ID: 1390093
- Weakness: Privilege Escalation
- Program: oneweb
- Disclosed At: 2021-11-04T09:10:41.711Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary
The issue happens due to using EC2 public DNS instead of using Elastic IPs as `CNAME` or `A` record. If the EC2 instance is killed or terminated and the DNS not updated this will lead to creating a dangling DNS record for the subdomain. The EC2 IP will be released to AWS IPs pool, This mean it's possible to assign the IP to new EC2 instance.

## PoC
- Visit `http://pmp.oneweb.net/melbadry9.html`
- Web Archive "https://web.archive.org/web/20211102203640/http://pmp.oneweb.net/melbadry9.html"

{F1501722}

## Fix
- Clear DNS records for mentioned subdomain

## Supporting Material/References:
- https://blog.melbadry9.xyz/dangling-dns/aws/ddns-ec2-current-state

## Impact

- High severity subdomain takeover as I have full control on Elastic IP and EC2 instance

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
