---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '119220'
original_report_id: '119220'
title: Sub-Domain Takeover
team_handle: x
created_at: '2016-02-28T03:52:37.286Z'
disclosed_at: '2016-03-18T17:41:16.619Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
---

# Sub-Domain Takeover

## Metadata

- HackerOne Report ID: 119220
- Weakness: 
- Program: x
- Disclosed At: 2016-03-18T17:41:16.619Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey !

Your subdomain web.mopub.com is pointing to DYN but you have not claimed it on DYN end.

So what happens here is actually that, since web.mopub.com is pointing to DYN, DYNis actually checking if there's a host with that name. Which in this case was not true. So I was able to claim the domain for my own host, and thus, can place content on this URL.

You should immediately remove the DNS-entry for web.mopub.com pointing to DYN

The issue is bit on same concept of #32825

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
