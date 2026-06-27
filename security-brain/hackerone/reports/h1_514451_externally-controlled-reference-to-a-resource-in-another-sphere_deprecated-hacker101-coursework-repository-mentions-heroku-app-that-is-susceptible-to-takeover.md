---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '514451'
original_report_id: '514451'
title: Deprecated Hacker101 coursework repository mentions Heroku App that is susceptible
  to takeover
weakness: Externally Controlled Reference to a Resource in Another Sphere
team_handle: security
created_at: '2019-03-24T09:01:46.192Z'
disclosed_at: '2019-04-04T19:41:54.301Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 68
asset_identifier: https://ctf.hacker101.com
asset_type: URL
max_severity: low
tags:
- hackerone
- externally-controlled-reference-to-a-resource-in-another-sphere
---

# Deprecated Hacker101 coursework repository mentions Heroku App that is susceptible to takeover

## Metadata

- HackerOne Report ID: 514451
- Weakness: Externally Controlled Reference to a Resource in Another Sphere
- Program: security
- Disclosed At: 2019-04-04T19:41:54.301Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi ,
I'm sure this repo on GitHub `https://github.com/Hacker0x01` belong to `Hackerone,inc`. I've found that your docs on it mention a Heroku app `breaker101.herokuapp.com
` which is no longer work and I could takeover it via HeroKu.

>Suggested Fix : 
Remove this app name from your docs or I can remove it from my apps to added it back to your account 

#`Poc :` 
http://breaker101.herokuapp.com


>Repo https://github.com/Hacker0x01/Hacker101Coursework/blob/master/gae/static/report47.md
{F450943}

## Impact

>New Researchers can be scammed by this app

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
