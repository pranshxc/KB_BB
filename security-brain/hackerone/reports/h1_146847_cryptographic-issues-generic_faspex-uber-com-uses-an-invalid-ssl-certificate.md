---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '146847'
original_report_id: '146847'
title: faspex.uber.com uses an invalid SSL certificate
weakness: Cryptographic Issues - Generic
team_handle: uber
created_at: '2016-06-23T17:17:59.760Z'
disclosed_at: '2016-07-07T23:03:32.772Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- cryptographic-issues-generic
---

# faspex.uber.com uses an invalid SSL certificate

## Metadata

- HackerOne Report ID: 146847
- Weakness: Cryptographic Issues - Generic
- Program: uber
- Disclosed At: 2016-07-07T23:03:32.772Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

The SSL certificate deployed on faspex.uber.com was originally issued for faspex.ubersp.com. This means the certificate is invalid for that domain and when loaded will display an error in the user's browser. Since this is an uber internal page, uber employees are most likely getting used to clicking through SSL errors which opens them up to future MITM attacks. 

Thanks,
David Dworken

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
