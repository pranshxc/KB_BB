---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '295330'
original_report_id: '295330'
title: code.wordpress.net subdomain Takeover
team_handle: wordpress
created_at: '2017-12-05T10:44:48.749Z'
disclosed_at: '2018-03-11T20:53:27.428Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
asset_identifier: '*.wordpress.net'
asset_type: WILDCARD
max_severity: low
tags:
- hackerone
---

# code.wordpress.net subdomain Takeover

## Metadata

- HackerOne Report ID: 295330
- Weakness: 
- Program: wordpress
- Disclosed At: 2018-03-11T20:53:27.428Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hy Wordpress sec i found as it is posible to takeover this domain http://code.wordpress.net when you navigate it you will get this error msg:

Warning! Domain mapping upgrade for this domain not found. Please log in and go to the Domains Upgrades page of your blog to use this domain. 

$ host code.wordpress.net
code.wordpress.net is an alias for wpprojects.wordpress.com.
wpprojects.wordpress.com is an alias for lb.wordpress.com.
lb.wordpress.com has address 192.0.78.13
lb.wordpress.com has address 192.0.78.12

## Impact

The attacker can takeover this subdomain

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
