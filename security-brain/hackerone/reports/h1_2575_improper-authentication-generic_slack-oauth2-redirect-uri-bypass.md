---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2575'
original_report_id: '2575'
title: Slack OAuth2 "redirect_uri" Bypass
weakness: Improper Authentication - Generic
team_handle: slack
created_at: '2014-03-01T15:12:55.080Z'
disclosed_at: '2014-05-29T22:15:44.983Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- improper-authentication-generic
---

# Slack OAuth2 "redirect_uri" Bypass

## Metadata

- HackerOne Report ID: 2575
- Weakness: Improper Authentication - Generic
- Program: slack
- Disclosed At: 2014-05-29T22:15:44.983Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I've found a way to circumvent redirect_uri restrictions imposed by the web application using domain-suffix/subdomain technique.

I created an OAuth application under https://api.slack.com/applications/new. That has OAuth redirect_uri configured to http://www.google.com.

So technically 

Allowed Request shall be :
https://slack.com/oauth/authorize?client_id=2190698099.2192071336&redirect_uri=http://www.google.com

Denied Request shall be:

https://slack.com/oauth/authorize?client_id=2190698099.2192071336&redirect_uri=http://www.blahblah.com

Surprisingly If I point the redirect_uri to http://www.google.com.mx (see .mx suffix) the endpoint will be accepted, infact endpoint like http://www.google.com.attacker.com will be accepted too. The server doesn't block these suffix attacks.

So attackers can craft an OAuth endpoint like below to circumvent redirect_uri restrictions :

https://slack.com/oauth/authorize?client_id=2190698099.2192071336&redirect_uri=http://www.google.com.mx


Thanks!
Prakhar Prasad

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
