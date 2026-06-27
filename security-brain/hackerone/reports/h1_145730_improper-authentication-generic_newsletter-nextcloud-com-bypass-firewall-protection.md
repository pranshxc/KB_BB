---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145730'
original_report_id: '145730'
title: 'newsletter.nextcloud.com: Bypass firewall protection'
weakness: Improper Authentication - Generic
team_handle: nextcloud
created_at: '2016-06-18T17:37:03.322Z'
disclosed_at: '2016-07-18T22:01:23.434Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# newsletter.nextcloud.com: Bypass firewall protection

## Metadata

- HackerOne Report ID: 145730
- Weakness: Improper Authentication - Generic
- Program: nextcloud
- Disclosed At: 2016-07-18T22:01:23.434Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Security team,

I would like to report a vulnerability bypass firewall.
when you are trying to navigate this  [link](https://newsletter.nextcloud.com/admin) it needs authentication
but it’s possible to access to admin panel when you add `index.php` after `/admin/`.
`https://newsletter.nextcloud.com/admin/index.php`

P.o.C : video in attachment.

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
