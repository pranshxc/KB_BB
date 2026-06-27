---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1929915'
original_report_id: '1929915'
title: Bypass for forced re-authentication upon biometrics change
weakness: Improper Authentication - Generic
team_handle: bitwarden
created_at: '2023-04-02T15:27:18.132Z'
disclosed_at: '2023-07-19T10:47:50.062Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 28
asset_identifier: com.x8bit.bitwarden
asset_type: GOOGLE_PLAY_APP_ID
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Bypass for forced re-authentication upon biometrics change

## Metadata

- HackerOne Report ID: 1929915
- Weakness: Improper Authentication - Generic
- Program: bitwarden
- Disclosed At: 2023-07-19T10:47:50.062Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Verified in Android, might also apply for iOS
This description requires 2 accounts, here called the primary and the secondary vault. 

1. Sign in to the Bitwarden app with the primary account and enable biometric unlock
2. Make sure the app is locked (e.g. by force killing the app)
3. Enroll a new fingerprint
4. As per [GH-1026](https://github.com/bitwarden/mobile/pull/1026), `BiometricIntegrityValid` will now be false and hence the app will display "Biometric unlock disabled pending verification of master password"
5. Add the secondary account following the regular procedure (and enable biometric unlock)
6. Attempt to switch to the primary vault; note that it still does not allow biometric unlock
7. Force kill the app making sure both vaults are locked
8. Switch back to the secondary vault and unlock it
9. From the secondary vault, switch to the primary vault and note how it is possible to unlock it using biometrics

## Impact

Changing biometric options, for example enrolling extra fingerprints should prompt for re-authentication according to the integrity checks implemented in [GH-1026](https://github.com/bitwarden/mobile/pull/1026) and [GH-1093](https://github.com/bitwarden/mobile/pull/1093).

This vulnerability allows bypassing those integrity checks if the following three conditions are met:
1. The attacker has physical access to the phone and is able to unlock the phone
2. The user has enabled biometrics unlock
3. The attacker has any valid Bitwarden account (including selfhosted)

Upon gaining access to the vault, export is not possible because the master password is required, but it is possible to view and delete all passwords the user has access to. It is also possible to enable device login if that was not enabled yet and gain access to the vault on a desktop computer.

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
