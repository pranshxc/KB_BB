---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6362'
original_report_id: '6362'
title: Full Path Disclosure on [smarthistory.khanacademy.org]
weakness: Information Disclosure
team_handle: khanacademy
created_at: '2014-04-07T22:22:31.724Z'
disclosed_at: '2014-04-11T19:03:04.152Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Full Path Disclosure on [smarthistory.khanacademy.org]

## Metadata

- HackerOne Report ID: 6362
- Weakness: Information Disclosure
- Program: khanacademy
- Disclosed At: 2014-04-11T19:03:04.152Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello, I have found a full path disclosure on a website that runs a wordpress installation. There isn't much to explain about this bug, as it's pretty self explanatory. What an attack can do with this bug is identify the full path, and the user the site is running under. If the attacker finds a vulnerability where he needs the full path, he can grab it from there.

Here's the proof of concept - http://smarthistory.khanacademy.org/blog/wp-content/plugins/podpress/getid3/write.php

To mitigate this vulnerability, either fix the syntax error, or remove the file if it is not necessary anymore after evaluation. 

Thank you.

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
