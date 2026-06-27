---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '631206'
original_report_id: '631206'
title: Passcode Protection in Android Devices Can be Bypassed.
weakness: Violation of Secure Design Principles
team_handle: nextcloud
created_at: '2019-06-28T03:01:29.577Z'
disclosed_at: '2019-08-27T07:27:27.266Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 6
asset_identifier: com.nextcloud.client
asset_type: GOOGLE_PLAY_APP_ID
max_severity: medium
tags:
- hackerone
- violation-of-secure-design-principles
---

# Passcode Protection in Android Devices Can be Bypassed.

## Metadata

- HackerOne Report ID: 631206
- Weakness: Violation of Secure Design Principles
- Program: nextcloud
- Disclosed At: 2019-08-27T07:27:27.266Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

###What is The Vulnerability?

The Passcode can be bypassed by calling a MainLoginActivity which is com.owncloud.android.ui.activity.FileDisplayActivity , We have successfully bypassed the passcode and are redirected to the App's User Interface.
of the user’s credentials:

Android Version: 9
Non Rooted Device.

##How to Reproduce:
1.) Setup a Emulated Device Via Android Studio AVD Using the Same Setup.
{F518191}

2.) Install NextCloud Client and Login Your NextCloud Account.

{F518192}

3.) Setup the PassCode

{F518193}

4.) Install Drozer and Drozer Agent

* https://labs.mwrinfosecurity.com/tools/drozer/

5.) Start the Drozer Embedded Server

{F518195}

6.) Open your CMD/Console and type ```drozer console connect```

█████████

7.) Close the NextCloud Client and Open it Again

{F518197}

8.) Go Back to Drozer Console and run this code
```run app.activity.start --component com.nextcloud.client com.owncloud.android.ui.activity.FileDisplayActivity```

9.) Voila, Passcode Bypassed

{F518198}

##Supporting Materials

* Attached as poc.mp4

█████

## Impact

Successful exploitation of this vulnerability allows an attacker to bypass the android application's authentication mechanisms and gain unauthorized access to the user files and infos.

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
