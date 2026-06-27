---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1929567'
original_report_id: '1929567'
title: ReDoS( Ruby, Time)
weakness: Uncontrolled Resource Consumption
team_handle: ibb
created_at: '2023-04-01T23:52:39.257Z'
disclosed_at: '2023-04-26T03:36:32.774Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 51
asset_identifier: https://github.com/ruby
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# ReDoS( Ruby, Time)

## Metadata

- HackerOne Report ID: 1929567
- Weakness: Uncontrolled Resource Consumption
- Program: ibb
- Disclosed At: 2023-04-26T03:36:32.774Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I reported at https://hackerone.com/reports/1485501

https://www.ruby-lang.org/en/news/2023/03/30/redos-in-time-cve-2023-28756/
> The Time parser mishandles invalid strings that have specific characters. It causes an increase in execution time for parsing strings to Time objects.
> A ReDoS issue was discovered in the Time gem 0.1.0 and 0.2.1 and Time library of Ruby 2.7.7.

## Impact

ReDoS occurs when `Time.rfc2822` accepts user input.

In `Rack::ConditionalGet`, the header value is parsed by `Time.rfc2822`,  it is possible to attack from the request.
Rails uses `::Rack::ConditionalGet` by default, it can be attacked by a request from the client.

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
