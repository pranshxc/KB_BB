---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '130136'
original_report_id: '130136'
title: developer.uber.com/404 and developer.uber.com/docs/404 are susceptible to iframes
team_handle: uber
created_at: '2016-04-12T21:39:17.708Z'
disclosed_at: '2016-06-13T23:00:49.943Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
---

# developer.uber.com/404 and developer.uber.com/docs/404 are susceptible to iframes

## Metadata

- HackerOne Report ID: 130136
- Weakness: 
- Program: uber
- Disclosed At: 2016-06-13T23:00:49.943Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

#Issue
You can iframe the error pages for https://developer.uber.com/404 and https://developer.uber.com/docs/404

#Proof of concept
An example can be found here http://codepen.io/JacobReynolds/pen/VaMbde?editors=1010

#Impact
There is not a large security impact from a cursory glance at the 404 pages.  The docs page has a ReadMe.io login that is accessible in the iframe, but without some pretty clever trickery it would be hard to keylog a user's login info from there.

You are able to redirect in the iframe from /docs/404 to /404 but that is as much movement as you can get within the domains.

#Possible Fixes
Adding the X-Frame-Options:SAMEORIGIN header to the response for both of these pages would be the solution.

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
