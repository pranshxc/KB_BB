---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '101063'
original_report_id: '101063'
title: Drivers can change profile picture
weakness: Improper Authentication - Generic
team_handle: uber
created_at: '2015-11-23T08:29:58.844Z'
disclosed_at: '2016-05-12T07:11:49.140Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# Drivers can change profile picture

## Metadata

- HackerOne Report ID: 101063
- Weakness: Improper Authentication - Generic
- Program: uber
- Disclosed At: 2016-05-12T07:11:49.140Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Riders are able to change their profile picture whenever they want and they should be allowed to either way.

When a rider becomes a driver they should not be able to change their profile picture due to the fact they can change their pictures to something inappropriate.

Replicate:
Login into the Uber Rider app with your driver information (which should be the same as rider either way)
Go to Settings
Edit Account (Put in password)
Change Photo - Press Save
             An error will occur saying "Failed to update account details" but the new picture will be applied

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
