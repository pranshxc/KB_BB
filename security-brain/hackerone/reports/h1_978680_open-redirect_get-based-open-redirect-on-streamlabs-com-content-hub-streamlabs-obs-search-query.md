---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '978680'
original_report_id: '978680'
title: GET based Open redirect on [streamlabs.com/content-hub/streamlabs-obs/search?query=]
weakness: Open Redirect
team_handle: logitech
created_at: '2020-09-10T21:28:18.445Z'
disclosed_at: '2020-10-09T22:13:52.657Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 31
asset_identifier: '*.streamlabs.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- open-redirect
---

# GET based Open redirect on [streamlabs.com/content-hub/streamlabs-obs/search?query=]

## Metadata

- HackerOne Report ID: 978680
- Weakness: Open Redirect
- Program: logitech
- Disclosed At: 2020-10-09T22:13:52.657Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Description: in the following link, the parameter `query` is reflecting in multiple places, one of them is in the `<meta>` tag in the head section of the HTML source, the reflection is in the `content` attribute to be precise (check the below image)

{F983200}

And i was able to break out of the `content` attribute and was able to bypass the Cloudflare protection that wouldnt let me to add `http-equiv` attribute by using `%00` char to finally achieve the following redirect using a crafted payload

{F983205}

PoC: `https://streamlabs.com/content-hub/streamlabs-obs/search?query=0;url=https://google.com"%20http-%00equiv="refresh"`
Payload: `0;url=https://google.com/document.cookie"%20http-%00equiv="refresh"` 
Readable payload: `0;url=https://google.com/" http-equiv="refresh"`

## Impact

Open redirect

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
