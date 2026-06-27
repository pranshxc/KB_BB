---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '273803'
original_report_id: '273803'
title: '[werkenbijmcdonalds.nl] Unsafe-inline in "script-src" results in "bootstrapping"
  or passing data to JavaScript from HTML pages.'
weakness: Violation of Secure Design Principles
team_handle: radancy
created_at: '2017-10-02T16:29:09.824Z'
disclosed_at: '2017-11-15T09:01:29.061Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
asset_identifier: werkenbijmcdonalds.nl
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# [werkenbijmcdonalds.nl] Unsafe-inline in "script-src" results in "bootstrapping" or passing data to JavaScript from HTML pages.

## Metadata

- HackerOne Report ID: 273803
- Weakness: Violation of Secure Design Principles
- Program: radancy
- Disclosed At: 2017-11-15T09:01:29.061Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi Dear Maximum Team

Hope you are good!

**Vulnerablity Summary**
The HTTP header of the werkenbijmcdonalds.nl website includes an unsafe-inline parameter for "script-src".

**Impact:**
However, the "script-src" parameter is set to "unsafe-inline" or "unsafe-eval", which allows injection of user passed values, which in result can be misused for Cross-Site Scripting attacks.This is to allow "bootstrapping" or passing data to JavaScript from HTML pages. It's a dangerous setting, so I recommend here to fix it soon by passing data to JavaScript in the DOM instead of creating JavaScript variables from HTML.


**Mitigation**
Please remove "unsafe-inline" from "script-src", to  resolve. Thanks for reading this!

If you need help, be free to ask.

Happy to help.

Regards,
@smit

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
