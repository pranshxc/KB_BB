---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '98432'
original_report_id: '98432'
title: 'Urgent : Disclosure of all the apps with hash ID in mopub through API request
  (Authentication bypass)'
weakness: Improper Authentication - Generic
team_handle: x
created_at: '2015-11-07T12:09:46.724Z'
disclosed_at: '2016-08-22T18:23:13.469Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- improper-authentication-generic
---

# Urgent : Disclosure of all the apps with hash ID in mopub through API request (Authentication bypass)

## Metadata

- HackerOne Report ID: 98432
- Weakness: Improper Authentication - Generic
- Program: x
- Disclosed At: 2016-08-22T18:23:13.469Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

This looks like a very critical issue so you should fix it ASAP.

Steps to reproduce :
1.Go to your mopub account and create a segment in your network.
2.You will get a segment ID now.
3.Now Go to the API link : https://app.mopub.com/networks/v2/api/segment/[Segment_id]
Note : page will take lot of time to open and your browser may crash because the response will have all the Apps in mohub with there hash key.
4.When the page will be opened you can see all the Apps in App section.

Providing the video POC for more understanding :
https://youtu.be/QiiEiEeErGU

Kindly Fix the issue ASAP and Let me know if you need any other help from my side.
Best Regards !
Vijay Kumar

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
