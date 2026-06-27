---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '117325'
original_report_id: '117325'
title: DMARC is misconfigured for grtp.co
weakness: Violation of Secure Design Principles
team_handle: gratipay
created_at: '2016-02-19T12:24:36.518Z'
disclosed_at: '2016-04-02T18:46:08.773Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# DMARC is misconfigured for grtp.co

## Metadata

- HackerOne Report ID: 117325
- Weakness: Violation of Secure Design Principles
- Program: gratipay
- Disclosed At: 2016-04-02T18:46:08.773Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

in grtp.co ,
your dmark record  published in the wrong place! !
, your DMARC record needs to discoverable at _dmarc.grtp.co, and not at grtp.co. The "_dmarc." part is required!


Thanks
Paresh

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
