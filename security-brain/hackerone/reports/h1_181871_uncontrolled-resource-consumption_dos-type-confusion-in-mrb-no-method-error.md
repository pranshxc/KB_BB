---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '181871'
original_report_id: '181871'
title: 'DoS: type confusion in mrb_no_method_error'
weakness: Uncontrolled Resource Consumption
team_handle: shopify-scripts
created_at: '2016-11-13T03:58:33.109Z'
disclosed_at: '2017-03-01T21:25:22.719Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 60
tags:
- hackerone
- uncontrolled-resource-consumption
---

# DoS: type confusion in mrb_no_method_error

## Metadata

- HackerOne Report ID: 181871
- Weakness: Uncontrolled Resource Consumption
- Program: shopify-scripts
- Disclosed At: 2017-03-01T21:25:22.719Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Overwriting the 'new' method of the NoMethodError singleton to not return an exception object leads to memory corruption and possibly arbitrary code execution.

Running the following code under the mruny-engine sandbox script results in a native crash:
    NoMethodError.define_singleton_method(:new) do "waat" end
    Object.q

Attached is a patch to mitigate the issue.

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
