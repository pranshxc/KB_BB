---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145517'
original_report_id: '145517'
title: Vulnerable Javascript library
weakness: Information Disclosure
team_handle: nextcloud
created_at: '2016-06-17T18:57:07.847Z'
disclosed_at: '2016-06-17T19:19:22.918Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
- information-disclosure
---

# Vulnerable Javascript library

## Metadata

- HackerOne Report ID: 145517
- Weakness: Information Disclosure
- Program: nextcloud
- Disclosed At: 2016-06-17T19:19:22.918Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Information disclosure:

So from simple lookup you can confirm the version of the jquery used.
And is a outdated one, that accordingly to some research i did, was public vulnerabilities, such as XSS.


Steps to reproduce:
1- navigate to: https://nextcloud.com/introducing-the-nextcloud-bug-bounty-program/
2- see sorce code
3- find /wp-content/cache/minify/000000/hY1BEoJADAQ_hMnKxfdEiFS2dhNNVgt9vYhcKY4zNT2dUHluSBHcAnPgi3U0x2oju8rHTz1cIEEV7RAp0wyT2VSY7hIwWF07LHJd6MeT_Y3nBei38OMgR5d2NNtK9CYqjWNwK2WVHRCVwvT__wU.js
4- navigate to: https://nextcloud.com/wp-content/cache/minify/000000/hY1BEoJADAQ_hMnKxfdEiFS2dhNNVgt9vYhcKY4zNT2dUHluSBHcAnPgi3U0x2oju8rHTz1cIEEV7RAp0wyT2VSY7hIwWF07LHJd6MeT_Y3nBei38OMgR5d2NNtK9CYqjWNwK2WVHRCVwvT__wU.js
5- find: jquery:"1.7.2"

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
