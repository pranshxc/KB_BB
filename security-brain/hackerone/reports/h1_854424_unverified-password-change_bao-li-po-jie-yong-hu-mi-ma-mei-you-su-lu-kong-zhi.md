---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '854424'
original_report_id: '854424'
title: 暴力破解用户密码没有速率控制
weakness: Unverified Password Change
team_handle: x
created_at: '2020-04-20T18:18:00.167Z'
disclosed_at: '2020-07-01T03:02:04.220Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 30
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- unverified-password-change
---

# 暴力破解用户密码没有速率控制

## Metadata

- HackerOne Report ID: 854424
- Weakness: Unverified Password Change
- Program: x
- Disclosed At: 2020-07-01T03:02:04.220Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

http://www.twitter.com的登录功能存在一个问题，只限制了单个用户尝试登录系统的错误次数，并不限制用固定的密码去尝试登录不同用户，或者是撞库



请您跟着视频操作，否则无法复现到此问题

## Impact

暴力破解用户密码没有速率控制

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
