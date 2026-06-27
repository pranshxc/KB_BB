---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1884372'
original_report_id: '1884372'
title: HAProxy stats panel exposed externally
weakness: Information Disclosure
team_handle: deptofdefense
created_at: '2023-02-23T12:30:51.505Z'
disclosed_at: '2023-03-24T17:25:49.058Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- information-disclosure
---

# HAProxy stats panel exposed externally

## Metadata

- HackerOne Report ID: 1884372
- Weakness: Information Disclosure
- Program: deptofdefense
- Disclosed At: 2023-03-24T17:25:49.058Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team

I was able to find exposed web panel for HAProxy running on ████at port 1024

## Impact

By visiting http://██████:1024/haproxy-status, the statistics page for HAProxy is shown. I have attached a screenshot to confirm that the endpoint is accessible externally
███

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
To Reproduce this simply visit 
http://███:1024/haproxy-status?stats
http://███:1024/haproxy-status

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
