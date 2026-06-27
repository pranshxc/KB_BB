---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '152586'
original_report_id: '152586'
title: CSRF token fixation in Sign in with Google
weakness: Cross-Site Request Forgery (CSRF)
team_handle: harvest
created_at: '2016-07-20T16:02:35.565Z'
disclosed_at: '2016-10-25T05:06:50.170Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF token fixation in Sign in with Google

## Metadata

- HackerOne Report ID: 152586
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: harvest
- Disclosed At: 2016-10-25T05:06:50.170Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi 
There is CSRF token fixation in Sign in with Google at https://id.getharvest.com/sessions/new

The state parameter is same for any time login
https://id.getharvest.com/oauth2/callback?state=%7B%22intent%22:%22sign-in%22%7D&code={code}

Steps to reproduce
1. Go to https://id.getharvest.com/sessions/new
2. Click sign in with google, and authorise Harvest
3. Capture the request in burp
4. copy the authorization code link https://id.getharvest.com/oauth2/callback?state={"intent":"sign-in"}&code={attackers_code}
5. Open the link in other browser

Reference: https://hackerone.com/reports/55911

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
