---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1278977'
original_report_id: '1278977'
title: Sensitive data exposure via /secure/QueryComponent!Default.jspa endpoint on
  ████████
weakness: Information Disclosure
team_handle: deptofdefense
created_at: '2021-07-27T12:14:31.181Z'
disclosed_at: '2022-04-29T14:03:34.013Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Sensitive data exposure via /secure/QueryComponent!Default.jspa endpoint on ████████

## Metadata

- HackerOne Report ID: 1278977
- Weakness: Information Disclosure
- Program: deptofdefense
- Disclosed At: 2022-04-29T14:03:34.013Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**

Hi,
While going through the testing of DoD assets, I have came across a subdomain that is vulnerable to CVE-2020-14179. Some of the internal fields that are exposed are Project, Status, Limits, Creator, Query, Created Date, Updated Date, Resolution Date, etc. 

## References

https://jira.atlassian.com/browse/JRASERVER-71536
https://www.cvedetails.com/cve/CVE-2020-14179

## Impact

It allows unauthenticated attackers like me to view custom field names and custom SLA names via an Information Disclosure vulnerability in the /secure/QueryComponent!Default.jspa endpoint.

## System Host(s)
███

## Affected Product(s) and Version(s)


## CVE Numbers
CVE-2020-14179

## Steps to Reproduce
1.  Open browser
    2. Hit endpoint */jira/secure/QueryComponent!Default.jspa* in the target
    3. Observe the results.

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
