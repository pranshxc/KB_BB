---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1390782'
original_report_id: '1390782'
title: Possible Domain Takeover on AWS Instance.
weakness: Phishing
team_handle: rocket_chat
created_at: '2021-11-03T19:40:16.399Z'
disclosed_at: '2022-05-22T20:18:20.219Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- phishing
---

# Possible Domain Takeover on AWS Instance.

## Metadata

- HackerOne Report ID: 1390782
- Weakness: Phishing
- Program: rocket_chat
- Disclosed At: 2022-05-22T20:18:20.219Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The vulnerable domain possibly available for takeover is:` traefik-livedemo.rocket.chat (CNAME: a0e7eaaaa82f611e9b1cc0e9ccd15f3e-557536140.us-west-2.elb.amazonaws.com)`.
This domain, contains a record pointing to these an WS instance. When querying for any IP under the instance, I got returned an NXDomain error.

Steps to claim the instances:
Log-in or register into AWS. (Region has to be set as us-west-2)
Go onto the "Elastic LoadBalancer" section
Click "Create Loadbalancer"
Click "Application Loadbalancer"
Input the name before the final dash and the numbers. (eg: a0e7eaaaa82f611e9b1cc0e9ccd15f3e )
Deploy it, and check if the numbers are the same.

It might take a few to get the right one, but with an automated script I am certainly sure that it is achievable.

## Impact

The attacker might be able to takeover the domain, and gain access to the domain. An user, recognizing the domain recalling "rocket.chat" would let the user trust the page, and then, give the attacker his credentials via a phishing form.

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
