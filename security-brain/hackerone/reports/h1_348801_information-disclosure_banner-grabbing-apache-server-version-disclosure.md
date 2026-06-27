---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '348801'
original_report_id: '348801'
title: Banner Grabbing - Apache Server Version Disclosure
weakness: Information Disclosure
team_handle: nextcloud
created_at: '2018-05-08T08:32:13.236Z'
disclosed_at: '2018-05-17T09:05:01.273Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
asset_identifier: customerupdates.nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Banner Grabbing - Apache Server Version Disclosure

## Metadata

- HackerOne Report ID: 348801
- Weakness: Information Disclosure
- Program: nextcloud
- Disclosed At: 2018-05-17T09:05:01.273Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

I have found a little information disclosure on your system.

Banner Grabbing is a technique used to gain information about a remote server. Additionally, this technique is use to get information about remote servers.

I've captured the HTTP request while visiting https://customerupdates.nextcloud.com

POC: 
Simply check screenshot you will see server version of Nextcloud  [Apache/2.4.18 (Ubuntu)]

This information might help an attacker gain a greater understanding of the systems in use and potentially develop further attacks targeted at the specific version of Apache.

Remediation
Configure your web server to prevent information leakage from the SERVER header of its HTTP response.

I hope you'll fix it!

I think and hope this report would impress you.

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
