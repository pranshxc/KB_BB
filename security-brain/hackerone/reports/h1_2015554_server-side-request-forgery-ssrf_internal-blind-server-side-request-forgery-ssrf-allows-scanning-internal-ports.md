---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2015554'
original_report_id: '2015554'
title: Internal Blind Server-Side Request Forgery (SSRF) allows scanning internal
  ports
weakness: Server-Side Request Forgery (SSRF)
team_handle: mozilla
created_at: '2023-06-07T08:05:58.532Z'
disclosed_at: '2024-01-12T16:35:59.521Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 42
asset_identifier: getpocket.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# Internal Blind Server-Side Request Forgery (SSRF) allows scanning internal ports

## Metadata

- HackerOne Report ID: 2015554
- Weakness: Server-Side Request Forgery (SSRF)
- Program: mozilla
- Disclosed At: 2024-01-12T16:35:59.521Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
Blind SSRF reports on services that are designed to load resources from the internet is Out of scope but this is a Internal Blind SSRF report so should be a Valid find as I am reading the localhost not someone else server.
I found a Blind SSRF issue that allows scanning internal ports on https://getpocket.com/saves , the server will give different response  the request to all the closed ports and  we can use this in our advantage.
I also confirm this by doing a scan on my network for open ports and closed ports thus proving that the open and closed ports show different response 

## Steps To Reproduce:

1. Go to https://getpocket.com/saves? as an Authenticated person
2. Click on the Plus Icon at the Top and enter the URL "https://127.0.0.1:1"
3. intercept this request using a Proxy like BURP and send the request to the Repeater Tab [Intruder Tab if you want to scan ]
4. change the ports to see different results , You will see different  response for the different ports which shows which one is open and which one is closed.

Such as 
https://127.0.0.1:22 Open
https://127.0.0.1:21 close
https://127.0.0.1:86 Open
https://127.0.0.1:88 Open
https://127.0.0.1:87 close

## Supporting Material/References:
https://hackerone.com/reports/1300585

##PoC
Scanning the Internal system
{F2403088}

Proving that the Open ports gives greater then 3000 length response 
{F2403089}

## Impact

This vulnerability can be used for reconnaissance. Attacker can enumerate services and launch attacks against them
Example: Port Scan by different response from the server

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
