---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '673273'
original_report_id: '673273'
title: subdomain take over at recommendation.algolia.com
weakness: Violation of Secure Design Principles
team_handle: algolia
created_at: '2019-08-14T09:14:02.191Z'
disclosed_at: '2019-08-14T13:53:03.340Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 24
tags:
- hackerone
- violation-of-secure-design-principles
---

# subdomain take over at recommendation.algolia.com

## Metadata

- HackerOne Report ID: 673273
- Weakness: Violation of Secure Design Principles
- Program: algolia
- Disclosed At: 2019-08-14T13:53:03.340Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Description
hello sir,
your subdomain recommendation.algolia.com cname is recommendation.us and recommendation.us is for sell which can lead to subdomain take over
##steps to reproduce
1. check the cname of recommendation.algolia.com
2. see that the cname "recommendation.us" is for sell using lookup tool

##poc:
{F555251}

## Impact

Attackers are able to purchase recommendation.us then they will be able to takeover recommendation.algolia.com and post porn pictures or phishing forums

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
