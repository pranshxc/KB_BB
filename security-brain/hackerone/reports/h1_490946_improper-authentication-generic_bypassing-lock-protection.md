---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '490946'
original_report_id: '490946'
title: Bypassing lock protection
weakness: Improper Authentication - Generic
team_handle: nextcloud
created_at: '2019-02-04T10:52:20.351Z'
disclosed_at: '2019-07-26T07:42:20.235Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: com.nextcloud.client
asset_type: GOOGLE_PLAY_APP_ID
max_severity: medium
tags:
- hackerone
- improper-authentication-generic
---

# Bypassing lock protection

## Metadata

- HackerOne Report ID: 490946
- Weakness: Improper Authentication - Generic
- Program: nextcloud
- Disclosed At: 2019-07-26T07:42:20.235Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Nextcloud allows multi account within the android client app and relies on a single lock

Based on the (exposed) intent nc://login, it is possible to add a new account under attacker domain and open the Nextcloud without the lock check.

# Proof of concept
1. open the NC app with the lock displayed
2. triggers the following intent 
adb shell am start -a android.intent.action.VIEW -d "nc://login/server:MY_SERVER\&user:ME\&password:PWD  --es "ACCOUNT" "not_valid"
3. if the "add an account" action fails, attacker can still add an account in the screen
the app opens and attacker can check other accounts installed on the app.

# Remark
note that the "adb shell" comamnds could also be trigger with an app, making adb access not required
the "--es" option is required to prevent an app crash on

     AuthenticatorActivity.java:303
      mAccount = getIntent().getExtras().getParcelable(EXTRA_ACCOUNT);

## Impact

Lock can be removed and then data can be retrieved / alter / uploaded

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
