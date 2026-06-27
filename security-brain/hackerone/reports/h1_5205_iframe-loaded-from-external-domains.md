---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '5205'
original_report_id: '5205'
title: IFRAME loaded from External Domains
team_handle: coinbase
created_at: '2014-03-30T03:36:34.354Z'
disclosed_at: '2014-04-30T00:48:49.991Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
---

# IFRAME loaded from External Domains

## Metadata

- HackerOne Report ID: 5205
- Weakness: 
- Program: coinbase
- Disclosed At: 2014-04-30T00:48:49.991Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello coinbase,

Iam saikiran.Iam a security researcher.while i was going through your site i found that your website loads an iframe from an external website which might not be trustworthy.IFRAME has been loaded in the page 'https://coinbase.com/charts' from 'www.statsmix.com' which is an external domain that might not be trustworthy.

As this is a bit-coin wallet website it is not advisable to load iframes or any type of data from other websites...it would be very dangerous if the external domain misuses this..if he changes that i frame into any exploitation method he can get into your website easily.

SOLUTION.

just stop using external domain data in your webserver..what ever you use,use your own data or just try to keep that data on your server only..

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
