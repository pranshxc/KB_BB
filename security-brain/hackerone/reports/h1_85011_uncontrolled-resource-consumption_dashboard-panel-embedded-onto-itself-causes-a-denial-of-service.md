---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '85011'
original_report_id: '85011'
title: Dashboard panel embedded onto itself causes a denial of service
weakness: Uncontrolled Resource Consumption
team_handle: phabricator
created_at: '2015-08-27T00:09:58.016Z'
disclosed_at: '2015-08-27T01:15:48.225Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Dashboard panel embedded onto itself causes a denial of service

## Metadata

- HackerOne Report ID: 85011
- Weakness: Uncontrolled Resource Consumption
- Program: phabricator
- Disclosed At: 2015-08-27T01:15:48.225Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I know this may not qualify for a bounty since it's a DoS, but I believe you'd rather get sensitive reports through HackerOne rather than Maniphest. (PS: mongoose.)

Steps to reproduce
================
* In Dashboards, create a new **Text Panel** (let's say it would get the object reference `W1` on creation).
* In the **Create New Panel** dialog, embed the panel view onto itself with Remarkup: `{W1}`
* Phabricator should now bravely attempt to render this, and choke.

Impact
======
Significantly disruptive in an install where any user may create a dashboard (I think that's true by default), since they would then be able to embed this eldritch panel in, say, a Maniphest comment, forever ruining rendering for all of task, feed, and likely homepage, views.

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
