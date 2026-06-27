---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '199804'
original_report_id: '199804'
title: Persistent XSS on ForecastApp
weakness: Cross-site Scripting (XSS) - Generic
team_handle: harvest
created_at: '2017-01-20T01:40:05.882Z'
disclosed_at: '2017-03-04T18:13:38.292Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Persistent XSS on ForecastApp

## Metadata

- HackerOne Report ID: 199804
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: harvest
- Disclosed At: 2017-03-04T18:13:38.292Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

When adding a new Person, by inserting this in First or Last Name, I've got a persistent XSS:

<sVg/oNloAd=//><sVg/oNloAd=alert("XSS2")//>

The key for this is that the person with the XSS string must appear in one or more dropdown menus. In other words, the Person must be available to be assigned to at least one project.

I can also trigger the alert box by clicking on Expand All and any time slot where the Person with the XSS string is in the dropdown menu.

This is true for all similar dropdown menus. If I create a Client with the same string, I also get the alert box when creating a New Project since there's a dropdown menu that lists the Clients.

If I create a New Project with the XSS string in Project Name, I can trigger the alert box on the Team's tab in the same way as in the Projects' tab.

Also, by going to https://forecastapp.com/000000/projects and clicking on the malicious project, the alert box is also triggered.

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
