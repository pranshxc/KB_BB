---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '416516'
original_report_id: '416516'
title: A 10GB file is reachable
weakness: Information Disclosure
team_handle: chaturbate
created_at: '2018-09-30T15:22:21.964Z'
disclosed_at: '2018-10-01T21:03:34.442Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
asset_identifier: '*.highwebmedia.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# A 10GB file is reachable

## Metadata

- HackerOne Report ID: 416516
- Weakness: Information Disclosure
- Program: chaturbate
- Disclosed At: 2018-10-01T21:03:34.442Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

##Summary##

A file is 10GB is accessible on the following server: http://edge193.stream.highwebmedia.com:8080/.

## Steps To Reproduce:

  1. Open the following link: http://edge193.stream.highwebmedia.com:8080/download

## Additional notes:

I tried to download the file and analyze  it, but after 20 seconds the server interrupted the connection. However an attacker can download the whole file if he has 1Gb/s or faster internet connection.

To be honest I do not know exactly, what is this file because I was not able to download and analyze it. This require further investigation on the server.

## Impact

An attacker is able to download this file and also could be able to extract sensitive information from it.

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
