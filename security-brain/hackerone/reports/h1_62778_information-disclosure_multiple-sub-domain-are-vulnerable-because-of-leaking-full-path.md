---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '62778'
original_report_id: '62778'
title: Multiple sub domain are vulnerable because of leaking full path
weakness: Information Disclosure
team_handle: udemy
created_at: '2015-05-17T11:19:24.731Z'
disclosed_at: '2015-06-25T09:37:42.037Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Multiple sub domain are vulnerable because of leaking full path

## Metadata

- HackerOne Report ID: 62778
- Weakness: Information Disclosure
- Program: udemy
- Disclosed At: 2015-06-25T09:37:42.037Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

At the following address i have found debug.log file disclose the application full path onthe server.

https://business.udemy.com/wp-content/debug.log

http://about.udemy.com/wp-content/debug.log

THe below URLs showing the version number of the application :

http://about.udemy.com/readme.html

http://about.udemy.com/wp-content/plugins/all-in-one-seo-pack/readme.txt

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
