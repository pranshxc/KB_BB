---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '204047'
original_report_id: '204047'
title: Segmentation fault while printing backtrace
weakness: Uncontrolled Resource Consumption
team_handle: shopify-scripts
created_at: '2017-02-06T23:57:57.045Z'
disclosed_at: '2017-03-14T21:11:22.179Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Segmentation fault while printing backtrace

## Metadata

- HackerOne Report ID: 204047
- Weakness: Uncontrolled Resource Consumption
- Program: shopify-scripts
- Disclosed At: 2017-03-14T21:11:22.179Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The code below crashes the sandbox/mruby as it tries to print the backtrace. Incidentally, it does not crash mirb.
```
def foo(n)
  return '\' 
  if n \n' ensure % 
  if:n != if n == -1110
  else foo(n-1).%  
  end
end %foo(0)
```

We are still examining the bug and hope to produce a detailed analysis and a fix this week.

Thank you,
Dinko Galetic
Denis Kasak

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
