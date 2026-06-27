---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '166682'
original_report_id: '166682'
title: Denial of Service through set_preference.json
weakness: Uncontrolled Resource Consumption
team_handle: keybase
created_at: '2016-09-07T21:44:37.372Z'
disclosed_at: '2016-10-07T21:49:39.330Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Denial of Service through set_preference.json

## Metadata

- HackerOne Report ID: 166682
- Weakness: Uncontrolled Resource Consumption
- Program: keybase
- Disclosed At: 2016-10-07T21:49:39.330Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey there,

When selecting an image at `https://keybase.io/_/api/1.0/image/set_preference.json`, passing an invalid value in `identity_src` knocks the server down for 20-30 seconds, with just one request. I have verified this by visiting an external website that checks if a website is down.

POC:

1. Connect either your twitter or github account with Keybase.
2. Select to edit your profile image, and select one of the images.
3. Repeat the request, such as in BurpSuite. Pass in a value to replacing `identity_src`. To prevent keeping the server down, I have only tried two values, `1043` and `http://google.com`. The server will error with 503 and will be down for 20-30 seconds. I have attached a screenshot from http://downoruprightnow.com/ verifying that the site is down.

Please let me know if you need any more information.

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
