---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '49170'
original_report_id: '49170'
title: Information disclosure - emails disclosed in response > staging.seatme.us
weakness: Cross-Site Request Forgery (CSRF)
team_handle: yelp
created_at: '2015-02-25T14:06:51.368Z'
disclosed_at: '2017-05-11T11:32:43.440Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Information disclosure - emails disclosed in response > staging.seatme.us

## Metadata

- HackerOne Report ID: 49170
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: yelp
- Disclosed At: 2017-05-11T11:32:43.440Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,
I found a  info disclosure vulnerability. We can enumerate emails via user_id parameter from Manage users.

And I found that :

>ID 1 is ██████
ID 514755 is ████████
ID 514775 is █████
ID 514764 is ███████

I attached photos from burp repeater to be more explicit.

We can easily bruteforce user_id parameter with ids to harvest user's emails.


Regards,
  Florin

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
