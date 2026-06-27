---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '281387'
original_report_id: '281387'
title: HackerOne Report 281387
team_handle: stellar
created_at: '2017-10-21T07:18:57.571Z'
disclosed_at: '2020-02-23T16:22:08.654Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 6
tags:
- hackerone
---

# HackerOne Report 281387

## Metadata

- HackerOne Report ID: 281387
- Weakness: 
- Program: stellar
- Disclosed At: 2020-02-23T16:22:08.654Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

content on a server is including Javascript content from an unrelated domain. When this script code is fetched by a user browser and loaded into the DOM,

 it will have complete control over the DOM, bypassing the protection offered by the same-origin policy. 

Even if the source of the script code is trusted by the website operator, malicious code could be introduced if the server is ever compromised.
 
It is strongly recommended that sensitive applications host all included Javascript locally.

This gives the operator of the server where the code originates control over the DOM, and the web application .

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
