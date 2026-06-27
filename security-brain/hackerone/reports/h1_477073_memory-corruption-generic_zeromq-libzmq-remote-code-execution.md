---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '477073'
original_report_id: '477073'
title: ZeroMQ libzmq remote code execution
weakness: Memory Corruption - Generic
team_handle: ibb
created_at: '2019-01-09T12:16:04.570Z'
disclosed_at: '2019-09-12T20:44:49.134Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 29
asset_identifier: IBB (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
- memory-corruption-generic
---

# ZeroMQ libzmq remote code execution

## Metadata

- HackerOne Report ID: 477073
- Weakness: Memory Corruption - Generic
- Program: ibb
- Disclosed At: 2019-09-12T20:44:49.134Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Bug report and exploit: https://github.com/zeromq/libzmq/issues/3351
Fix by me: https://github.com/zeromq/libzmq/pull/3353

My motive for full disclosure is as follows:

```
Is it true that it is not safe to use ZeroMQ over the internet because it will crash?

Earlier versions of the ZeroMQ library (before 2.1) were not very resilient against "fuzzing" attacks. A malformed packet or garbage data could cause an old version of the library to assert and exit. Since the release of 2.1, all reported cases of assertions caused by bad data have been fixed. If your testing uncovers a problem in this area, please file a bug report.
```
Source: http://zeromq.org/area:faq

The issue reporting page (http://zeromq.org/docs:issue-tracking) instructs to open a Github issue, with no special procedure for security issues, so I went ahead and did just that.

libzmq appears to be widely used and has wrapper implementations for Go, Python, Java, Node.js, etc.

## Impact

Running arbitrary code on the victim's system.

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
