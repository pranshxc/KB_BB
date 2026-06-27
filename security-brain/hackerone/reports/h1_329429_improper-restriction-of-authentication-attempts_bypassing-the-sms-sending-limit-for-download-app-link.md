---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '329429'
original_report_id: '329429'
title: Bypassing the SMS sending limit for download app link.
weakness: Improper Restriction of Authentication Attempts
team_handle: zomato
created_at: '2019-03-28T11:29:41.769Z'
disclosed_at: '2019-04-16T15:45:53.262Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 7
asset_identifier: '*.zomato.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# Bypassing the SMS sending limit for download app link.

## Metadata

- HackerOne Report ID: 329429
- Weakness: Improper Restriction of Authentication Attempts
- Program: zomato
- Disclosed At: 2019-04-16T15:45:53.262Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

**Summary:** Here an attacker can send the download link sms to any number of people bypassing the sms rate limit imposed by zomato.

**Description:** zomato provides an easy way for the users to download their app when they are at the home page of zomato's website. A user can send upto 15 sms ( to themself or others) and after that the rate limit is imposed (Preventing them to abuse it). But however it can be bypassed.

**Platform(s) Affected:** website

## Steps To Reproduce:


  1. visit to the website https://www.zomato.com/
  2. Now at the bottom there is a TEXT LINK BUTTON (Click it and intercept the request)
  3. It has an endpoints which have two **type** paramete rwhich handles the same sms functionality.

a) ``` /php/restaurantSmsHandler.php?type=app-download-sms&mobile_no=<NUMBER>&csrf_token=<TOKEN>```

b) ``` /php/restaurantSmsHandler.php?type=order-app-download-sms&mobile_no=<NUMBER>&csrf_token=<TOKEN>```

4) Now if we give the list of mobile number's to **mobile_no** parameter then all the numbers in this list are going to receive the sms.

 `/php/restaurantSmsHandler.php?type=app-download-sms&mobile_no=[8127410000,8317030000,...]&csrf_token=<TOKEN>`

>Here there is no limit on number of MOBILE NUMBERs that can we putted in the list.

## Supporting Material/References:
F453703: Screenshot from 2019-03-28 16-45-54.png

## Impact

>The attacker can send the spam download app sms to any number of people without any limit

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
