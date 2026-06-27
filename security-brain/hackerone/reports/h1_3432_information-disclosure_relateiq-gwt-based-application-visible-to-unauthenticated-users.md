---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '3432'
original_report_id: '3432'
title: RelateIQ GWT based application visible to unauthenticated users
weakness: Information Disclosure
team_handle: relateiq
created_at: '2014-03-07T05:13:07.101Z'
disclosed_at: '2014-04-11T01:54:39.719Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# RelateIQ GWT based application visible to unauthenticated users

## Metadata

- HackerOne Report ID: 3432
- Weakness: Information Disclosure
- Program: relateiq
- Disclosed At: 2014-04-11T01:54:39.719Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

When a legitimate user authenticates to the RelateIQ application, since it is a GWT based application, a request is sent to the URL https://app.relateiq.com/app/app.nocache.js. This detects the browser and then a corresponding request is sent to the URL https://app.relateiq.com/app/3E21F01ECCFB75FE4838912FCE252FA1.cache.html and the response from the server is the entire RelateIQ application obfuscated in javascript rendered on the client side. As long as the user is authenticated to the website, it is acceptable for the server to return the obfuscated javascript of the RelateIQ application. 

However, it was observed that even an unauthenticated attacker can request for the same URL and receive the same obfuscated JavaScript from the server. Since de-obfuscation of this JavaScript is possible, the attacker will then be able to retrieve information about the application itself like the different RPC calls, pages and data residing within the application, functionality logic, etc. which can then be leveraged to exploit other vulnerabilities.

This requirement is clearly stated on the on the GWT Project website and they have also described some of the ways that this can be done here - http://www.gwtproject.org/articles/dynamic_host_page.html

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
