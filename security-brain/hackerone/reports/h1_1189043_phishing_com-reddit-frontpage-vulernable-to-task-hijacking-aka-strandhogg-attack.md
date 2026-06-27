---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1189043'
original_report_id: '1189043'
title: com.reddit.frontpage vulernable to Task Hijacking (aka StrandHogg Attack)
weakness: Phishing
team_handle: reddit
created_at: '2021-08-31T11:32:38.595Z'
disclosed_at: '2021-12-13T22:48:14.542Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 1
asset_identifier: com.reddit.frontpage
asset_type: GOOGLE_PLAY_APP_ID
max_severity: critical
tags:
- hackerone
- phishing
---

# com.reddit.frontpage vulernable to Task Hijacking (aka StrandHogg Attack)

## Metadata

- HackerOne Report ID: 1189043
- Weakness: Phishing
- Program: reddit
- Disclosed At: 2021-12-13T22:48:14.542Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

## Summary:
The app com.reddit.frontpage is vulnerable to Task Hijacking used by widespread Android trojans. Task hijacking allows malicious apps to inherit permissions of vulnerable apps and is usually used for phishing login credentials of victims.

## Impact:
Assuming a malicious actor want's to grab the login credentials of an app user they can hijack the main tasks by overriding the taskAffinity to the vulnerable android package. When the victim then tries to open the legitimate app the malicious app can inject their own activities and phish credentials of the victim.

## Steps To Reproduce:
  1. Victim installs malicious app
  1. Victim starts malicious app (could also be a background service)
  1. Victim opens legitimate app which the malicious app can intercept.

This does NOT require root nor any permissions in the malicious app.
To prevent this attack you will need to set taskAffinity property of the application activities to ""(empty string) in the <activity> tag of
the AndroidManifest.xml to force the activities to use a randomly generated task affinity, or set it at the <application> tag to enforce on all activities in the application.

This vulnerability applies to all Android Versions before Android 11.

## Supporting Material/References:
* https://promon.co/security-news/strandhogg/
* https://arstechnica.com/information-technology/2019/12/vulnerability-in-fully-patched-android-phones-under-active-attack-by-bank-thieves/
* Found by: https://ostorlab.co/ Mobile App scanner

## Impact

An attacker could phish the victims user credentials or get additional permissions in the name of the legitimate app which then again could be abused for eavesdropping etc.

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
