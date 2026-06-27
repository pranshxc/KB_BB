---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '460556'
original_report_id: '460556'
title: Banner Grabbing - Apache Server Version Disclousure
weakness: Information Disclosure
team_handle: ratelimited
created_at: '2018-12-11T17:54:57.078Z'
disclosed_at: '2018-12-11T20:57:14.603Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: theendlessweb.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Banner Grabbing - Apache Server Version Disclousure

## Metadata

- HackerOne Report ID: 460556
- Weakness: Information Disclosure
- Program: ratelimited
- Disclosed At: 2018-12-11T20:57:14.603Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello RATELIMITED, I'd like to report a nice little bug.

Banner Grabbing is a technique used to gain information about a remote server. Additionally, this technique is use to get information about remote servers.

I've captured the HTTP request while visiting theendlessweb.com

POC: 
Simply check screenshot you will see server version of RATELIMITED [Apache/2.4.25 (Debian)]

This information might help an attacker gain a greater understanding of the systems in use and potentially develop further attacks targeted at the specific version of Apache.

Impact
An attacker might use the disclosed information to harvest specific security vulnerabilities for the version identified.

Remediation

Configure your web server to prevent information leakage from the SERVER header of its HTTP response.

I hope you'll fix it!

## Impact

An attacker might use the disclosed information to harvest specific security vulnerabilities for the version identified.

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
