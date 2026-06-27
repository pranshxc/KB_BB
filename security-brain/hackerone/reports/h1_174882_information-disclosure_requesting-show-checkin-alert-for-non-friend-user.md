---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '174882'
original_report_id: '174882'
title: Requesting Show CheckIn Alert for Non Friend User
weakness: Information Disclosure
team_handle: yelp
created_at: '2016-10-10T05:54:19.898Z'
disclosed_at: '2016-10-27T18:42:09.172Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- information-disclosure
---

# Requesting Show CheckIn Alert for Non Friend User

## Metadata

- HackerOne Report ID: 174882
- Weakness: Information Disclosure
- Program: yelp
- Disclosed At: 2016-10-27T18:42:09.172Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

During analysis it was observed that I was able to request "ShowCheck In Alert" Request for non friend user.

I performed this application from Mobile application. Below are the steps we have to carry to achieve this:

Logged in to Yelp Mobile Application
Visit any added friend and click on "ShowCheck In Alert" 
It will originate the request from the mobile application. Capture this request and Change the UserID value with any other user non-added friend value. Server sends response with OK message.

Please find attached POC for the same.

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
