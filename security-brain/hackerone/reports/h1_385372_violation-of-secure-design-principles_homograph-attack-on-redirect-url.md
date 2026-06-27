---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '385372'
original_report_id: '385372'
title: Homograph attack on redirect URL
weakness: Violation of Secure Design Principles
team_handle: chaturbate
created_at: '2018-07-23T12:06:19.169Z'
disclosed_at: '2018-10-19T22:09:10.773Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
asset_identifier: m.chaturbate.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Homograph attack on redirect URL

## Metadata

- HackerOne Report ID: 385372
- Weakness: Violation of Secure Design Principles
- Program: chaturbate
- Disclosed At: 2018-10-19T22:09:10.773Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Team

There is no Homography protection on redirect URL
URL:
https://m.chaturbate.com/external_link/?url=http://ebаy.com

In Homograph attack basically attacker may able to inject some malicious script with URL.

Here i made homograph link for the ebay.com, when normal user see this link its look like normal simple text link but no its not simple link it's crafted homograph malicious script link so when user see this particular link user might be think that they are going to redirect on eBay.com but the fact that the link which add is malicious link and made from homograph encoding so when user click on this link user will redirect on some malicious website.

The IDN (Malicious link which i add in website) : https://xn--eby-7cd.com in looking it's look like eBay.com but when user click this link user will redirect on malicious website.

Vulnerable  URL: https://m.chaturbate.com/external_link/?url=http://ebаy.com

Reference

https://hackerone.com/reports/29491
https://hackerone.com/reports/175286

## Impact

Attacker may able to inject any homograph URL in website and able to scratch any normal user to their malicious website.

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
