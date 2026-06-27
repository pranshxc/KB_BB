---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '884756'
original_report_id: '884756'
title: xmlrpc.php FILE IS enable which enables attacker to XSPA Brute-force and even
  Denial of Service(DOS), in https://████/xmlrpc.php
weakness: Uncontrolled Resource Consumption
team_handle: deptofdefense
created_at: '2020-05-28T14:33:18.757Z'
disclosed_at: '2020-06-25T13:02:58.803Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- uncontrolled-resource-consumption
---

# xmlrpc.php FILE IS enable which enables attacker to XSPA Brute-force and even Denial of Service(DOS), in https://████/xmlrpc.php

## Metadata

- HackerOne Report ID: 884756
- Weakness: Uncontrolled Resource Consumption
- Program: deptofdefense
- Disclosed At: 2020-06-25T13:02:58.803Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Summary:

Hello team,

I have found a security vulnerability inhttps://███████/xmlrpc.php which lets attacker to:

1: XSPA or PortScan

2: Bruteforce

3:DOS and much more

##Description:

##Impact
Step-by-step Reproduction Instructions
█████████
1: Go to https://██████/xmlrpc.php to check if it is enabled or not.

Remediation:
If the xmlrpc.php file is not being used, it should be disabled and removed completely to avoid any potential risks. Otherwise, it should at the very least be blocked from external access.

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
