---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '56002'
original_report_id: '56002'
title: Shopify android client all API request's response leakage, including access_token,
  cookie, response header, response body content
weakness: Improper Authentication - Generic
team_handle: shopify
created_at: '2015-04-12T08:51:42.562Z'
disclosed_at: '2015-07-04T15:45:09.606Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- improper-authentication-generic
---

# Shopify android client all API request's response leakage, including access_token, cookie, response header, response body content

## Metadata

- HackerOne Report ID: 56002
- Weakness: Improper Authentication - Generic
- Program: shopify
- Disclosed At: 2015-07-04T15:45:09.606Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Shopify android client all API request's response leakage, including access_token, cookie, response header, response body content and much other information. An attacker can extract cookie and access_token of Shopify android client without any permission needed and user awareness.

#Bug impact:

A malicious android app can extract cookie and access_token and other user sensitive information in Shopify android client, and thus taking control of user's account.

Bug demostration (see two screenshots with stolen cookie in http headers printed in logcat and access_token).

#Bug explaination:

The shopify client use implicit broadcast to communicate intra-app to pass network request's response infromation, with action "com.shopify.service.requestComplete". However this broadcast is not protected by permission, thus any android client can register a broadcast receiver and monitor response information, extracting sensitive account credentials.

The broadcast is send at com/shopify/service/netcomm/NetworkService, recvd at multiple points. including com/shopify/service/BaseRequestDelegate$RequestCompletionBroadcastReceiver$1.

#Steps to reproduce:

- Install the poc apk and shopify client, poc apk registered a receiver and monitor in background
- Open shopify and login, the poc apk will now receives user's admin_cookie and access_token silently, print them in logcat as demonstrated in screenshots. Of course the attacker can send it to remote control center and fully take control of user's account.
- As user operates the attacker can receives other response information.
- logcat command:  adb logcat -s SHOPIFYHACK:V

#Fix recommendations:

Use signature level permission to protect the broadcast, or use a LocalBroadcastManager

POC apk attached, tested on Nexus 5 4.4.4. No special permission or root required. No user interactions and awareness.

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
