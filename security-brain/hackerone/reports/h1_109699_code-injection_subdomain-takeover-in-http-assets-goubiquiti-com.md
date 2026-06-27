---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '109699'
original_report_id: '109699'
title: Subdomain Takeover in http://assets.goubiquiti.com/
weakness: Code Injection
team_handle: ui
created_at: '2016-01-10T10:10:43.037Z'
disclosed_at: '2016-02-14T23:30:37.820Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
tags:
- hackerone
- code-injection
---

# Subdomain Takeover in http://assets.goubiquiti.com/

## Metadata

- HackerOne Report ID: 109699
- Weakness: Code Injection
- Program: ui
- Disclosed At: 2016-02-14T23:30:37.820Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi there,

Its urgent issue about your subdomain http://assets.goubiquiti.com pointing to AWS S3 but no such website configuration is made. This unused subdomain can claim by anyone and fully take over it.

An attacker can fully takeover this subdomain and do whatever he wants. this can cause huge damage to the website's main domain as well as to the company.

I Recommend to remove the Cname and Dns connecting to it. 
PoC is attached to this report.

You can read about this sort of attacks here : http://labs.detectify.com/post/109964122636/hostile-subdomain-takeover-using

Please Consider my report to Support my study

cheers,

Karl

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
