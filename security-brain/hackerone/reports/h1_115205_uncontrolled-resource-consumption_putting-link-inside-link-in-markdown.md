---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '115205'
original_report_id: '115205'
title: Putting link inside link in markdown
weakness: Uncontrolled Resource Consumption
team_handle: security
created_at: '2016-02-07T14:57:10.339Z'
disclosed_at: '2016-04-02T11:06:17.608Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Putting link inside link in markdown

## Metadata

- HackerOne Report ID: 115205
- Weakness: Uncontrolled Resource Consumption
- Program: security
- Disclosed At: 2016-04-02T11:06:17.608Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello.
I was playing around in markdown editor and find 1 interesting feature.
You can put a link inside link.
```
[  [ololo][l]   ][l]
[l]:http://dwq
```
If you do it `[ololo][l]` will be parsed first, then result of parsing will be send outside.
Maximum depth of such link inserting is 16.
So the slowest thing we can do is:
```
[[[[[[[[[[[[[[[[][l]][l]][l]][l]][l]][l]][l]][l]][l]][l]][l]][l]][l]][l]][l]][l]
[l]:http://dwq
```
If we will add more such lines we will get error 522 from cloudflare.

Example with 522 error:
https://hackerone.com/fuzopeti

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
