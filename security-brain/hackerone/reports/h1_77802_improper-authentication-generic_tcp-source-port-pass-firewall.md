---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '77802'
original_report_id: '77802'
title: TCP Source Port Pass Firewall
weakness: Improper Authentication - Generic
team_handle: shopify
created_at: '2015-07-22T14:55:39.324Z'
disclosed_at: '2015-08-11T15:10:49.339Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- improper-authentication-generic
---

# TCP Source Port Pass Firewall

## Metadata

- HackerOne Report ID: 77802
- Weakness: Improper Authentication - Generic
- Program: shopify
- Disclosed At: 2015-08-11T15:10:49.339Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Affects: *yourshop.myshopify.com

Your firewall policy seems to let TCP packets with a specific source port pass through. Some types of requests can pass through the firewall. The port number 80 is the source port that unauthorized users can use to bypass your firewall.

Suggestion to fix: Make sure that all your filtering rules are correct and strict enough. If the firewall intends to deny TCP connections to a specific port, it should be configured to block all TCP SYN packets going to this port, regardless of the source port. 

I tested on test.myshopify.com and it responded 4 times to 4 TCP SYN probes sent to port 20 using source port 80. However, it did not respond at all to 4 TCP SYN probes sent to the same destination port using a random source port.

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
