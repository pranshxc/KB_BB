---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '160488'
original_report_id: '160488'
title: stored SELF xss on Basic Google Maps Placemarks Settings plugin
weakness: Cross-site Scripting (XSS) - Generic
team_handle: iandunn-projects
created_at: '2016-08-18T18:03:14.022Z'
disclosed_at: '2016-09-27T21:46:23.112Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# stored SELF xss on Basic Google Maps Placemarks Settings plugin

## Metadata

- HackerOne Report ID: 160488
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: iandunn-projects
- Disclosed At: 2016-09-27T21:46:23.112Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hi Ian,

I have to say, normally I don't report and vendors doesn't accept self xss vulnerabilities as valid, but I'm encouraged by #9375
So, I'm reporting this. 

Placemark title field is NOT sanitizing the user input properly. 
I've updated wordpress to latest, and checked your plugin's versiyon from SVN also, it is latest, too. You can confirm in the attached PoC Screenshots.
Thanks for giving opportunity to test your plugins! Keep up good work.

If you don't find this report useful for you, you can just close it as informative or whatever you like.

Regards

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
