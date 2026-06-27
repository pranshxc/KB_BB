---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '179920'
original_report_id: '179920'
title: WordPress DB Class, bad implementation of prepare method guides to sqli and
  information disclosure
weakness: SQL Injection
team_handle: wordpress
created_at: '2016-11-03T13:32:17.535Z'
disclosed_at: '2017-11-13T14:56:48.898Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 17
tags:
- hackerone
- sql-injection
---

# WordPress DB Class, bad implementation of prepare method guides to sqli and information disclosure

## Metadata

- HackerOne Report ID: 179920
- Weakness: SQL Injection
- Program: wordpress
- Disclosed At: 2017-11-13T14:56:48.898Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Issue 1: Method checks if first argument is an array and if it is, it avoids the rest of the arguments and uses the first argument array values as input.

Issue 2: When input query has %s in it, then it quote and this guides to sql injection in case query that need to be prepared have quoted user controlled input in it.  

This leaves all wordpress plugins/ themes potentially vulnerable on this two types of attack. As PoC sqli in bbpress wp plugin and core wp function is shown.

PoC: 
1. There is SQLi in bbpress in case anonymous posting is allowed. ( check  bbpress-sqli.png)
2.  Demo for the Issue 1 and Issue 2 for the prepare method
3. Wordpress core function delete_metadata is vulnerable to sqli in case delete all e.g. last argument is true and meta value has value e.g. is user supplied / controlled.

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
