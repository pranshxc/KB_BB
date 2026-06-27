---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '997281'
original_report_id: '997281'
title: xmlrpc file enabled
weakness: Information Disclosure
team_handle: yelp
created_at: '2022-05-19T09:29:41.332Z'
disclosed_at: '2022-06-16T19:02:47.543Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 4
asset_identifier: restaurants.yelp.com
asset_type: URL
max_severity: low
tags:
- hackerone
- information-disclosure
---

# xmlrpc file enabled

## Metadata

- HackerOne Report ID: 997281
- Weakness: Information Disclosure
- Program: yelp
- Disclosed At: 2022-06-16T19:02:47.543Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

## Summary:

Hello team,
I have found a security vulnerability in ** restaurants.yelp.com/xmlrpc.php** which lets attacker to:
1: XSPA or PortScan
2: Bruteforce
3:DOS and much more
## Platform(s) Affected:
  https://restaurants.yelp.com

## Steps To Reproduce:
1: Go to https://restaurants.yelp.com/xmlrpc.php to check if it is enabled or not. so the server altought respons with 403 error but the xmplrpc is enabled just the error because The following request requires permissions for some Boths.

## Supporting Material/References:
         Reference:
https://medium.com/@the.bilal.rizwan/wordpress-xmlrpc-php-common-vulnerabilites-how-to-exploit-them-d8d3c8600b32
https://medium.com/@protector47/how-to-hack-wordpress-website-via-xmlrpc-php-61c813fa3740
https://hackerone.com/reports/325040?fbclid=IwAR0qgG-Xfzfi8epruslb_aB91f-Nj8DitF0su8O9ibFKSFdvefJ8h_qWNyc
https://hackerone.com/reports/752073?fbclid=IwAR2i3AM4woHlr01MvyJR-Vu485XQg_gxb1doWmAhSBTfxPK9cUSRFxO2iFo

## Impact

This method is also used for brute force attacks to stealing the admin credentials and other important credentials
This can be automated from multiple hosts and be used to cause a mass DDOS attack on the victim.

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
