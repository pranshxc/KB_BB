---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '789034'
original_report_id: '789034'
title: Buffer Overflow in ext_lm_group_acl helper
weakness: Classic Buffer Overflow
team_handle: ibb
created_at: '2020-02-04T21:58:53.101Z'
disclosed_at: '2021-07-28T18:44:41.421Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
asset_identifier: IBB (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
- classic-buffer-overflow
---

# Buffer Overflow in ext_lm_group_acl helper

## Metadata

- HackerOne Report ID: 789034
- Weakness: Classic Buffer Overflow
- Program: ibb
- Disclosed At: 2021-07-28T18:44:41.421Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary

Due to incorrect buffer management ext_lm_group_acl is vulnerable to a denial of service attack when processing NTLM Authentication credentials. This problem is limited to installations using the
ext_lm_group_acl binary.

## Affected Versions

Squid 2.x -> 2.7.STABLE9
Squid 3.x -> 3.5.28
Squid 4.x -> 4.9

## Severity 

Due to incorrect input validation the NTLM authentication credentials parser in ext_lm_group_acl may write to memory outside the credentials buffer. On systems with memory access protections this can result in the helper process being terminated unexpectedly. Resulting in the Squid process also terminating and a denial of service for all clients using the proxy.

## Supporting Material/References:

Advisory : http://www.squid-cache.org/Advisories/SQUID-2020_3.txt

## Remediation

An official patch is available from the Squid archives for both Squid 3.5 and Squid 4. 

## Timeline

2019-11-11 : I reported the issue
2019-11-18 : I made a PR on GitHub with a fix
2019-11-22 :  Fix was merged

## Impact

See 'Severity' section of report.

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
