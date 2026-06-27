---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '208566'
original_report_id: '208566'
title: Outdated Jenkins server hosted at OwnCloud.org
weakness: Information Disclosure
team_handle: owncloud
created_at: '2017-02-24T08:22:00.187Z'
disclosed_at: '2017-03-30T08:26:41.572Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- information-disclosure
---

# Outdated Jenkins server hosted at OwnCloud.org

## Metadata

- HackerOne Report ID: 208566
- Weakness: Information Disclosure
- Program: owncloud
- Disclosed At: 2017-03-30T08:26:41.572Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

###Summary: 
The target OwnCloud's server is running an outdated version of _Jenkins server_ which is vulnerable to various attacks.

Server Location: `https://ci.owncloud.org`

Vulnerable Software: `Jenkins ver. 2.27`

###Proof of Exploitability

CVE-2016-3727
**POC URL:** `https://ci.owncloud.org/computer/(master)/api/xml`

>Details:

> The API URL /computer/(master)/api/xml allowed users with the extended read permission for the master node to see some global Jenkins configuration, including the configuration of the security realm.

> Source: https://jenkins.io/security/advisory/2016-05-11/


Additionally, the current software version is also vulnerable to RCE.
>CVE-2017-2608

>XStream remote code execution vulnerability

>Affected Versions:  < 2.43

> Source: https://jenkins.io/security/advisory/2017-02-01/

###Recommended Fix
Update Jenkins server to latest version 2.47

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
