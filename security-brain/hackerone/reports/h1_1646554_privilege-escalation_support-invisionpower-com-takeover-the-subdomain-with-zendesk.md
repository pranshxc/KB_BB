---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1646554'
original_report_id: '1646554'
title: support.invisionpower.com takeover the subdomain with Zendesk
weakness: Privilege Escalation
team_handle: ips
created_at: '2022-07-22T13:00:17.049Z'
disclosed_at: '2022-08-24T13:10:11.028Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- privilege-escalation
---

# support.invisionpower.com takeover the subdomain with Zendesk

## Metadata

- HackerOne Report ID: 1646554
- Weakness: Privilege Escalation
- Program: ips
- Disclosed At: 2022-08-24T13:10:11.028Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The subdomain at https://support.invisionpower.com has an unclaimed CNAME record ( ipscommunity.zendesk.com ). I checked the username availability in the signup process at Zendesk, it was observed that the subdomain is vulnerable to a subdomain takeover which allows an attacker could exploit such a situation by registering the expired sub domain and setting up a phishing page that mimics the company’s main support website.

## Impact

Subdomain takeover can be abused to do several things like :
Malware distribution
Phishing / Spear phishing
XSS
Authentication bypass
Legitimate mail sending and receiving on behalf of the ford subdomain
...
The list goes on and on.

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
