---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '49759'
original_report_id: '49759'
title: Open Redirect leak of authenticity_token lead to full account take over.
weakness: Open Redirect
team_handle: x
created_at: '2015-03-02T01:07:46.725Z'
disclosed_at: '2015-04-03T21:20:11.985Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- open-redirect
---

# Open Redirect leak of authenticity_token lead to full account take over.

## Metadata

- HackerOne Report ID: 49759
- Weakness: Open Redirect
- Program: x
- Disclosed At: 2015-04-03T21:20:11.985Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey guys
URL: https://mobile.twitter.com/messages/follow?recipient=/example.com
when I click 'Follow'
I will send my POST request to https://example.com
witch contains my authenticity_token
that can be used for anything like tweeting, following, sending messages, changing username.,.,.etc
it can be used too to Add a mobile number, and then steal the account by recovering it by the mobile number.
Thank You.

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
