---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '663431'
original_report_id: '663431'
title: IDOR in Bugs overview enables attacker to determine the date range a hackathon
  was active
weakness: Insecure Direct Object Reference (IDOR)
team_handle: security
created_at: '2019-07-29T22:59:38.121Z'
disclosed_at: '2019-12-13T17:53:35.192Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 25
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR in Bugs overview enables attacker to determine the date range a hackathon was active

## Metadata

- HackerOne Report ID: 663431
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: security
- Disclosed At: 2019-12-13T17:53:35.192Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

A minor Insecure Direct Object Reference (IDOR) vulnerability is present in the `/bugs` endpoint. One of the Bugs overview filters enables a program member to filter by Hackathon that their program was a part of. This filter is applied when hackathon IDs are provided in the `hackathons` parameter, like https://hackerone.com/bugs?subject=security&hackathons[]=28.

The parameter takes an array of IDs and is vulnerable to an IDOR. When a hackathon ID is given that belongs to a private hackathon, a date range will be applied. Based on the extremes of the returned reports submission date, a user could determine the date range of the hackathon.

This vulnerability is easier to exploit for a program that has a lot of reports submitted on different days.

## Impact

The date range of a private hackathon could be determined. At the moment, there aren't any real hackathon objects that are marked as private, so no sensitive information is disclosed.

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
