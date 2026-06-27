---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '131452'
original_report_id: '131452'
title: PHP 5.4.45 is Outdated and Full of Preformance Interupting Arbitrary Code Execution
  Bugs
weakness: Violation of Secure Design Principles
team_handle: gratipay
created_at: '2016-04-16T22:49:59.379Z'
disclosed_at: '2017-08-21T13:29:40.785Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# PHP 5.4.45 is Outdated and Full of Preformance Interupting Arbitrary Code Execution Bugs

## Metadata

- HackerOne Report ID: 131452
- Weakness: Violation of Secure Design Principles
- Program: gratipay
- Disclosed At: 2017-08-21T13:29:40.785Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Your PHP version is affected by quite a few remote arbitrary code execution, remote file renaming, and remote file rewriting bugs that require no authentication and can cause big problems, from performance interruptions and messing with server files to DoS attacks. These are not related to any particular non-default module, but php itself.

Here's a little list I compiled:
                CVE-2015-2301
                CVE-2014-9652
               CVE-2014-5459
               CVE-2014-4698
               CVE-2014-4670
               CVE-2014-3981

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
