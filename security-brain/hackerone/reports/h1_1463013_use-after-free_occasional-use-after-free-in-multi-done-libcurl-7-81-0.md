---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1463013'
original_report_id: '1463013'
title: Occasional use-after-free in multi_done() libcurl-7.81.0
weakness: Use After Free
team_handle: curl
created_at: '2022-01-28T18:22:32.999Z'
disclosed_at: '2022-03-09T21:46:52.194Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- use-after-free
---

# Occasional use-after-free in multi_done() libcurl-7.81.0

## Metadata

- HackerOne Report ID: 1463013
- Weakness: Use After Free
- Program: curl
- Disclosed At: 2022-03-09T21:46:52.194Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

We are seeing the use of a `struct connectdata *` on a thread after it was returned to the connection cache (and thus available for use on other threads including potential deallocation) in `multi_done()` in libcurl-7.81.0.  This could occasionally result in an actual use-after-free, witnessed on Windows 10 platform.

## Steps To Reproduce:
- [`multi_done()` line 717](https://github.com/curl/curl/blob/curl-7_81_0/lib/multi.c#L717) a call is made to `Curl_conncache_return_conn()`
- `Curl_conncache_return_conn()` returns `TRUE` (conn was returned to the cache and available for use in other threads) and execution continues on [line 719](https://github.com/curl/curl/blob/curl-7_81_0/lib/multi.c#L719) where the code derefs the now unowned `conn` to get the `connection_id`
- We have a fork with a [commit](https://github.com/luminixinc/curl/commit/e8560cb3a2aa0c104d1afcc77490b70bad1ce9cd) that both tests (inline, not formally) and offers a potential fix for this issue.
- See attached screenshot showing assert firing in debug build

## Impact

Unsure.

I'm not a hacker, and would have been happy to submit this as a GitHub issue instead, but _discretion being the better part of valor_, decided to post this issue here instead :)

Tangentially, I do not care to get credit or receive a bounty for this issue.  Would be great to get this fixed as I suggested or in some other manner, thanks!

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
