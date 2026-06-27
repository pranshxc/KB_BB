---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1343733'
original_report_id: '1343733'
title: Broken link profile in the website leads to identity theft.
team_handle: lacework
created_at: '2021-09-19T14:43:06.520Z'
disclosed_at: '2021-10-22T17:35:23.955Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: '*.lacework.net'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# Broken link profile in the website leads to identity theft.

## Metadata

- HackerOne Report ID: 1343733
- Weakness: 
- Program: lacework
- Disclosed At: 2021-10-22T17:35:23.955Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I have found the Broken link profile in the website where the attacker can perform identity theft.

Summary :
When a web application has any pages, sources, links to external 3rd party services and are broken then the attacker can claim those endpoints to successfully conduct the attack and claim those endpoints on behalf of the target website and impersonate his identity.

From : Remote / External

Steps to Reproduce:

1. I have found the Broken link profile on the main webpage https://engineering.lacework.net/
2. I Scrolled down and clicked on the Twitter  profile of the company "https://engineering.lacework.net/#" where I found that the profile is not available.


Affected IP's : IP Address  Port
https://engineering.lacework.net/  443

Recommendations :
Fix all the broken links in the web application to any external resources and make updates to the user profiles in a timely manner.

References :
https://medium.com/@iamtess5277/what-is-broken-link-hijacking-o-o-872d821da6fd
https://medium.com/@arbazhussain/broken-link-hijacking-burp-plugin-6918d922c3fb
https://hackerone.com/reports/266908

Proof of concept:
Attached screenshot for your references.

## Impact

An Adversary can carry out a BLH attack to trick the victim into clicking the link and visiting the resources which are linked to the website, this way the attacker can identify theft and steal credentials.

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
