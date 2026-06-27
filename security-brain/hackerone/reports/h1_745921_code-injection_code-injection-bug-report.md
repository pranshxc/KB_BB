---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '745921'
original_report_id: '745921'
title: Code Injection Bug Report
weakness: Code Injection
team_handle: ruby
created_at: '2019-11-25T13:32:06.662Z'
disclosed_at: '2021-05-07T11:50:39.776Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: https://github.com/ruby/ruby
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- code-injection
---

# Code Injection Bug Report

## Metadata

- HackerOne Report ID: 745921
- Weakness: Code Injection
- Program: ruby
- Disclosed At: 2021-05-07T11:50:39.776Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Good morning, I hope this message finds you well. On 22 November 2019, I emailed security@ruby-lang.org about a Code Injection bug on cache.ruby-lang.org, as the ruby-lang.org website is considered out-of-scope on H1. on 24 November 2019 the bug was acknowledged and [a patch](https://github.com/ruby/cache.r-l.o/commit/8739ca125f412a0cf2583b4b49a10ea52c75ff5f) released. This morning, 27 November 2019, I was asked to open this ticket.

## Impact

A lack of filtering on the cache.ruby-lang.org website enabled persons to inject code into the page, spoofing messages to the user, or redirecting them to malicious websites.

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
