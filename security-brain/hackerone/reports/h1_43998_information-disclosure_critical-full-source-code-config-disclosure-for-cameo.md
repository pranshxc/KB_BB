---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '43998'
original_report_id: '43998'
title: CRITICAL full source code/config disclosure for Cameo
weakness: Information Disclosure
team_handle: vimeo
created_at: '2015-01-16T07:43:31.882Z'
disclosed_at: '2015-05-11T08:07:15.130Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- information-disclosure
---

# CRITICAL full source code/config disclosure for Cameo

## Metadata

- HackerOne Report ID: 43998
- Weakness: Information Disclosure
- Program: vimeo
- Disclosed At: 2015-05-11T08:07:15.130Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi!

The server at https://ci.cameo.tv/ has directory listing on and seems to host quiet a few debian packages containing extremely sensitive information (database paswords, API keys, you name it). One example is the config package containing 16 config files, even personal ones containing local passwords etc.

I think it's pretty obvious but you need to **IMMEDIATELY** remove the possibility to access this server from the internet. I also think that you should check your logs for this server, and consider changing all the passwords possibly leaked.

Mathias

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
