---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '123748'
original_report_id: '123748'
title: Not Using Secure Flag Option on Cookies Could Lead to a Man in the Middle Session
  Highjacking
weakness: Improper Authentication - Generic
team_handle: veris
created_at: '2016-03-17T01:15:43.390Z'
disclosed_at: '2016-03-17T13:49:12.570Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# Not Using Secure Flag Option on Cookies Could Lead to a Man in the Middle Session Highjacking

## Metadata

- HackerOne Report ID: 123748
- Weakness: Improper Authentication - Generic
- Program: veris
- Disclosed At: 2016-03-17T13:49:12.570Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,
I noticed that your cookies are stored in plain text, without a secure flag option. As a result, if a user is logged and visits http://sandbox.veris.in/portal/, the cookies with the uid and user token are submitted.

If a malicious attacker was on the same network and managed to get a legitimate user to visit the non-secure version of the site, they would be able to intercept the two values which enables them to take over their session.

I've included a POC video, unlisted, on YouTube.  In it, you'll see I am using Chrome on the left, logged in as a legitimate user. I visit the http version of the site and receive the redirect. Using chrome tools, I can see the cookies being sent - this is meant to simulate was a man in the middle attack would accomplish.

Then, with those values, I open up firefox and an existing session I have with another account. I modify my cookies with the stolen values and I am now logged in as the victim.

POC video: https://youtu.be/KiJtsDosGT8

Please let me know if you have any questions.
Pete

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
