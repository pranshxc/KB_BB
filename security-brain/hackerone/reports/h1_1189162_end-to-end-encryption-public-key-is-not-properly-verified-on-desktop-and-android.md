---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1189162'
original_report_id: '1189162'
title: End to end encryption public key is not properly verified on Desktop and Android
team_handle: nextcloud
created_at: '2021-05-08T19:22:20.438Z'
disclosed_at: '2021-09-23T12:25:34.076Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
asset_identifier: Desktop Client
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
---

# End to end encryption public key is not properly verified on Desktop and Android

## Metadata

- HackerOne Report ID: 1189162
- Weakness: 
- Program: nextcloud
- Disclosed At: 2021-09-23T12:25:34.076Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Since last time when I reported something on multiple platforms you seems to prefer handling it in 1 spot. I now just do one. Let me know if You want me to fill separate for android as well. This issue does not seem to happen on iOS as there a test string is encrypted and decrypted, in short binding the keypair.

So the attack vector results in weird behavior but that seems to be due to random bugs in the end to end encryption implementations (because I also ran into those when just messing around with the end to end encryption). In any case there should be a big error if this happens. 

1. userA has an account on serverA
2. End2End encryption is enabled on serverA
3. userA setups device1 and enabled end to end encryption. Stores the nonce. Uploads some data. All is good.
4. Now an attacker obtains access to the server, for sake of argument assume there is an evil Admin.
5. They replace the public key of userA with their own
6. userA now setups device2
7, userA enters the nonce
8. userA uploads more data
9. the evil admin now has access to the uploaded data

## Impact

In short it breaks the whole premise of your end to end encryption. An evil admin is able to make the device encrypt to their key.

It is even in the RFC: https://github.com/nextcloud/end_to_end_encryption_rfc/blob/master/RFC.md#further-devices
"Client checks if private key belongs to previously downloaded public certificate."

Recommendations:
1. the clients should verify that the private key matches with the public key and if not  throw a big error

This is especially important because somebody is clearly doing something they are not supposed to if this happens.

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
