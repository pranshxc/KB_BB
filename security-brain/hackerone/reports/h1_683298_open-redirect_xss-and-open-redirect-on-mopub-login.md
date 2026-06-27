---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '683298'
original_report_id: '683298'
title: XSS and Open Redirect on MoPub Login
weakness: Open Redirect
team_handle: x
created_at: '2019-08-27T23:07:07.662Z'
disclosed_at: '2019-09-24T23:18:02.369Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 233
asset_identifier: mopub.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- open-redirect
---

# XSS and Open Redirect on MoPub Login

## Metadata

- HackerOne Report ID: 683298
- Weakness: Open Redirect
- Program: x
- Disclosed At: 2019-09-24T23:18:02.369Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** I found open redirect at the MoPub login page, https://app.mopub.com/login?next=https://google.com. It also allows javascript URIs, leading to XSS.


**Description:** You can modify the "next" URL parameter to redirect to any website upon logging in on MoPub. 

## Steps To Reproduce:

1. Take this URL: https://app.mopub.com/login?next=https://google.com
2. Change "https://google.com" to whatever URL you want to redirect to.
3. Visit the URL and login
4. You will be redirected to that site

## Impact: Outlined in Impact section below

## Supporting Material/References:

Here's a proof of concept using the URL javascript:alert("proof of concept"):
{F568245}

## Impact

An attacker could use this for phishing, cookie jacking, etc. since it allows javascript URIs and therefore XSS vectors. Additionally, they could use URL encoding to hide the URL that the victim is being redirected to.

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
