---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '189548'
original_report_id: '189548'
title: GNIP subdomain take over
team_handle: x
created_at: '2016-12-08T16:21:08.992Z'
disclosed_at: '2017-02-06T01:59:02.263Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 30
tags:
- hackerone
---

# GNIP subdomain take over

## Metadata

- HackerOne Report ID: 189548
- Weakness: 
- Program: x
- Disclosed At: 2017-02-06T01:59:02.263Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,
Your subdomain at blog.gnipcentral.com is not well configured with allows subdomain take over as @fransoren explained in report #145224 .

PoC:
Go to http://blog.gnipcentral.com/ , you will be redirected to my domain http://testcloudfrontbug.s3-us-west-2.amazonaws.com/asd/index.html 


Please for more information visit the report made by @fransorosen, it's explained with all details possible.

Thanks,
Hussein

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
