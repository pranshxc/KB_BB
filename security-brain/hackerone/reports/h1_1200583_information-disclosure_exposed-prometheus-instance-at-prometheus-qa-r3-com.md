---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1200583'
original_report_id: '1200583'
title: Exposed Prometheus instance at prometheus.qa.r3.com
weakness: Information Disclosure
team_handle: r3
created_at: '2021-05-18T05:32:37.304Z'
disclosed_at: '2021-07-12T08:40:26.437Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
asset_identifier: R3 - everything in scope
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Exposed Prometheus instance at prometheus.qa.r3.com

## Metadata

- HackerOne Report ID: 1200583
- Weakness: Information Disclosure
- Program: r3
- Disclosed At: 2021-07-12T08:40:26.437Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary
Hi there, just wanted to note that all of your assets are listed as out of scope on HackerOne right now, which is a bit confusing. Nevertheless, I noticed that your Prometheus server at prometheus.qa.r3.com is exposed to the internet, which appears to let you view all of the internal metrics of all of your QA systems. This seems to be connected to your Kubernetes API server, so it seems pretty concerning.

I don't think this is incredibly concerning, as after all Prometheus is just metrics. But I don't think they are intended to be publicly exposed. :)

{F1305158}
{F1305159}

## Steps To Reproduce:
Visit https://prometheus.qa.r3.com/.

## Impact

Disclosure of normally private metrics

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
