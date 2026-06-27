---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1804128'
original_report_id: '1804128'
title: ReDoS (Rails::Html::PermitScrubber.scrub_attribute)
team_handle: ibb
created_at: '2022-12-14T10:10:23.525Z'
disclosed_at: '2022-12-14T22:51:27.924Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
asset_identifier: https://github.com/rails
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# ReDoS (Rails::Html::PermitScrubber.scrub_attribute)

## Metadata

- HackerOne Report ID: 1804128
- Weakness: 
- Program: ibb
- Disclosed At: 2022-12-14T22:51:27.924Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I reported at  https://hackerone.com/reports/1684163

https://github.com/rails/rails-html-sanitizer/security/advisories/GHSA-5x79-w82f-gw8w

> Certain configurations of rails-html-sanitizer < 1.4.4 use an inefficient regular expression that is susceptible to excessive backtracking when attempting to sanitize certain SVG attributes. This may lead to a denial of service through CPU resource consumption.

It seems that the same problem existed on the Loofah side, so it was fixed as well. That has been fixed as CVE-2022-23514(https://github.com/flavorjones/loofah/security/advisories/GHSA-486f-hjj9-9vhh)

## Impact

ReDoS may occur if scrub is executed in Rails::Html::PermitScrubber.

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
