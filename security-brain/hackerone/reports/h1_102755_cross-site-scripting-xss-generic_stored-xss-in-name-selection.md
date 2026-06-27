---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '102755'
original_report_id: '102755'
title: Stored XSS in name selection
weakness: Cross-site Scripting (XSS) - Generic
team_handle: algolia
created_at: '2015-12-01T01:49:22.668Z'
disclosed_at: '2016-06-18T18:26:15.868Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in name selection

## Metadata

- HackerOne Report ID: 102755
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: algolia
- Disclosed At: 2016-06-18T18:26:15.868Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

You have a stored XSS vuln when you set your name in your account information.

to reproduce just set your name field to:
</script><script>alert('xss')</script>

and most pages on your account you will show XSS.

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
