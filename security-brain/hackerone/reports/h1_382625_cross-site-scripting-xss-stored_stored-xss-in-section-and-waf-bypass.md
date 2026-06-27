---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '382625'
original_report_id: '382625'
title: Stored XSS in '' Section and WAF Bypass
weakness: Cross-site Scripting (XSS) - Stored
team_handle: semrush
created_at: '2018-07-17T14:32:28.592Z'
disclosed_at: '2018-12-07T13:58:31.468Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 40
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in '' Section and WAF Bypass

## Metadata

- HackerOne Report ID: 382625
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: semrush
- Disclosed At: 2018-12-07T13:58:31.468Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary 
   Stored Cross-site Scripting (XSS) is the most dangerous type of Cross Site Scripting. Web applications that allow users to store data are potentially exposed to this type of attack. stored XSS occurs when a web application gathers input from a user which might be malicious, and then stores that input in a data store for later use. 

## Description 
   I have found this Stored XSS in 'position tracking' of [SEMrush](http://semrush.com) website.
first I setup 'position tracking' then in 'Rankings Distribution' tab add a valid domain in competitor's domain field which is check the validation just in client side so I try to hook it via BurpSuit and change the domain parameter to my XSS payload, as I see it saved my payload completely but by the time it wants to show me, my payload must have passed through the website Firewall so there is nothing to show.
As I guess the Firewall probably uses blacklist that controls just the HTTP/GET method so Although it blocked lots of HTML tags and attributes but I try hard and bypass it after all as shown in Figures  F321488 and F321489.
in conclusion, there is a WAF bypass vulnerability besides the XSS that may cause of effects in other vulnerabilities happening.

## Browsers Verified In
   Mozilla 5.0 Firefox 52.0 ESR

## Steps To Reproduce
   1. Log in to your account.
   2. Create project.
   3. Navigate to Dashboard-> Position Tracking ->Rankings Distribution -> select one of add domains -> click on "Edit competitor's list"
    4. Fill 'new competitor's domain' field with a valid domain like google.com then open BurpSuit for changing the domain parameter with the payload below then click on "Add to list"
```"><u>XSS Vulnerability</u><marquee+onstart='alert(document.cookie)'>XSS```

  Note: lots of tags and attributes are blocked by the firewall but this rare payload isn't blocked so far and works correctly as shown in Figure F321486.
   5. After changing the domain parameter click on 'Update' button then close "Position Tracking Settings" page.
    6. And shown in Figure F321490 after closing the "Position Tracking Settings" page the XSS is loaded.

## Supporting Material/References:

{F321488}
{F321489}
{F321486}
{F321490}

https://www.owasp.org/index.php/Testing_for_Stored_Cross_site_scripting_(OTG-INPVAL-002)

## Impact

The attacker can have the session and cookie of customers and deface that page.
The firewall that uses blacklist is bypassed by the special payload.

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
