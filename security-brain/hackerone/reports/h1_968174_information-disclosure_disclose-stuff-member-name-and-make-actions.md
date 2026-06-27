---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '968174'
original_report_id: '968174'
title: Disclose STUFF member name and make actions.
weakness: Information Disclosure
team_handle: shopify
created_at: '2020-08-27T00:04:04.884Z'
disclosed_at: '2022-05-14T14:34:50.371Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
asset_identifier: Shopify Developed Apps
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- information-disclosure
---

# Disclose STUFF member name and make actions.

## Metadata

- HackerOne Report ID: 968174
- Weakness: Information Disclosure
- Program: shopify
- Disclosed At: 2022-05-14T14:34:50.371Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Shopify Security Team!

 Bug Summary:
=============

Based on the report #968165, this also can retrieve the STUFF member name and can send messages using his name.

 Reproduction steps:
=============
  - install shopify chat applications.

Start Exploit #1 : 
=============
+ Go to targeted store : 
+ Start a chat using the app with the store support.
+ Click on _I need an update on my order_.
+ fill out the Order ID and Email. ( fill the info randomly if you want to), the respond comes with message "in order to provide you with ....".
+  I intercept the the post request, and inject changes in the request, 
+ In this exploit allowed the attacker to send messages like a team member (bot)

{F965084}

Example : i changed text element  to " Hello customer hahaha "

Result : 
========

poc from shopify ping application ( STUFF side )

{F965081}


 Start Exploit #2 : 
=============
+ Go to targeted store : 
+ Start a chat using the app with the store support.
+ As soon as you get the answer.
+ I intercept the message request, i found the STUFF member name and ID.

{F965077}

{F965078}

## Impact

Can retrive STUFF info,  not allowed !

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
