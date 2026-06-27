---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '779442'
original_report_id: '779442'
title: Subdomain takeover of storybook.lystit.com
weakness: Privilege Escalation
team_handle: lyst
created_at: '2020-01-21T16:51:00.002Z'
disclosed_at: '2020-01-22T14:38:48.812Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 157
asset_identifier: '*.lyst.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Subdomain takeover of storybook.lystit.com

## Metadata

- HackerOne Report ID: 779442
- Weakness: Privilege Escalation
- Program: lyst
- Disclosed At: 2020-01-22T14:38:48.812Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# Summary:
The subdomain storybook.lystit.com had an CNAME record pointing to an unclaimed S3 bucket. This is a high severity security issue because an attacker can register the bucket on AWS and therefore can serve her own content on the subdomain. This allows for various attacks.

# Description:
The dangling CNAME record of storybook.lystit.com is pointing to ███████ and the bucket which could not be found was: "storybook.lystit.com". I was able to register a S3 bucket with this name in AWS. After enabling static website hosting I was able to takeover the subdomain and serve arbitrary content. I am serving a POC to proof I am controlling the subdomain as well as a simple XSS POC.

# POC
POC: view-source:http://storybook.lystit.com/
Stored XSS: http://storybook.lystit.com/asdjklkas1312das879123.html
{F691531}
{F691530}

# Supporting Material/References:
https://www.hackerone.com/blog/Guide-Subdomain-Takeovers

# Recommendations for fix
Remove the dangling CNAME record from storybook.lystit.com

## Impact

The domain takeover allows various attacks. As the full domain is attacker controlled it can be used to serve XSS attacks, phishing campaigns and might be used to bypass the Same Origin Policy on other lystit.com domains and services.

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
