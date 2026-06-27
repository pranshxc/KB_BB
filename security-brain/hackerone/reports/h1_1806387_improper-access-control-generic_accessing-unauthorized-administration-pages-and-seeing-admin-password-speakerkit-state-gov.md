---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1806387'
original_report_id: '1806387'
title: Accessing unauthorized administration pages and seeing admin password - speakerkit.state.gov
weakness: Improper Access Control - Generic
team_handle: us-department-of-state
created_at: '2022-12-15T13:18:55.236Z'
disclosed_at: '2023-03-25T13:44:22.594Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 37
asset_identifier: '*.STATE.GOV'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Accessing unauthorized administration pages and seeing admin password - speakerkit.state.gov

## Metadata

- HackerOne Report ID: 1806387
- Weakness: Improper Access Control - Generic
- Program: us-department-of-state
- Disclosed At: 2023-03-25T13:44:22.594Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
- I discovered an issue referred to as no-redirect in a subdomain on state.gov.
When you enter the page, it directs you directly to the entrance. When I examined it via burp suite, it gave 302 found, but the homepage data was showing below.
When I tried it as admin, it still gave 302 found, but this time we could see the content of the admin page.
this way i was able to see admin user and normal user's info.
I was also able to perform many transactions.
uploading files, adding categories and many more.

## Steps To Reproduce:
1- Login to https://speakerkit.state.gov/
- and it will throw you to the page named "spklogin". Using the find and replace feature on burpsuite, I told it to change all requests that gave 302 found to 200 Ok, and I easily performed my operations.
You will be able to do it when you watch the video.

## Supporting Material/References:
https://hackerone.com/reports/1026146
https://hackerone.com/reports/95441

  * [attachment / reference]

{F2078131}
{F2078132}
{F2078133}

* [ poc / video]
████████

## Impact

access the admin page. unauthorized.

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
