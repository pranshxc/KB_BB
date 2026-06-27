---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1198907'
original_report_id: '1198907'
title: Clickjacking on profile page leading to unauthorized changes
weakness: UI Redressing (Clickjacking)
team_handle: upchieve
created_at: '2021-05-16T17:16:19.440Z'
disclosed_at: '2021-06-15T22:14:43.339Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: app.upchieve.org
asset_type: URL
max_severity: none
tags:
- hackerone
- ui-redressing-clickjacking
---

# Clickjacking on profile page leading to unauthorized changes

## Metadata

- HackerOne Report ID: 1198907
- Weakness: UI Redressing (Clickjacking)
- Program: upchieve
- Disclosed At: 2021-06-15T22:14:43.339Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Any attacker could use iFrame options to connect remotely to the real website, And he can craft his own website using the iFrame options of the specific link and can lead to unauthorized changes if the user will be logged in.

## Steps To Reproduce:
1. Login to https://app.upchieve.org/profile
2. Download the attached file and run it on the same browser 
3. You will see a small window which shows us the profile page, Ive currently set the size to small
4. Attacker can make it bigger and gain info.

## Recommendations for Fixing/Mitigation
Use X-Frame Options in the HTTP Responses of the page, This will help content going straight to user and not a 3rd Party.

## Impact

Unauthorized control

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
