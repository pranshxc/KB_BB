---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '200079'
original_report_id: '200079'
title: Critical information disclosure at https://█████████
weakness: Information Disclosure
team_handle: deptofdefense
created_at: '2017-01-21T00:24:00.149Z'
disclosed_at: '2019-12-02T18:35:17.934Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- information-disclosure
---

# Critical information disclosure at https://█████████

## Metadata

- HackerOne Report ID: 200079
- Weakness: Information Disclosure
- Program: deptofdefense
- Disclosed At: 2019-12-02T18:35:17.934Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

There is a critical information disclosure at https://████████/rserver/rdPage.aspx?rdReport=db_Dashboard&rdShowModes=

**Description:**

As you can see in the video the  https://████████/rserver/rdPage.aspx?rdReport=db_Dashboard&rdShowModes= loads a page with a debug this page functions enabled, which gives the user access to server side information such some sql structure, the path to the webroot  plus some other information.

POC video : 
https://█████


## Impact

The impact here can be great, since the user have access to sql structure.

## Step-by-step Reproduction Instructions

1. Log in to the application and open the following link:  https://██████/rserver/rdPage.aspx?rdReport=db_Dashboard&rdShowModes=

## Product, Version, and Configuration (If applicable)

Tested on firefox latest version

## Suggested Mitigation/Remediation Actions

Reference: https://www.owasp.org/index.php/Full_Path_Disclosure

**Mitigation**

Turn of the debugger trace report or limit the access only to administrator

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
