---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '12454'
original_report_id: '12454'
title: Browser cross-site scripting filter misconfiguration
weakness: Violation of Secure Design Principles
team_handle: reddapi
created_at: '2014-05-18T13:09:39.511Z'
disclosed_at: '2014-10-28T16:47:01.628Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# Browser cross-site scripting filter misconfiguration

## Metadata

- HackerOne Report ID: 12454
- Weakness: Violation of Secure Design Principles
- Program: reddapi
- Disclosed At: 2014-10-28T16:47:01.628Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Issue detail :-
No X-XSS-Protection header was set in the response. This means that the browser uses default behaviour that detection of a cross-site scripting attack never prevents rendering.

Remediation detail
The following header should be set:

X-XSS-Protection: 1; mode=block

Issue background :-
Cross-site scripting (XSS) filters in browsers check if the URL contains possible harmful XSS payloads and if they are reflected in the response page. If such a condition is recognized, the injected code is changed in a way, that it is not executed anymore to prevent a succesful XSS attack. The downside of these filters is, that the browser has no possibility to distinguish between code fragments which were reflected by a vulnerable web application in an XSS attack and these which are already present on the page. In the past, these filters were used by attackers to deactivate JavaScript code on the attacked web page. Sometimes the XSS filters itself are vulnerable in a way, that web applications which were protected properly against XSS attacks became vulnerable under certain conditions.

Remediation background :-
It is considered as better practice to instruct the browser XSS filter to never render the web page if an XSS attack is detected.

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
