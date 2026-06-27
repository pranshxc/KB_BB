---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1715538'
original_report_id: '1715538'
title: Subdomain Takeover on  delivey.yelp.com
weakness: Phishing
team_handle: yelp
created_at: '2022-09-28T14:45:13.273Z'
disclosed_at: '2022-11-12T15:49:34.354Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
asset_identifier: '*.yelp.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- phishing
---

# Subdomain Takeover on  delivey.yelp.com

## Metadata

- HackerOne Report ID: 1715538
- Weakness: Phishing
- Program: yelp
- Disclosed At: 2022-11-12T15:49:34.354Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

## Summary:
[Subdomain takeover vulnerabilities occur when a subdomain (delivery.yelp.com) is pointing to a service]
Vulnerable url : delivery.yelp.com
This is an [verify Link](http://delivery.yelp.com.s3-website-us-east-1.amazonaws.com/).
{F1959331}

## Platform(s) Affected:
[website  ]


## Steps To Reproduce

  1. [Create the Amazon S3 Bucket on this Name : delivery.yelp.com]
{F1959320}
  1. [then Upload the Attacker HTML web page]
  1. [then using Static Web hosting ]

## Supporting Material/References:
{F1959332}

Remediation
Remove the cname entry or claim the subdomain delivey.yelp.com on amazon aws

## Impact

Risk
fake website
malicious code injection
users tricking
company impersonation
This issue can have really huge impact on the companies reputation someone could post malicious content on the compromised site and then your users will think it's official but it's not.

Best Regards, 
Racer Saravanaa 05

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
