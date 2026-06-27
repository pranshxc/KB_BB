---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '292457'
original_report_id: '292457'
title: Reflected XSS in www.dota2.com
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: valve
created_at: '2017-11-22T20:40:21.090Z'
disclosed_at: '2018-05-09T17:39:38.711Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 29
asset_identifier: www.dota2.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS in www.dota2.com

## Metadata

- HackerOne Report ID: 292457
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: valve
- Disclosed At: 2018-05-09T17:39:38.711Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi guys,

##Description
I found another XSS in www.dota2.com. This time it is located in **http://www.dota2.com/international/live/5/5/1**. However it seems that when you can change the /5/5 folders to any other number (to confirm) and it still worked. I tested this on http://www.dota2.com/international/live/1/1/1 and with other random digits.

##Steps to reproduce
1. Using any browser (except IE), go to
`www.dota2.com/international/live/5/5/1})}});alert(document.cookie);(test=>{{({<!--`
2. You'll see an alert box with your cookie.

I was able to confirm the XSS works in Firefox, Chrome and Opera so the payload successfully bypasses the Chrome XSS filter since the reflection point is directly in a javascript.

{F241581}

## Impact

As you know, with a reflected XSS, a malicious user could trick a user into browsing to a URL which would trigger the XSS and steal the user's cookie, capture keyboard strokes, etc and eventually take over a user's account. 

Thanks,

JR0ch17

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
