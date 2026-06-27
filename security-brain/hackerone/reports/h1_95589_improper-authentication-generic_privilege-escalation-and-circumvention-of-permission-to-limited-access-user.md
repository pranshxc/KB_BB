---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '95589'
original_report_id: '95589'
title: Privilege escalation and circumvention of permission to limited access user
weakness: Improper Authentication - Generic
team_handle: shopify
created_at: '2015-10-24T12:39:14.004Z'
disclosed_at: '2015-11-11T02:06:42.520Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# Privilege escalation and circumvention of permission to limited access user

## Metadata

- HackerOne Report ID: 95589
- Weakness: Improper Authentication - Generic
- Program: shopify
- Disclosed At: 2015-11-11T02:06:42.520Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Scenario:
Test shopify shop : https://elamaranhack.myshopify.com/admin
User1 : elamaran+hackerone@shopify.com(X) - Account Owner(Shop Admin)
User2 : elamaran619@gmail.com(Y) - Limited access user(access to Sales Channels Overviews only)

Limited access user(Y) who don't have permission to access home page activities is able to see all shop owner activities using the request 
"https://elamaranhack.myshopify.com/admin/dashboard/activity_feed?activity_pages=XXXX&activity_filter=all" where XXXX is page number

Steps to reproduce:
1) Created users X & Y with above mentioned permissions(X1.png,X2.png)
2) Shop admin X views his activities using url "https://elamaranhack.myshopify.com/admin/activity" (X3.png,X4.png)
3) If limited access user Y tried to view shop admin activities, the system blocks the url rightly (Y1.png)
4) There is one option for shop admin X to load more activities using url "https://elamaranhack.myshopify.com/admin/dashboard/activity_feed?activity_pages=XXXX&activity_filter=all" where XXXX is page number (X5.png, X6.png)
5) If the limited access user Y use the url "https://elamaranhack.myshopify.com/admin/dashboard/activity_feed?activity_pages=XXXX&activity_filter=all" , he can able to view all shop admin activities (Y2.png, Y3.png)

Error screenshots attached for reference.

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
