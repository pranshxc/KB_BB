---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '331428'
original_report_id: '331428'
title: Cross domain tracking even with 3rd party cookies disabled.
team_handle: brave
created_at: '2018-03-30T19:15:36.506Z'
disclosed_at: '2018-08-07T22:46:40.235Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
asset_identifier: https://laptop-updates.brave.com/latest/osx
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
---

# Cross domain tracking even with 3rd party cookies disabled.

## Metadata

- HackerOne Report ID: 331428
- Weakness: 
- Program: brave
- Disclosed At: 2018-08-07T22:46:40.235Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Cross domain tracking
Default settings from Brave browser has 3rd party cookies disabled. Which I am assuming also disables 3rd part storage like IndexedDB etc. Because of this protection it is not possible for a 3rd party to track users across multiple domains.

But, Even though third-party cookies is disabled by default using Shared workers, a third-party is able to track the user across domains and websites.

REPRODUCTION STEPS
If you visit the these three pages in three tabs, you will notice that as a third-party it can learn the movement of a user across domains, even though the user has disabled 3rd party cookies.

https://cdn.cliqz.com/browser-f/fun-demo/some-random-page.html
https://cdn2.ghostery.com/browser-f/fun-demo/some-random-page.html

The third party script is being loaded from https://konarkmodi.github.io/

## Impact

Because of this protection it is not possible for a 3rd party to track users across multiple domains. The demo is not very clever, but a 3rd party with a large footprint on the web can use this to track substantial web browsing behaviour of the user.

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
