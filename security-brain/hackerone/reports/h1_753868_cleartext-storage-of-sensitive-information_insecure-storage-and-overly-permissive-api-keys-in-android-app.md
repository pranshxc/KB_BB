---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '753868'
original_report_id: '753868'
title: Insecure Storage and Overly Permissive  API Keys in Android App
weakness: Cleartext Storage of Sensitive Information
team_handle: zenly
created_at: '2019-12-08T06:22:37.354Z'
disclosed_at: '2020-04-12T18:32:21.784Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 45
asset_identifier: app.zenly.locator
asset_type: GOOGLE_PLAY_APP_ID
max_severity: critical
tags:
- hackerone
- cleartext-storage-of-sensitive-information
---

# Insecure Storage and Overly Permissive  API Keys in Android App

## Metadata

- HackerOne Report ID: 753868
- Weakness: Cleartext Storage of Sensitive Information
- Program: zenly
- Disclosed At: 2020-04-12T18:32:21.784Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

#Description:
Most often Developers for their ease of use,leave API keys and some sensitive keys ,Tokens as hardcoded strings,which isn't really a good ideas as it can result in Leaks of sensitive information getting in Wrong Hands which indeed can results in Data theft and Tampering with how the application deals with the data, and API requests the application Makes.

==I found a bunch of API keys,Tokens.==

#To Check API keys leaks Sensitive Information or not
https://github.com/streaak/keyhacks

#Steps to reproduce.
1.Decomiple the app.
2.Look for sensitive information


#Proof of Concept:
Screenshots has been attached as a proof of concept.

## Impact

If an attacker decompiles your apk, and extracts your token, they can indeed maliciously send traffic on your behalf.
This is the case with pretty much every single one of the web  companies out there (google included).
The main thing to know however, is that it is rarely useful for people to do this. Polluting someone else's data  while possible, isn't exactly a profitable thing to do. You can also create server-side filters to help prevent this thing from happening.

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
