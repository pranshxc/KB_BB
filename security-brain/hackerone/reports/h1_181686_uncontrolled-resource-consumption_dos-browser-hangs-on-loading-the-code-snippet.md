---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '181686'
original_report_id: '181686'
title: '[DOS] Browser hangs on loading the code snippet'
weakness: Uncontrolled Resource Consumption
team_handle: brave
created_at: '2016-11-12T01:42:23.773Z'
disclosed_at: '2018-05-06T21:02:40.473Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- uncontrolled-resource-consumption
---

# [DOS] Browser hangs on loading the code snippet

## Metadata

- HackerOne Report ID: 181686
- Weakness: Uncontrolled Resource Consumption
- Program: brave
- Disclosed At: 2018-05-06T21:02:40.473Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Basically the function location.reload() is causing browser to hang as browser is not able to handle multiple reloads but similar issue cannot be seen in Firefox and chrome as i am able to close the current tab.

## Products affected: 

Latest brave browser in linux.

## Steps To Reproduce:
Use the below code and save it as html file and then open it up on browser :-

<script>
open("");
setInterval('location.reload()',1);
</script>

Or

open up pop.html that i have attached

## Supporting Material/References:

i have attached html file that contains the code causing denial of service,

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
