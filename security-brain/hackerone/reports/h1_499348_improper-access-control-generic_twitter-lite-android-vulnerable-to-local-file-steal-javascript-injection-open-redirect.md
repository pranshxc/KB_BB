---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '499348'
original_report_id: '499348'
title: 'Twitter lite(Android): Vulnerable to local file steal, Javascript injection,
  Open redirect'
weakness: Improper Access Control - Generic
team_handle: x
created_at: '2019-02-21T16:14:32.124Z'
disclosed_at: '2019-04-29T16:17:02.180Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 86
asset_identifier: com.twitter.android
asset_type: GOOGLE_PLAY_APP_ID
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Twitter lite(Android): Vulnerable to local file steal, Javascript injection, Open redirect

## Metadata

- HackerOne Report ID: 499348
- Weakness: Improper Access Control - Generic
- Program: x
- Disclosed At: 2019-04-29T16:17:02.180Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** com.twitter.android.lite.TwitterLiteActivity is set to exported and doesn't validate data pass to intent due to which this activity vulnerable to steal users local files, javascript injection and open redirect.

**Description:** com.twitter.android.lite.TwitterLiteActivity is set to exported so external app can communicate with it.
As this activity doesn't validate data pass through intent critical uri like javascript and file so malicious app can steal users files as well as inject javascript.
It can leads to many issue like UXSS, Token steal, etc.

## Steps To Reproduce:

  1. To reproduce we use ADB tool

  2. To reproduce local file access use: adb shell am start -n com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d "file:///sdcard/BugBounty/1.html"

  3. To reproduce javascript injection: adb shell am start -n com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d "javascript://example.com%0A alert(1);"

  4. To reproduce open redirect: adb shell am start -n com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d "http://evilzone.org"

 * Video of POC attached.

Thanks

## Impact

As critical uri like javascript & file is not being validate malicious app can steal users session token, users files etc.

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
