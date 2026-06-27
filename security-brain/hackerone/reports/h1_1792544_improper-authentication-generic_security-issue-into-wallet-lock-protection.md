---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1792544'
original_report_id: '1792544'
title: Security Issue into Wallet lock protection
weakness: Improper Authentication - Generic
team_handle: hiro
created_at: '2022-12-04T17:20:39.715Z'
disclosed_at: '2023-01-11T13:17:23.226Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 47
tags:
- hackerone
- improper-authentication-generic
---

# Security Issue into Wallet lock protection

## Metadata

- HackerOne Report ID: 1792544
- Weakness: Improper Authentication - Generic
- Program: hiro
- Disclosed At: 2023-01-11T13:17:23.226Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# Description

While testing wallet extension i generally try to test multiple endpoints, so 2 tabs were open of wallet on chrome-extension://ldinpeekobnhjjdofggfgjlcehhmanlj/popup.html


So i tried to lock Wallet extension buti found that i can still use browser in 2nd tab, why i had already locked wallet,


So there is a security issue where wallet is not properly encrypted after user press lock

Wallet should close all open tabs of wallets and encrypt data for all tabs, It's very insecure way of password protection or lock protection


# Steps To reproduce

To understand clearly i had created a POC video 
{F2061644}

1. Open two tabs of chrome-extension://ldinpeekobnhjjdofggfgjlcehhmanlj/popup.html
2. lock wallet in any of 1 tab and you can see you can access wallet on other tab and still able to do transaction as shown in POC{F2061648}


# HOW to fix?

Edit code and make sure when user click on lock wallet wallet should encrypt data in all tabs or close rest of the tabs to protect user and make lock protection work more securely

Thank you

## Impact

This is totally fail of lock protection AND attacker can use this vulnerability to craft custom attacks

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
