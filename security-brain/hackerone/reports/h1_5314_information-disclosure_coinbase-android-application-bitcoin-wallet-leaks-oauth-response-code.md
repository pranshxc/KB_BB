---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '5314'
original_report_id: '5314'
title: Coinbase Android Application - Bitcoin Wallet Leaks OAuth Response Code
weakness: Information Disclosure
team_handle: coinbase
created_at: '2014-03-31T06:12:33.653Z'
disclosed_at: '2014-11-26T21:54:19.265Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- information-disclosure
---

# Coinbase Android Application - Bitcoin Wallet Leaks OAuth Response Code

## Metadata

- HackerOne Report ID: 5314
- Weakness: Information Disclosure
- Program: coinbase
- Disclosed At: 2014-11-26T21:54:19.265Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

There's a simple bug here, the Coinbase Android App. "BitCoin Wallet" leaks the **OAuth** Response Code which can be obtained using `adb logcat -s Coinbase` command line for testing, and any Android application on the same phone can read the response code for the user by reading the logs. As of now nothing can be harmed with OAuth Response code, but along with the hardcoded `client secret` we can obtain the `access_token`.

This bug is similar to this - http://attack-secure.com/all-your-facebook-access-tokens-are-belong-to-us/

So using the stolen response code and `client secret` we can derive the `access_token`

POC: https://www.dropbox.com/s/zionksi1pt7lot5/Coinbase-Android.mov

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
