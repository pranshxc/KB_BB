---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '435457'
original_report_id: '435457'
title: Ability to login to the Nexus Repo Manager from https://nexus.imgur.com/
weakness: Path Traversal
team_handle: imgur
created_at: '2018-11-07T02:32:40.014Z'
disclosed_at: '2018-12-13T19:02:43.939Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- path-traversal
---

# Ability to login to the Nexus Repo Manager from https://nexus.imgur.com/

## Metadata

- HackerOne Report ID: 435457
- Weakness: Path Traversal
- Program: imgur
- Disclosed At: 2018-12-13T19:02:43.939Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Imgur Administrators,

I am not sure if this falls in your scope but I wanted to alert you that your Nexus Repository Manager can be accessed through https://nexus.imgur.com/
Usually the default user/pass for the NRM are admin/admin123 but there is an alternative way to login using the below default credentials.
user: anonymous
pass: anonymous

I was able to login and I got access to check all the repositories available. I uploaded the attached video as a proof of traversal.
Kindly arrange to remove the user anonymous or change its password & limit the access to the Nexus Repo Manager site https://nexus.imgur.com/

## Impact

The attacker can manage to proxy, collect, and manage your dependencies (delete components & Analyze applications).

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
