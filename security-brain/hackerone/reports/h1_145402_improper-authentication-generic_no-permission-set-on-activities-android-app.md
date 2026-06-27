---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145402'
original_report_id: '145402'
title: No permission set on Activities [Android App]
weakness: Improper Authentication - Generic
team_handle: nextcloud
created_at: '2016-06-17T13:50:03.526Z'
disclosed_at: '2016-06-20T15:10:52.170Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- improper-authentication-generic
---

# No permission set on Activities [Android App]

## Metadata

- HackerOne Report ID: 145402
- Weakness: Improper Authentication - Generic
- Program: nextcloud
- Disclosed At: 2016-06-20T15:10:52.170Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Android app version: 1.0.0

Issue Details:
-----------------
The following activities are exported and it does not have a permission set. 

1) com.owncloud.android.ui.activity.FileDisplayActivity
2) com.owncloud.android.ui.activity.ReceiveExternalFilesActivity
3) com.owncloud.android.authentication.AuthenticatorActivity
4) com.owncloud.android.ui.activity.ShareActivity

This could allow any malicious application to initiate the above mentioned activities thus bypassing security checks or getting private information of any user.

Recommendation:
-------------------------
Set the permission for the above mentioned activities or either set android:exported=false (which allows the activities to be launched by only components of the same app or the same uid)

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
