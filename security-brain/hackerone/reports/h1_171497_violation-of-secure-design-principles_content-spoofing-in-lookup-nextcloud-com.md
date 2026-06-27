---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '171497'
original_report_id: '171497'
title: Content spoofing in lookup.nextcloud.com
weakness: Violation of Secure Design Principles
team_handle: nextcloud
created_at: '2016-09-23T16:56:06.861Z'
disclosed_at: '2016-10-10T14:56:44.467Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- violation-of-secure-design-principles
---

# Content spoofing in lookup.nextcloud.com

## Metadata

- HackerOne Report ID: 171497
- Weakness: Violation of Secure Design Principles
- Program: nextcloud
- Disclosed At: 2016-10-10T14:56:44.467Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Scenerio**
An attacker can include any arbitrary text using specially crafted nextcloud url.
This is done using character /%0d%0a.

**Steps**
1) Attacker distributed the below url by means of spamming or through his website
https://lookup.nextcloud.com/%0d%0ahas%20moved%20to%20www.evil.com.Please%20visit%20evil.com%20Present%20resource
2) Victim see below text 
The requested URL / has moved to www.evil.com.Please visit evil.com Present resource was not found on this server.
3) Since the text came from official site so user believes and gets into attacker trap

**Resolution**
Crafted text should not be responded back in the response HTML

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
