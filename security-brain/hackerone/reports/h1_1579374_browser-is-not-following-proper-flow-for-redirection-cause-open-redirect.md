---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1579374'
original_report_id: '1579374'
title: Browser is not following proper flow for redirection cause open redirect
team_handle: brave
created_at: '2022-05-24T03:44:18.233Z'
disclosed_at: '2022-06-30T17:45:11.059Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 40
asset_identifier: https://laptop-updates.brave.com/latest/winx64
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
---

# Browser is not following proper flow for redirection cause open redirect

## Metadata

- HackerOne Report ID: 1579374
- Weakness: 
- Program: brave
- Disclosed At: 2022-06-30T17:45:11.059Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Brave browser is not following proper flow for redirection. Browser is directly redirecting to the site that is present in redirect parameter without confirming from the main site server.
I have found this vulnerability and this is affecting Facebook. Facebook use ```l.facebook.com/l.php?u=<redirect_site>``` for redirection and when server gets the request it check whether the redirect_site is in the list of there malicious(linkshim) list or not. If not then Facebook redirect  it properly.
But when we try to go to a site like https://l.facebook.com/l.php?u=https://test.facebook-whitehat.com/ then brave browser is directly requesting to https://test.facebook-whitehat.com/ (a domain resticted by facebook which can be used for testing prepose) without asking Facebook server  whether should I redirect or not. But other browser are properly following the flow. 

## Products affected: 

 Windows 11, Version 1.38.119 Chromium: 101.0.4951.67 (Official Build) (64-bit)

## Steps To Reproduce:

1. Open brave browser in windows
2.  Intercept the requests
3. Go to ```https://l.facebook.com/l.php?u=https://test.facebook-whitehat.com/``` and you will notice that it directly generating a request ```https://test.facebook-whitehat.com/``` not to ```l.facebook.com```

## Supporting Material/References:

 I also soon how other browser is responding and how brave is responder. POC video attached

## Impact

Brave has seen a massive growth in 2021 quarter and Facebook is the one of the largest used social media.
Due to this vulnerability users that are using Brave browser are directly affected which will affect brave reputation as only brave browser users are getting affect.
As well  this vulnerability in brave browser is affecting facebook's security also.

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
