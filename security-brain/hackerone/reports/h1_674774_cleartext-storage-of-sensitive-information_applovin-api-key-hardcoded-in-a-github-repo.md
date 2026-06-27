---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '674774'
original_report_id: '674774'
title: AppLovin API Key hardcoded in a Github repo
weakness: Cleartext Storage of Sensitive Information
team_handle: x
created_at: '2019-08-16T00:26:53.604Z'
disclosed_at: '2019-09-18T22:01:53.543Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
asset_identifier: mopub.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cleartext-storage-of-sensitive-information
---

# AppLovin API Key hardcoded in a Github repo

## Metadata

- HackerOne Report ID: 674774
- Weakness: Cleartext Storage of Sensitive Information
- Program: x
- Disclosed At: 2019-09-18T22:01:53.543Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,
I found a Sensitive Data Exposure in github/mopub-android-mediation project, the AppLovin UI API key is hardcoded in source code. 

And in the comment it's mentioned that 
##"This is a unique SDK Key from AppLovin. Get yours from the AppLovin UI".

Github Link:- https://github.com/mopub/mopub-android-mediation/blob/72804166ec9f3b79cc0dcfa96bd8c813f3252794/Testing/src/main/AndroidManifest.xml#L60

Google Ads SDK reference link:- https://developers.google.com/admob/android/mediation/applovin

Thanks
Anshuman Pattnaik

## Impact

So if it's a production API key then it shouldn't be shown publicly in Github repo otherwise it can be used by other developers as it's a company property the API key should be secure as it's a monetize API key.

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
