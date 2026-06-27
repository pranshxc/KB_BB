---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '164578'
original_report_id: '164578'
title: Reflected XSS in www.lahitapiola.fi (/cs/Satellite) using Oracle WebCenter
  -page
weakness: Cross-site Scripting (XSS) - Generic
team_handle: localtapiola
created_at: '2016-08-30T23:47:57.307Z'
disclosed_at: '2016-11-17T22:21:50.969Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected XSS in www.lahitapiola.fi (/cs/Satellite) using Oracle WebCenter -page

## Metadata

- HackerOne Report ID: 164578
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: localtapiola
- Disclosed At: 2016-11-17T22:21:50.969Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

There is possible to include HTML/Javascript code in the parameter "destpage" of one of the Fatwire pages.

The affected Fatwire page is: OpenMarket/Xcelerate/UIFramework/LoginError

This allows to launch a reflected XSS attack by creating a simple URL like the following:
https://www.lahitapiola.fi/cs/Satellite?destpage="><h1>xxx<script>alert(111)</script>&pagename=OpenMarket%2FXcelerate%2FUIFramework%2FLoginError

The XSS not persistent, so only users that visit the malicious URL will execute the injected Javascript.

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
