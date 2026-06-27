---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '746000'
original_report_id: '746000'
title: Route53 Subdomain Takeover on test-cncf-aws.canary.k8s.io
weakness: Misconfiguration
team_handle: kubernetes
created_at: '2020-02-12T10:38:37.420Z'
disclosed_at: '2021-01-16T06:07:13.398Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 11
asset_identifier: k8s.io
asset_type: URL
max_severity: critical
tags:
- hackerone
- misconfiguration
---

# Route53 Subdomain Takeover on test-cncf-aws.canary.k8s.io

## Metadata

- HackerOne Report ID: 746000
- Weakness: Misconfiguration
- Program: kubernetes
- Disclosed At: 2021-01-16T06:07:13.398Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

## Summary:
I discovered that it was possible to takeover ` test-cncf-aws.canary.k8s.io` by assigning a zone to that name with one of the following nameservers in Route53:
```
test-cncf-aws.canary.k8s.io. 3600 IN    NS      ns-265.awsdns-33.com.
test-cncf-aws.canary.k8s.io. 3600 IN    NS      ns-687.awsdns-21.net.
test-cncf-aws.canary.k8s.io. 3600 IN    NS      ns-1458.awsdns-54.org.
test-cncf-aws.canary.k8s.io. 3600 IN    NS      ns-1825.awsdns-36.co.uk.
```
Once the zone was claimed, I was able to create DNS records under this host. Consider the following record:
```
poc.test-cncf-aws.canary.k8s.io
```

##Steps To Reproduce:
1. See above domain

##Remediation Instructions
Remove the NS record delegation NS privs on a subdomain before you delete the zone

## Impact

With this vulnerability, an attacker can host arbitrary content under your domain. This can allow an attacker to host brand-damaging materials, steal sensitive * scoped session cookies, and even escalate other vulnerabilities.

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
