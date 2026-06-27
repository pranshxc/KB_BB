---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '294364'
original_report_id: '294364'
title: De-anonymization by visiting specially crafted bookmark.
weakness: Information Disclosure
team_handle: torproject
created_at: '2017-12-02T00:41:24.597Z'
disclosed_at: '2018-07-03T04:35:59.675Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- information-disclosure
---

# De-anonymization by visiting specially crafted bookmark.

## Metadata

- HackerOne Report ID: 294364
- Weakness: Information Disclosure
- Program: torproject
- Disclosed At: 2018-07-03T04:35:59.675Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

There is a way to import logs in 'about:memory' from local disk, however, (tested on windows) you can pass a network url that may point to attack controlled server which logs IP's. This connection is done by windows (presumably) and so doesn't hide real IP of Tor user.

1. Have victim drag and drop an anchor tag pointing to 'about:memory?file=\\localhost\\q.json.gz' inside bookmarks bar.
2. Victim then clicks on bookmark to visit URL.
3. An unproxied connection is made to 'localhost'

## Impact

De-anonymization. If coupled with a bug to open privileged pages (which about:memory is) one could theoretically achieve a very dangerous exploit to expose real ips of victims.

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
