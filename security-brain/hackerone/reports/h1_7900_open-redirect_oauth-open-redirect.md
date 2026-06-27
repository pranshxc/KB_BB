---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7900'
original_report_id: '7900'
title: OAuth open redirect
weakness: Open Redirect
team_handle: respondly
created_at: '2014-04-17T19:42:40.444Z'
disclosed_at: '2014-04-22T00:01:46.526Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- open-redirect
---

# OAuth open redirect

## Metadata

- HackerOne Report ID: 7900
- Weakness: Open Redirect
- Program: respondly
- Disclosed At: 2014-04-22T00:01:46.526Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

An attacker can use an open redirect vulnerability in the Twitter OAuth process to redirect someone to his/her webpage, while also obtaining the OAuth token and verifier of the victim. 

The vulnerability is right here: https://app.respond.ly/_oauth/twitter/?requestTokenAndRedirect=https://hackerone.com. When someone authorizes their Twitter account using that URL, the redirect will go to https://hackerone.com.

Recommendation: make sure the `requestTokenAndRedirect` paramater only accepts hosts on whitelisted domains.

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
