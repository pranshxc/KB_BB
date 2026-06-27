---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '111968'
original_report_id: '111968'
title: Interstitial redirect bypass / open redirect in https://hackerone.com/zendesk_session
weakness: Open Redirect
team_handle: security
created_at: '2016-01-21T04:41:43.042Z'
disclosed_at: '2016-02-24T10:55:14.479Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 23
tags:
- hackerone
- open-redirect
---

# Interstitial redirect bypass / open redirect in https://hackerone.com/zendesk_session

## Metadata

- HackerOne Report ID: 111968
- Weakness: Open Redirect
- Program: security
- Disclosed At: 2016-02-24T10:55:14.479Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi guys , I have found a way to use the open redirect vulnerability that zendesk refused to fix and we discussed it in #101146 to bypass intristial redirect. 
in #101146 , @bencode said : 
> I tend to agree with Zendesk, we don't really see any security issues with it. We use our interstitial to warn the user and it's clear you are on a separate site.

Well , using this issue I could bypass the interstitial redirect.
#PoC:
[Clicking here will bypass interistial redirect and get you on evil.com](https://hackerone.com/zendesk_session?locale_id=1&return_to=https://support.hackerone.com/ping/redirect_to_account?state=compayn:/)
 
The link is `https://hackerone.com/zendesk_session?locale_id=1&return_to=https://support.hackerone.com/ping/redirect_to_account?state=compayn:/` which is used to redirect to generate a zendesk session.
This can be fixed from your end , by detecting the `/ping/redirect_to_account` in the `return_to` parameter. 
Thanks

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
