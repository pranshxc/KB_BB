---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '180346'
original_report_id: '180346'
title: Nginx server version disclosure on engineeringblog
weakness: Information Disclosure
team_handle: yelp
created_at: '2016-11-05T12:23:04.505Z'
disclosed_at: '2017-11-09T20:10:13.487Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
- information-disclosure
---

# Nginx server version disclosure on engineeringblog

## Metadata

- HackerOne Report ID: 180346
- Weakness: Information Disclosure
- Program: yelp
- Disclosed At: 2017-11-09T20:10:13.487Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi Yelp Team,

I have found a little information disclosure on your system with regards to the version of server you are using, due to not properly handling 404 errors , whe you go to the page that i not existing, the exact nginx version was disclosed.

__PoC URL:__ engineeringblog.yelp.com/test

__PoC Screenshot:__ {F33044}

It is important to keep secret of the exact server versions.

__Mitigation:__

You may want to create a customize 404 error page, or you can just simply remove the nginx server version.

Regards
Japz

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
