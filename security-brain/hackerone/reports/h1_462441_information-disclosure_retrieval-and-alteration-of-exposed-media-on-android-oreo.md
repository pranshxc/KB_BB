---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '462441'
original_report_id: '462441'
title: Retrieval and alteration of exposed media on Android Oreo
weakness: Information Disclosure
team_handle: nextcloud
created_at: '2018-12-14T13:28:52.663Z'
disclosed_at: '2019-06-26T15:32:46.286Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
asset_identifier: com.nextcloud.client
asset_type: GOOGLE_PLAY_APP_ID
max_severity: medium
tags:
- hackerone
- information-disclosure
---

# Retrieval and alteration of exposed media on Android Oreo

## Metadata

- HackerOne Report ID: 462441
- Weakness: Information Disclosure
- Program: nextcloud
- Disclosed At: 2019-06-26T15:32:46.286Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Good afternoon.

Any media downloaded from the cloud server within the Android app is subject to third party modification and server re-upload without explicit  user consent.

This happens at least on Android Oreo, as data is automatically stored on shared folder /sdcard/Android/media/com.nextcloud.client/nextcloud/ACCOUNT/.

This report could be probably divided in two as one aspect is data confidentially while the other one is data integrity, which could be solved separately.

## Impact

Local media availability  is impacted if device is not web connected as third app can delete any downloaded assets

Local media confidentiality is impacted as any third app can access any downloaded assets, even if  Nextcloud lock is set up.

Local media confidentiality is impacted as any third app can alter any downloaded assets, even if  Nextcloud lock is set up. Once the user open up NC app, content get automatically reuploaded to sever.

As it seems NEW content does not get uploaded nor DELETED content get removed, it seems that Nextcloud app maintain a local sync setup and this setup could be used for metadata control to at least prevent/control data re-upload.

if Nextcloud lock is setup, it would also good to at least provide a minimal confidentiality setup so that data gets encrypted PER default and decrpyted on tmp folder only on click (which is required to open assets with PDF/other app).

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
