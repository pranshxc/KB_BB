---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '277502'
original_report_id: '277502'
title: '[BuddyPress 2.9.1] Open Redirect via "wp_http_referer" parameter on "bp-profile-edit"
  endpoint'
weakness: Open Redirect
team_handle: wordpress
created_at: '2017-10-15T20:36:39.950Z'
disclosed_at: '2017-11-02T16:56:46.533Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- open-redirect
---

# [BuddyPress 2.9.1] Open Redirect via "wp_http_referer" parameter on "bp-profile-edit" endpoint

## Metadata

- HackerOne Report ID: 277502
- Weakness: Open Redirect
- Program: wordpress
- Disclosed At: 2017-11-02T16:56:46.533Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

In a similar manner to #228569, it is currently possible to execute authenticated open redirections via the `wp_http_referer` parameter used in the [BuddyPress](https://wordpress.org/plugins/buddypress/) extended user edit screen.

## Proof of concept

Upon accessing the below URL, please select the "Update Profile" button, then select the "**←Back to Users**" link. This will redirect a target to the attacker-specified address (in this case, "google.com").


```
http://instance/wp-admin/users.php?page=bp-profile-edit&wp_http_referer=https://google.com
```

### Supporting evidence

{F229538}

Thanks,

Yasin

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
