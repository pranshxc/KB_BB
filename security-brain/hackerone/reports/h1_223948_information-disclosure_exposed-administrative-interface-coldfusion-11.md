---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223948'
original_report_id: '223948'
title: Exposed ███████ Administrative Interface (ColdFusion 11)
weakness: Information Disclosure
team_handle: deptofdefense
created_at: '2017-04-26T03:56:24.484Z'
disclosed_at: '2019-12-02T18:54:09.011Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- information-disclosure
---

# Exposed ███████ Administrative Interface (ColdFusion 11)

## Metadata

- HackerOne Report ID: 223948
- Weakness: Information Disclosure
- Program: deptofdefense
- Disclosed At: 2019-12-02T18:54:09.011Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
The "/██████████/administrator/" directory is accessible to the public and allows an attacker to further enumerate the system and/or perform brute force attacks.

**Description:**
The ████████ website has an exposed "Administrative Interface" for ColdFusion 11, which could be useful to an attacker to perform brute force attacks and/or further version enumeration. Additionally, leaving an exposed administrative interface open to the world, increases attack surface to zero days and other advanced attacks that would exploit the ████ administrative interface, which has been stopped previously due to access restrictions.

## Impact
Low
## Step-by-step Reproduction Instructions

1) Perform directory scanning, which detects the URL using tools such as Burp Suite professional spider and/or DirSearch.
2) Visit URL - https://█████████/████/administrator/index.cfm
3) None.

## Product, Version, and Configuration (If applicable)
ColdFusion 11
https://██████/████████/administrator/index.cfm

## Suggested Mitigation/Remediation Actions
The "/█████" directory should be completely locked down to prevent unauthorised access, to ensure secure design principles are followed. This can be achieved by .htaccess password protection, or IP restrictions with IP filtering. (IP/Domain Restrictions)

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
