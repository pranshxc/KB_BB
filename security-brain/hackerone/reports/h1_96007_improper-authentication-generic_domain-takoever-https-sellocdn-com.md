---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '96007'
original_report_id: '96007'
title: Domain takoever - https://sellocdn.com
weakness: Improper Authentication - Generic
team_handle: shopify
created_at: '2015-10-27T06:02:48.273Z'
disclosed_at: '2015-11-03T08:16:23.251Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# Domain takoever - https://sellocdn.com

## Metadata

- HackerOne Report ID: 96007
- Weakness: Improper Authentication - Generic
- Program: shopify
- Disclosed At: 2015-11-03T08:16:23.251Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

While performing some DNS recon activities, I identified the following domain sellocdn.com, owned and operated by Shopify (see whois below). The DNS record is pointing to Heroku, but it hasn't be claimed on Heroku. This would allow a malicious user  to login to Heroku and claim the domain, and host malicious content of their choosing on http://sellocdn.com.

i understand that this is out of scope, but I thought I would point it out since I found it.

Registry Registrant ID:
Registrant Name: Shopify Hostmaster
Registrant Organization: Shopify Inc.
Registrant Street: 126 York St.  200
Registrant City: Ottawa
Registrant State/Province: ON
Registrant Postal Code: K1N 5T5
Registrant Country: CA
Registrant Phone: +1.(613) 241-2828
Registrant Phone Ext:
Registrant Fax:
Registrant Fax Ext:
Registrant Email: domains@shopify.com

PoC - navigate to http://sellocdn.com

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
