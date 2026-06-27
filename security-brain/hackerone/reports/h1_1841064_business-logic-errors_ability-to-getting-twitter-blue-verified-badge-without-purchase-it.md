---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1841064'
original_report_id: '1841064'
title: Ability to getting Twitter Blue verified badge without purchase it
weakness: Business Logic Errors
team_handle: x
created_at: '2023-01-20T00:58:13.433Z'
disclosed_at: '2024-02-22T21:13:19.894Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 60
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Ability to getting Twitter Blue verified badge without purchase it

## Metadata

- HackerOne Report ID: 1841064
- Weakness: Business Logic Errors
- Program: x
- Disclosed At: 2024-02-22T21:13:19.894Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

**Summary:** 

Hi there. In this report, I submit a bug about getting Twitter Blue verified badge without purchasing it. 

## Steps To Reproduce:

1. First, you should buy a Twitter Blue subscription for your account. 
2. Change the profile photo of your Twitter account 1 day before your Twitter Blue subscription expires.
3. Check your Twitter profile and ensure your verified badge is gone for review by the Twitter team. (note that, this review will take 1-2 days but it might be good to check from time to time if your account has been reviewed - if it's reviewed and your verified badge is there, you should change again your profile picture before your Twitter Blue subscription is expired)
4. Go to the `App Store` -> `Your App Store Account` > `Subscriptions` section and cancel your Twitter Blue subscription.
5. You should wait one day for your subscription to expire. (please read the note written in step 3)
6. After the subscription expired, try change to your account details if your verified badge still is not there. You'll get a message about your Twitter account is still under review.

Now you have to wait for 2-3 days (no eta about review times but it takes at least 3 days) then the Twitter team will give back your verified badge even your Twitter Blue subscription is expired.

## Impact: 

This can harm financial damages to the Twitter team, and malicious actors can't be tracked since they do not pay for the Blue subscription. 

## Supporting Material/References:

I recorded this video on PC, and showed that I can't edit any new tweet and I'm no longer a Twitter Blue subscriber :

███

I recorded this video on my iPhone device, and showed that I can't edit any new tweet, I'm no longer a Twitter Blue subscriber and went to my Subscriptions section on App Store to show my Twitter Blue subscription is ended on January 13 2023  :

█████

## Impact

This can harm financial damages to Twitter, Inc., and malicious actors can't be tracked since they do not pay for the Blue subscription.

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
