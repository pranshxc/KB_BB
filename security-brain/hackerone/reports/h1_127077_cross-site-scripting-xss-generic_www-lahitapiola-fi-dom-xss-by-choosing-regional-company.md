---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '127077'
original_report_id: '127077'
title: www.lahitapiola.fi DOM XSS by choosing regional company
weakness: Cross-site Scripting (XSS) - Generic
team_handle: localtapiola
created_at: '2016-03-31T09:17:34.671Z'
disclosed_at: '2016-06-01T12:47:58.657Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# www.lahitapiola.fi DOM XSS by choosing regional company

## Metadata

- HackerOne Report ID: 127077
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: localtapiola
- Disclosed At: 2016-06-01T12:47:58.657Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

please check screenshot first.
browser: Chrome(latest) or Internet Explorer 11
steps to reproduce:
- go to page http://www.lahitapiola.fi/henkilo#"><img src=x onerror=alert(1)>
- press `Valitse alueyhtiösi` button
- input zip e.g. 111

vulnerable js code - https://www.lahitapiola.fi/cs/lahitapiola/js/scripts.js

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
