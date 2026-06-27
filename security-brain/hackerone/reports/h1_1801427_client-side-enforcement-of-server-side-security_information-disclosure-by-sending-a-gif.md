---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1801427'
original_report_id: '1801427'
title: Information disclosure by sending a GIF
weakness: Client-Side Enforcement of Server-Side Security
team_handle: linkedin
created_at: '2022-12-12T16:08:49.934Z'
disclosed_at: '2023-04-28T23:09:29.419Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 71
asset_identifier: www.linkedin.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- client-side-enforcement-of-server-side-security
---

# Information disclosure by sending a GIF

## Metadata

- HackerOne Report ID: 1801427
- Weakness: Client-Side Enforcement of Server-Side Security
- Program: linkedin
- Disclosed At: 2023-04-28T23:09:29.419Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# Summary
- The attacker can view the Operating System, Version Of  The Operating System, Browser, IP Address, Device ID, Phone Model, Time Zone and other critical information about any LinkedIn user they have identified as a victim.

# Steps to Reproduce

1- Create a standard linkedin user account to use in the attack.
2- Select a GIF from the GIF Keyboard and capture the request with Burp Suite while sending it to your victim.
3- Forward all requests until you get to the voyager/api/voyagerMessagingDashMessengerMessages?action=createMessage endpoint. In this request, type the Burp Suite Collaborator url in message.renderContentUnions.externalMedia.media.url in the JSON Data containing (parameters) section.
4- When the victim opens the message box, the attacker will get critical information about the victim.

** Steps Photo **

{F2073194}
{F2073195}
{F2073196}
{F2073197}
{F2073200}
{F2073201}
{F2073202}

## Notes ##

- This vulnerability affects not only smartphones but all platforms where you can use the link (Smart Phones, iPads, Web Browser, Smart TV etc.)
- When the victim uses an apple phone, much more and critical data can be obtained than the android and web version.

{F2073291}
--------
{F2073293}

## PoC Video
{F2073296}
{F2073297}

## References
- Same Attack Scenarios

https://ph-hitachi.medium.com/facebook-bug-poc-external-service-interaction-dns-http-ab55bfdb98f6

## Impact

Black Hat Hackers can get critical information about all LinkedIn users. The information obtained is very important for the privacy of the users and includes information such as IP address, OS versions.

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
