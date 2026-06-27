---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '859136'
original_report_id: '859136'
title: Malicious apps can crash Nextcloud Android client by sending malformed intents
team_handle: nextcloud
created_at: '2020-04-25T11:05:52.815Z'
disclosed_at: '2021-06-17T10:50:12.335Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: com.nextcloud.client
asset_type: GOOGLE_PLAY_APP_ID
max_severity: medium
tags:
- hackerone
---

# Malicious apps can crash Nextcloud Android client by sending malformed intents

## Metadata

- HackerOne Report ID: 859136
- Weakness: 
- Program: nextcloud
- Disclosed At: 2021-06-17T10:50:12.335Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Not sure if this can be tracked as a security issue, but this definitely calls for a code change. This can be classified into Denial of Service category attack and can seriously hamper user experience. 

Asset: Nexcloud Android Client (com.nextcloud.client)
Version: 3.11.1 (latest)

###_Details_ 

The Nextcloud android app registers a deeplink `nc://login` that is handled by the `com.owncloud.android.authentication.ModifiedAuthenticatorActivity` class as seen in AndroidManifest file.

The above mentioned class implements `AuthenticatorActivity` class in order to handle incoming deeplinks.

It is seen that the method `parseLoginDataUrl` does not handle exception correctly crashing the Nextcloud app.  

malicious apps can thus crash the nextcloud client by sending following data in intent : `nc://login`. 

ADB payload:

```
adb shell am start -a "android.intent.action.VIEW" -c "android.intent.category.DEFAULT" -n "com.nextcloud.client/com.owncloud.android.authentication.ModifiedAuthenticatorActivity" -d "nc://login"
```

Attaching video PoC
{F803256}

## Impact

1. Malicious apps can crash the nextcloud android client to cause a denial of service attack.

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
