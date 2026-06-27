---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '515574'
original_report_id: '515574'
title: Unclaimed Github Repository Takeover on https://www.data.gov/labs
weakness: Phishing
team_handle: gsa_bbp
created_at: '2019-03-26T15:09:35.472Z'
disclosed_at: '2019-07-29T16:54:50.899Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
asset_identifier: www.data.gov
asset_type: URL
max_severity: critical
tags:
- hackerone
- phishing
---

# Unclaimed Github Repository Takeover on https://www.data.gov/labs

## Metadata

- HackerOne Report ID: 515574
- Weakness: Phishing
- Program: gsa_bbp
- Disclosed At: 2019-07-29T16:54:50.899Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Security Team,

I found a Vulnerability in your website where in one of your domain https://www.data.gov/labs
there was Description about Simple API in which two links were pointing to https://simple-api.github.io/api-offices/ but after visiting this URL i got an 404 error where it shown like page not found.

Steps were used to claim these repository :-
1. this domain was available to claim.
2. registered for new github account
3. used username "simple-api"
4. created a master-branch of repository with "api-offices"
5. created a simple index.html file.

## Impact

There is impact where when victim visitor's visit the website they see "Simple API" section for information if they click on below options 
1) Source Code and Documentation
2) Remote Hosted Tool

they will get into attackers repository, and attacker can upload any malicious content on it which can harm your organisation.

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
