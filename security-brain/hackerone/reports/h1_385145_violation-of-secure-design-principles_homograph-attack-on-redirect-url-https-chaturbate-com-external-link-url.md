---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '385145'
original_report_id: '385145'
title: Homograph attack on redirect URL (https://chaturbate.com/external_link/?url)
weakness: Violation of Secure Design Principles
team_handle: chaturbate
created_at: '2018-07-22T09:07:16.037Z'
disclosed_at: '2018-09-20T00:06:12.880Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: chaturbate.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Homograph attack on redirect URL (https://chaturbate.com/external_link/?url)

## Metadata

- HackerOne Report ID: 385145
- Weakness: Violation of Secure Design Principles
- Program: chaturbate
- Disclosed At: 2018-09-20T00:06:12.880Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi There,

Hope you are doing good,

As i was just playing around with ```chaturbate.com``` and found that you guys does not have proper configuration for malicious script injection in website.

In Homograph attack basically attacker may able to inject some malicious script with URL.

Here i made homograph link for the ```ebay.com```, when normal user see this link its look like normal simple text link but no its not simple link it's crafted homograph malicious script link so when user see this particular link user might be think that they are going to redirect on ```eBay.com``` but the fact that the link which add is malicious link and made from homograph encoding so when user click on this link user will redirect on some malicious website.

The IDN (Malicious link which i add in website) : ```https://xn--eby-7cd.com``` in looking it's look like ```eBay.com``` but when user click this link user will redirect on malicious website.

**POC video**
{F323281}

**POC URL**
https://chaturbate.com/external_link/?url=http://ebаy.com/

**Prevention of this vulnerability**

To prevent this vulnerability it would be safer to show the punycode version of the url so it would be apparent that something weird is going on. that is, show ```http://xn--eby-7cd.com/``` instead of ```eBay.com```.

you can see that how hackerone prevent this vulnerability

For instance, Here you can see that in hackerone if i am attaching punycode homograph URL but when you click on this link it will show you actual encryption URL of malicious URL : http://xn--eby-7cd.com/ - Click on this link and you will get know how to prevent this vulnerability or else you can also put prevention by adding validation on particular field for URL.

Reference

https://hackerone.com/reports/29491
https://hackerone.com/reports/175286

Please let me know if you want more information then,

Cheers, 
Ninjan

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
