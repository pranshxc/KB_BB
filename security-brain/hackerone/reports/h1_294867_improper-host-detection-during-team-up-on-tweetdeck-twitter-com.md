---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '294867'
original_report_id: '294867'
title: Improper Host Detection During Team Up  on tweetdeck.twitter.com
team_handle: x
created_at: '2017-12-04T05:05:34.028Z'
disclosed_at: '2018-01-04T02:38:38.801Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# Improper Host Detection During Team Up  on tweetdeck.twitter.com

## Metadata

- HackerOne Report ID: 294867
- Weakness: 
- Program: x
- Disclosed At: 2018-01-04T02:38:38.801Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi

Give this url ```https://twitter.com/teams/authorize?target_screen_name=&authorize_callback=https%3A%2F%2F%0Agoogle.com%5C@x.twitter.com``` to any authorised user for team up and after authorization of his 2nd account he will be redirected to ```google.com``` .

First I tried to make it malicious  with adding ```%0Agoogle.com%5C@x``` but it not redirected me but after adding %0Agoogle.com%5C@x```.twitter.com``` in it, this redirected me to google.com. Which shows in this endpoint url isn't properly validating the Host after login.


Vulnerable Url: ```https://twitter.com/teams/authorize?target_screen_name=&authorize_callback=https%3A%2F%2F%0Agoogle.com%5C@x.twitter.com```

Malicious point: ```%0Agoogle.com%5C@x.twitter.com```

PoC video attached

With Best Regards

## Impact

Impact: Attacker can use this for tricking users to Phising attacks.

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
