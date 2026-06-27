---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '114631'
original_report_id: '114631'
title: Several XSS affecting Zomato.com and developers.zomato.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: zomato
created_at: '2016-02-04T12:59:43.501Z'
disclosed_at: '2016-08-02T03:51:51.427Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Several XSS affecting Zomato.com and developers.zomato.com

## Metadata

- HackerOne Report ID: 114631
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: zomato
- Disclosed At: 2016-08-02T03:51:51.427Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi there, I have found several XSS in Zomato.com and developers.zomato.com

A. Steps to reproduce:
1. Go to zomato.com
2. Look for any restaurant
3. Click "Write review" and enter the payload as your review
                                             (<img src=x onerror=alert(document.domain)>)
4. Click "Publish review" . XSS pop up

B. Now in developers.zomato.com:
1. Go to developers.zomato.com
2. Go to "widgets" tab
3. Look for "Restaurant Search" widget and click "Add Widget"
4. Now a window will open (restaurant search), on the left side, you will see "Search for restaurant, cuisine or a dish" now, enter the payload   (<img src=x onerror=alert(document.domain)>) in the seachbar, XSS popup.

C. developers.zomato.com (II)
1. Go to developers.zomato.com
2. Go to "widgets" tab
3. Look for "Foodie Index Widget"
4. Click "add widget"
5. In the longitude and latitude, enter the XSS payload
 (<img class="emoji" alt="😯" src="x" /><svg onload=prompt(document.domain)>). 
6. XSS popup

I hope you fix this since this are affecting several zomato users.
Thanks

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
