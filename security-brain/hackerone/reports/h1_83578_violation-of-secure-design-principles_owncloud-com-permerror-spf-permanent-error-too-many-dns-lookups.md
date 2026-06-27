---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '83578'
original_report_id: '83578'
title: 'owncloud.com: PermError SPF Permanent Error: Too many DNS lookups'
weakness: Violation of Secure Design Principles
team_handle: owncloud
created_at: '2015-08-20T04:18:20.397Z'
disclosed_at: '2015-10-11T07:06:31.068Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# owncloud.com: PermError SPF Permanent Error: Too many DNS lookups

## Metadata

- HackerOne Report ID: 83578
- Weakness: Violation of Secure Design Principles
- Program: owncloud
- Disclosed At: 2015-10-11T07:06:31.068Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I just checked for SPF records for the owncloud.com domain, and there are none, effectively allowing for spam(spoof) to originate from that domain. you can validate by testing yourself here: http://www.kitterman.com/spf/validate.html

SPF record lookup and validation for: owncloud.com

SPF records are published in DNS as TXT records.

The TXT records found for your domain are:
v=spf1 a:mx.owncloud.com a:kerio.owncloud.com a:schaltsekun.de a:m.hive01.com include:cmail1.com include:email.influitive.com include:google.com ~all 

Checking to see if there is a valid SPF record. 

Found v=spf1 record for owncloud.com: 
v=spf1 a:mx.owncloud.com a:kerio.owncloud.com a:schaltsekun.de a:m.hive01.com include:cmail1.com include:email.influitive.com include:google.com ~all 

evaluating...
Results - PermError SPF Permanent Error: Too many DNS lookups

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
