---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '965914'
original_report_id: '965914'
title: '`fs.realpath.native` on darwin may cause buffer overflow'
weakness: Classic Buffer Overflow
team_handle: nodejs
created_at: '2020-08-24T15:18:48.855Z'
disclosed_at: '2020-10-17T19:17:19.242Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
asset_identifier: https://github.com/nodejs/node
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- classic-buffer-overflow
---

# `fs.realpath.native` on darwin may cause buffer overflow

## Metadata

- HackerOne Report ID: 965914
- Weakness: Classic Buffer Overflow
- Program: nodejs
- Disclosed At: 2020-10-17T19:17:19.242Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

**Summary:** 

The libuv's implementation of realpath is flawed on darwin and may cause buffer overflow.

**Description:** 

libuv's `realpath` implementation determines the buffer size with `pathconf` and fallback to `_POSIX_PATH_MAX` (256) if that fails for any reason (eg. `ENOENT`). However `realpath` requires a buffer of at least `PATH_MAX` (1024) bytes to be used, hence causes the buffer overflow if the resolved path is longer than 256 bytes.

## Steps To Reproduce:

1. `LONG_PATH='/tmp/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/path/254B'`
1. `SHORT_LINK='/tmp/short'`
1. `mkdir -p "${LONG_PATH}"`
1. `ln -s "${LONG_PATH}" "${SHORT_LINK}"`
1. `node -e "fs.realpathSync.native('${SHORT_LINK}/file-not-exist')"`

## Impact: 

Cause node process to crash.

## Supporting Material/References:

- https://github.com/bazelbuild/rules_nodejs/issues/1958
- https://github.com/libuv/libuv/issues/2965
- https://github.com/libuv/libuv/issues/2966

## Impact

Given that nodejs on darwin are mostly desktop applications and used as developer tools, exploit this is very unlikely to cause more damage than an application crash.

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
