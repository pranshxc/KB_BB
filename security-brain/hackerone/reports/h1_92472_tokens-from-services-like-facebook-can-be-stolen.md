---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '92472'
original_report_id: '92472'
title: Tokens from services like Facebook can be stolen
team_handle: bumble
created_at: '2015-10-05T20:27:59.489Z'
disclosed_at: '2016-06-03T15:28:12.914Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
---

# Tokens from services like Facebook can be stolen

## Metadata

- HackerOne Report ID: 92472
- Weakness: 
- Program: bumble
- Disclosed At: 2016-06-03T15:28:12.914Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

__Description__

This file https://mus1.badoo.com/cb.html looks for the parameters _access_token_, _token_ and _code_ in the URL and send the value back to the `window.opener` using `window.opener.postMessage(message, '*');`. Because you specified `*` as the value of the second parameter of `postMessage()`, the browser is not going to check which is the opener and will send the message to any opener with the token.
The problem here is that you can receive the message from a site you control and then use this token to even log in Badoo.

__Proof of concept__

1. Download the file _opener.html_ that I attached.
2. Sign up to Badoo using Facebook.
3. Using the browser where you are logged in to Facebook, open the file that you downloaded in step 1.
4. Click on _Click Here_.
5. Wait a few seconds.
6. When it's done, in the page will appear your Facebook token for Badoo.

I attached a screen capture too (the size is 1.4MB).
Please, let me know if you need more information.

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
