---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '238890'
original_report_id: '238890'
title: SAUCE Access_key and User_name leaked in Travis CI build logs
weakness: Information Disclosure
team_handle: algolia
created_at: '2017-06-11T04:40:20.704Z'
disclosed_at: '2017-07-12T15:47:02.929Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# SAUCE Access_key and User_name leaked in Travis CI build logs

## Metadata

- HackerOne Report ID: 238890
- Weakness: Information Disclosure
- Program: algolia
- Disclosed At: 2017-07-12T15:47:02.929Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

hello algolia team,
I founded the SAUCE Access_Key and User_name was leaked in Travis CI build logs of instantsearch.js product [#Line-249-&-250](https://travis-ci.org/algolia/instantsearch.js/builds/225176027#L249).
This can be used to perform every API calls of sauce-lab.(e.g Creating a Sub account. I created a test account for testing. sorry for this ;) ).

You should revoke the access_key and secure the key in Travis Cl build logs.

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
