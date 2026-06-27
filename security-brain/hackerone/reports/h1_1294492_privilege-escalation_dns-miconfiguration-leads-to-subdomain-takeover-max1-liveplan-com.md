---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1294492'
original_report_id: '1294492'
title: DNS Miconfiguration Leads to Subdomain Takeover  - max1.liveplan.com
weakness: Privilege Escalation
team_handle: palo_alto_software
created_at: '2021-08-07T11:45:21.778Z'
disclosed_at: '2021-09-08T16:45:30.915Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- privilege-escalation
---

# DNS Miconfiguration Leads to Subdomain Takeover  - max1.liveplan.com

## Metadata

- HackerOne Report ID: 1294492
- Weakness: Privilege Escalation
- Program: palo_alto_software
- Disclosed At: 2021-09-08T16:45:30.915Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary
The issue happens due to using EC2 public DNS instead of using Elastic IPs as `CNAME` record. This report is simliar to report #1069795
 
## Misconfiguration

- DNS Records

```json
{
  "host": "max1.liveplan.com",
  "resolver": [
    "1.0.0.1:53"
  ],
  "a": [
    "54.68.121.128"
  ],
  "cname": [
    "ec2-54-68-121-128.us-west-2.compute.amazonaws.com"
  ],
  "status_code": "NOERROR",
  "timestamp": "2021-08-07T13:41:48.3522806+02:00"     
}
```

- If the EC2 instance is killed or terminated and the DNS was not updated this will lead to creating a dangling DNS record for the subdomain.
- The EC2 IP will be released to AWS IPs pool, This mean it's possible to assign the IP to new EC2 instance.

## PoC

- SSL Certificate Data pulled from `https://max1.liveplan.com` on date `7/8/2021 - 1:40PM`.
- Data was pulled using [SSLEnum](https://github.com/melbadry9/SSLEnum)

```json
{
  "name": "max1.liveplan.com",
  "org": [],
  "cn": [
    "*.test.tugo.com"
  ],
  "alt_doms": [
    "*.test.tugo.com",        
    "*.dev.tugo.com",
    "*.uat.tugo.com"
  ],
  "dangling": true
}
```

- This does prove that `max1.liveplan.com` is currently taken over by  someone.

{F1403387}
 
## Fix
- Use Elastic IPs instead of the public DNS of EC2 instance or clear DNS records for mentioned subdomain

## Supporting Material/References:
- https://blog.melbadry9.xyz/dangling-dns/aws/ddns-ec2-current-state

## Impact

- This could allow the takeover of the EC2 instance IP that will lead to subdomain takeover.

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
