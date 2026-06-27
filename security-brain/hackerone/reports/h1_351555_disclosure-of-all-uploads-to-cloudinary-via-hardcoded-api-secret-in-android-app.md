---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '351555'
original_report_id: '351555'
title: Disclosure of all uploads to Cloudinary via hardcoded api secret in Android
  app
team_handle: reverb
created_at: '2018-05-14T18:04:19.725Z'
disclosed_at: '2018-09-08T14:51:22.220Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 85
asset_identifier: sandbox.reverb.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Disclosure of all uploads to Cloudinary via hardcoded api secret in Android app

## Metadata

- HackerOne Report ID: 351555
- Weakness: 
- Program: reverb
- Disclosed At: 2018-09-08T14:51:22.220Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi, in file ``` com/reverb/app/CloudinaryFacade.java ``` you have hardcoded the following config:
```java
private static final java.lang.String CONFIG = "cloudinary://434762629765715:█████@reverb";
```
where ``` 434762629765715:████████ ``` is basic auth details.

It shouldn't be disclosed to third parties as official docs say (https://github.com/cloudinary/cloudinary_android):
> Note: You should only include the ``` cloud_name ``` in the value, the api secret and key should be left out of the application.

I was able to access your account data
{F297519}
{F297520}

Those keys give me ability to not only access the files, but also replace and delete them, change different their settings. Also this url https://api.cloudinary.com/v1_1/reverb/usage discloses statistics regarding stored files
```json
"requests":1894689201,
"resources":36029794,
"derived_resources":256178843
```

## Impact

Disclosure of all uploads to Cloudinary via hardcoded api secret in Android app

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
