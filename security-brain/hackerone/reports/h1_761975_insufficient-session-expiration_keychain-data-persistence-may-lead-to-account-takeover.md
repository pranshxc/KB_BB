---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '761975'
original_report_id: '761975'
title: Keychain data persistence may lead to account takeover
weakness: Insufficient Session Expiration
team_handle: qiwi
created_at: '2019-12-19T23:00:36.457Z'
disclosed_at: '2020-09-07T14:47:57.336Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
asset_identifier: ru.qiwi.QIWI
asset_type: APPLE_STORE_APP_ID
max_severity: critical
tags:
- hackerone
- insufficient-session-expiration
---

# Keychain data persistence may lead to account takeover

## Metadata

- HackerOne Report ID: 761975
- Weakness: Insufficient Session Expiration
- Program: qiwi
- Disclosed At: 2020-09-07T14:47:57.336Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary
When user deletes Qiwi iOS application Keychain isn't wiped and on first Qiwi launch after re-installation Keychain isn't wiped as well. It allows an attacker (possible buyer of second hand Iphone) to takeover account.

## Steps to reproduce
1. Find somebody who uses Qiwi (phone enumeration may help I guess) and desires to sell his Iphone (on Avito per example)
1. Meet up with the seller and check that Iphone isn't wiped to factory settings
1. Check that Qiwi app is deleted (seller isn't technically educated and thinks that if he have deleted an app, he is fine and safe)
1. Navigate to Settings and type Qiwi, this way you can find that the user previously had Qiwi app installed (it was surprise for me, but this way Apple returns empty line with "QIWI" as text, but without an icon)
1. Buy the Iphone and hope that the seller forgot to logout from Qiwi
1. Install Qiwi
1. If Qiwi asks to enter PIN, continue, either you can't get in (probably, because I have checked if Keychain wiped after log-out)
1. Jailbreak Iphone and attach Frida or Cydia to the app
1. Locate the function which checks PIN and find correct PIN (it was stored somewhere in class data in plaintext)
1. Login to QIWI with found PIN

## Mitigation
Wipe Keychain on first launch of application.

## References
* https://mobile-security.gitbook.io/mobile-security-testing-guide/ios-testing-guide/0x06d-testing-data-storage#data-protection-api (scroll to Keychain Data Persistence)

> There's no iOS API that developers can use to force wipe data when an application is uninstalled. Instead, developers should take the following steps to prevent Keychain data from persisting between application installations:
* When an application is first launched after installation, wipe all Keychain data associated with the application. This will prevent a device's second user from accidentally gaining access to the previous user's accounts.

## Notes
If it's possible do not close the report as N/A, I have thought if I should to send the report for about a month or two (in that period developers added and removed Jailbreak detection, I don't know why), messaged to somebody from Qiwi security team, but got no response. (thanks for reading)

## Impact

As it's a bank application, in my opinion developers should be extra careful about user security. So I think in this way security > UI (it isn't so hard to get SMS and enter it to login after re-installation of an app).

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
