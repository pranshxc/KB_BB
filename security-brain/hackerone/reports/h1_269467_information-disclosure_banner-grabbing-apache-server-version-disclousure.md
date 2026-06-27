---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '269467'
original_report_id: '269467'
title: Banner Grabbing - Apache Server Version Disclousure
weakness: Information Disclosure
team_handle: owncloud
created_at: '2017-09-19T12:46:00.504Z'
disclosed_at: '2017-10-22T10:07:12.848Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 19
asset_identifier: marketplace.owncloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Banner Grabbing - Apache Server Version Disclousure

## Metadata

- HackerOne Report ID: 269467
- Weakness: Information Disclosure
- Program: owncloud
- Disclosed At: 2017-10-22T10:07:12.848Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello ownCloud, I'd like to report a nice little bug.

Banner Grabbing is a technique used to gain information about a remote server. Additionally, this technique is use to get information about remote servers.

I've captured the HTTP request while visiting https://marketplace.owncloud.com/ and https://owncloud.com

POC: 
Simply check screenshot you will see server version of ownCloud [Apache/2.4.27 (Unix)]

This information might help an attacker gain a greater understanding of the systems in use and potentially develop further attacks targeted at the specific version of Apache.

Impact
An attacker might use the disclosed information to harvest specific security vulnerabilities for the version identified.

Remediation
Configure your web server to prevent information leakage from the SERVER header of its HTTP response.

I hope you'll fix it!

I think and hope this report would impress you.

Let me know if u have any question
Thanks
Cheers
Anas

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
