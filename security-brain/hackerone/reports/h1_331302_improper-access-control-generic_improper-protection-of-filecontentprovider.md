---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '331302'
original_report_id: '331302'
title: Improper protection of FileContentProvider
weakness: Improper Access Control - Generic
team_handle: nextcloud
created_at: '2018-03-30T08:21:53.366Z'
disclosed_at: '2020-03-01T14:05:16.781Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
asset_identifier: com.nextcloud.client
asset_type: GOOGLE_PLAY_APP_ID
max_severity: medium
tags:
- hackerone
- improper-access-control-generic
---

# Improper protection of FileContentProvider

## Metadata

- HackerOne Report ID: 331302
- Weakness: Improper Access Control - Generic
- Program: nextcloud
- Disclosed At: 2020-03-01T14:05:16.781Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Some data in the FileContentProvider is protected against applications not related to NextCloud. The application checks if calling application package name contains "com.nextcloud.client" string. Every application with such substring in package name is allowed to fully access FileContentProvider.

com.owncloud.android.providers.FileContentProvider

``` java
    private boolean isCallerNotAllowed() {
        String callingPackage = this.mContext.getPackageManager().getNameForUid(Binder.getCallingUid());
        return callingPackage == null || !callingPackage.contains(this.mContext.getPackageName());
    }
```

## Impact

Malicious applications with "com.nextcloud.client" in their package names are able to access FileContentProvider without restrictions. For example they are able to read private keys to end-to-end encryption using URI: content://org.nextcloud/arbitrary_data

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
