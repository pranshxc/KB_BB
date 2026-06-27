---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '792850'
original_report_id: '792850'
title: Hard-coded API keys at NordVpn Android App
weakness: Use of Hard-coded Credentials
team_handle: nordsecurity
created_at: '2020-02-11T00:42:03.520Z'
disclosed_at: '2020-03-27T10:50:58.537Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 10
asset_identifier: com.nordvpn.android
asset_type: GOOGLE_PLAY_APP_ID
max_severity: critical
tags:
- hackerone
- use-of-hard-coded-credentials
---

# Hard-coded API keys at NordVpn Android App

## Metadata

- HackerOne Report ID: 792850
- Weakness: Use of Hard-coded Credentials
- Program: nordsecurity
- Disclosed At: 2020-03-27T10:50:58.537Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello NordVpn,

**APK Version : 4.6.2**
**API'S at res/values/strings.xml**

>**Google**
>google_api_key = ███
**Stripe**
>stripe_publishable_api_key = ██████████

**Referance;** 
>https://stripe.com/docs/keys

## Impact

Cleartext Storage of Sensitive Information

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
