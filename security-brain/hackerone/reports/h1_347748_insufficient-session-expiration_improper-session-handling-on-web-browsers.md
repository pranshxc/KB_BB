---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '347748'
original_report_id: '347748'
title: Improper session handling on web browsers
weakness: Insufficient Session Expiration
team_handle: x
created_at: '2018-05-05T11:55:53.337Z'
disclosed_at: '2018-06-26T22:00:48.544Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- insufficient-session-expiration
---

# Improper session handling on web browsers

## Metadata

- HackerOne Report ID: 347748
- Weakness: Insufficient Session Expiration
- Program: x
- Disclosed At: 2018-06-26T22:00:48.544Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

**Summary:**  Sessions are not properly logged out/ Information Leak

**Description:** I have two accounts that I control from my mobile Browser , As a concept of Session handling by browsers at a time one can only use one account with proper mapping of session and generated cookies . But when someone send DM or other data for my logged out account i still get  web Notifications , where i can read the DM of that logged out account .
All the Testing is done on Chrome Browser of my phone , I have video for the same

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. login with multiple accounts in Twitter one by one , saving your credentials for future
  2. Enable web push notifications for twitter
  3  now as a normal scenario login to one account and ask your friend to send you DM on 
      account other account which is not logged in
  4 . you can see the DM in the android notifications for websites that saying notification for mobile.twitter.com and DM displayed 

## Impact : session mishandling leading to my private data leak  , on clicking the notification my cookies of one account is being taken with the request for other account 

Moreover i am working on it , hope will help you to get your service better . please revert 



## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, etc.)

## Impact

1 .Session mishandling leading to my private data leak  , 
 2. on clicking the notification my cookies of one account is being taken with the request for other account 
3 . information getting delivered even after the session isnt their can lead to privacy breach

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
