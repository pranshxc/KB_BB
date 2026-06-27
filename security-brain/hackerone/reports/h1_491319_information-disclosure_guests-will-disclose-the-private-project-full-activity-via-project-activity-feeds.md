---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '491319'
original_report_id: '491319'
title: Guests Will Disclose the Private Project Full Activity Via Project Activity
  Feeds
weakness: Information Disclosure
team_handle: gitlab
created_at: '2019-02-05T11:30:59.833Z'
disclosed_at: '2019-02-08T11:45:12.654Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 5
asset_identifier: gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Guests Will Disclose the Private Project Full Activity Via Project Activity Feeds

## Metadata

- HackerOne Report ID: 491319
- Weakness: Information Disclosure
- Program: gitlab
- Disclosed At: 2019-02-08T11:45:12.654Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hello!

Here guests will disclose the complete activity of the project via feeds

##Reproduction Steps:

Create Private Project.

Invite Attacker as Guest.

Next attacker will go to https://gitlab.com/victimyoursz/helloproject/activity

and he access the feeds link

https://gitlab.com/victimyoursz/helloproject.atom?feed_token=FeRKF1AafTSJiLzJ5EyX


It Contains sensitive data i.e activity of the private project it can be disclosed by Guests.

###Here main thing is If guests distribute this links any unauthorized users can access this private project activity.


{F418246}

## Impact

Guests will disclose the private project activity via feeds.

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
