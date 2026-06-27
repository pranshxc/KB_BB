---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '166699'
original_report_id: '166699'
title: Reflected xss on websummit.net
weakness: Cross-site Scripting (XSS) - Generic
team_handle: websummit
created_at: '2016-09-07T22:51:25.008Z'
disclosed_at: '2016-10-04T23:32:19.401Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected xss on websummit.net

## Metadata

- HackerOne Report ID: 166699
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: websummit
- Disclosed At: 2016-10-04T23:32:19.401Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey guys,

**TL;DR:** Reflected XSS on `websummit.net/attendees/featured-attendees` as the `q` parameter is directly reflecting special characters in the `data-url` on the handlebars template section of the page, as opposed to URL encoding them.

**Proof of Concept:**
Visit [https://websummit.net/attendees/featured-attendees?q=rubyoob%27%3E%3Ciframe/onload=alert(document.domain)%3E%3C/iframe%3E](https://websummit.net/attendees/featured-attendees?q=rubyoob%27%3E%3Ciframe/onload=alert\(document.domain\)%3E%3C/iframe%3E]). I've tested this on all modern browsers (latest Chrome, Firefox and Edge).

**Mitigation:** 
To mitigate this issue, I'd recommend URL encoding special characters when creating the `data-url` parameter server-side.

At the moment, visiting my proof of concept would generate HTML like:
`<script id="fa-list" class='api-json' data-target='#attendees' data-url='https://api.cilabs.net/v1/conferences/ws16/info/attendees?limit=25&q=rubyoob'><iframe/onload=alert(document.domain)></iframe>,' type='text/x-handlebars-template' data-page="1">`

It should be generating something similar to:
`<script id="fa-list" class='api-json' data-target='#attendees' data-url='https://api.cilabs.net/v1/conferences/ws16/info/attendees?limit=25&q=rubyoob%27%3E%3Ciframe%2Fonload%3Dalert(document.domain)%3E%3C%2Fiframe%3E,' type='text/x-handlebars-template' data-page="1">`

This would allow all API requests to go through without interruption and stop attackers from executing arbitrary javascript on the page.

Cheers,
@rubyroobs

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
