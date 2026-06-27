---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '759454'
original_report_id: '759454'
title: Helpdesk Takeover at dmc.datastax.com
weakness: Reliance on Untrusted Inputs in a Security Decision
team_handle: datastax
created_at: '2019-12-16T15:26:15.365Z'
disclosed_at: '2020-01-15T17:49:43.120Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 189
asset_identifier: www.datastax.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- reliance-on-untrusted-inputs-in-a-security-decision
---

# Helpdesk Takeover at dmc.datastax.com

## Metadata

- HackerOne Report ID: 759454
- Weakness: Reliance on Untrusted Inputs in a Security Decision
- Program: datastax
- Disclosed At: 2020-01-15T17:49:43.120Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
DNS record [dmc.datastax.com](dmc.datastax.com) is pointing to stale [dmc-support.zendesk.com](dmc-support.zendesk.com) domain on Zendesk which is available for takeover.

DNS Stale Records: {F661014}


## Proof of Concept:
There was no helpdesk configured at this address, which means that the address was available and anyone could claim it. I was able to claim dmc-support.zendesk.com.

On this page, https://dmc.datastax.com/hc/en-us I haven't made the page public, I'm attaching a screenshot of the webpage:
{F661004} 

## Supporting Material/References:
Login page:
{F661021}

## Impact

Subdomain takeover

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
