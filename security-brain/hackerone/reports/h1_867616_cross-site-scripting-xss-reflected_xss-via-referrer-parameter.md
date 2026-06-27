---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '867616'
original_report_id: '867616'
title: XSS via referrer parameter
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: x
created_at: '2020-05-07T06:05:49.797Z'
disclosed_at: '2020-10-26T16:11:27.433Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 121
asset_identifier: twitterflightschool.com
asset_type: URL
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS via referrer parameter

## Metadata

- HackerOne Report ID: 867616
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: x
- Disclosed At: 2020-10-26T16:11:27.433Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

# Description
Hi, i would like to report an XSS via `javascript` scheme in `https://www.twitterflightschool.com/student/award/[ID]?referer=`, the payload e need just a click of user to be triggered because the link will be placed in `a` tag.

url:`https://www.twitterflightschool.com/student/award/███?referer=javascript:alert(document.domain)`

I attached a video demonstration:
{F818801}

# Steps to reproduce
1. go to `https://www.twitterflightschool.com/student/award/████████?referer=javascript:alert(document.domain)`
2. click in "X" button in top left of the screen
3. XSS will be triggered

## Impact

it is possible to perform malicious actions on the victim's account

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
