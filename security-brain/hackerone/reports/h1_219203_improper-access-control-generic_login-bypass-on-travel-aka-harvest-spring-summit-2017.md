---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '219203'
original_report_id: '219203'
title: Login bypass on travel.██████████ aka "Harvest Spring Summit 2017"
weakness: Improper Access Control - Generic
team_handle: harvest
created_at: '2017-04-07T02:59:18.271Z'
disclosed_at: '2017-04-10T17:18:11.334Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- improper-access-control-generic
---

# Login bypass on travel.██████████ aka "Harvest Spring Summit 2017"

## Metadata

- HackerOne Report ID: 219203
- Weakness: Improper Access Control - Generic
- Program: harvest
- Disclosed At: 2017-04-10T17:18:11.334Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

# Introduction
I stumbled upon http://travel.████. It looks like the portal for Harvest Spring Summit 2017 travel planning and announcement. I was able to gain access to this portal and view the travel itineraries of some of the summit's participants.

**A note on scope**
I realize this domain is not listed in the scope section, but figured it would be something you want to know about as it discloses some personal information about your employees as well as their travel schedules.

# Steps to reproduce
* Head over to http://travel.██████
* Sign in with a random Slack account. I signed in with my test Slack account `hack-test-team.slack.com`.
* You'll be redirected to the Schedule page. Click on //Everyone// to see everyone's travel schedules. 

# Proof of concept
Here's a screenshot:
{F173937}

Note that it was also possible to create a new itinerary for myself:
{F173938}

# Recommendation
Ensure that whoever authenticates via Slack is a member of the `harvest.slack.com` team, and not just any random Slack instance.

Finally, I hope y'all had a great time at the summit! I won't be expecting a fast response on this one as it looks like many of you will be on your way back. =P

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
