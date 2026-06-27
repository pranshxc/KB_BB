---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '736283'
original_report_id: '736283'
title: 'open Firebase Database: msdict-dev.firebaseio.com'
weakness: Improper Access Control - Generic
team_handle: mobisystems_ltd
created_at: '2019-11-12T15:49:57.190Z'
disclosed_at: '2020-01-20T11:47:59.039Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 65
asset_identifier: com.mobisystems.msdict.embedded.wireless.oxford.dictionaryofenglish
asset_type: GOOGLE_PLAY_APP_ID
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# open Firebase Database: msdict-dev.firebaseio.com

## Metadata

- HackerOne Report ID: 736283
- Weakness: Improper Access Control - Generic
- Program: mobisystems_ltd
- Disclosed At: 2020-01-20T11:47:59.039Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
publicly available Firebase Database (msdict-dev.firebaseio.com)

## Steps To Reproduce:
Version: `Oxford Dictionary of English Free_v11.1.511`
in `res/values/strings.xml`
```
<string name="firebase_database_url">https://msdict-dev.firebaseio.com</string>
```

Accessing your Firebase Database via https://msdict-dev.firebaseio.com/.json returns
`null` instead of the usual `{ "error" : "Permission denied" }`

## Supporting Material/References:

https://medium.com/@danangtriatmaja/firebase-database-takover-b7929bbb62e1 describes how a firebase database can be taken over with similar conditions.

## Impact

```The above application doesn’t need any acces_token to insert data to the firebase database it’s completely open and anybody can access it without any access credentials.```

There are guidelines available by Firebase to resolve the insecurities and misconfiguration, please follow this link:
https://firebase.google.com/docs/database/security/resolve-insecurities

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
