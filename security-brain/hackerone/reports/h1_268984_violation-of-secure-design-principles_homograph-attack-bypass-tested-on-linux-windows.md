---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '268984'
original_report_id: '268984'
title: Homograph Attack Bypass [ Tested on Linux & Windows ]
weakness: Violation of Secure Design Principles
team_handle: brave
created_at: '2017-09-17T05:42:23.050Z'
disclosed_at: '2017-09-21T03:25:02.684Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- violation-of-secure-design-principles
---

# Homograph Attack Bypass [ Tested on Linux & Windows ]

## Metadata

- HackerOne Report ID: 268984
- Weakness: Violation of Secure Design Principles
- Program: brave
- Disclosed At: 2017-09-21T03:25:02.684Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

##Summary:
at #175286 you has been patched, and i try it work, but i've another way to bypass it. when we add a site to our Homepage with `@`, it's not validate a url properly, make sure it's display the punycode.

##Products affected:

Brave	0.18.36 ( Linux & Windows )

##Steps To Reproduce:

1. In browser add homepage with IDN `@ebаy.com/`
1. now close and open browser again
1. you can see it's redirect to http://xn--eby-7cd.com/

{F221533}

##References:
https://hackerone.com/reports/175286

##Video 
https://youtu.be/aCDeZRdRCuk (unlisted)

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
