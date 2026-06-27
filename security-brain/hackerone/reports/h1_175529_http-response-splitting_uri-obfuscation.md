---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '175529'
original_report_id: '175529'
title: URI Obfuscation
weakness: HTTP Response Splitting
team_handle: brave
created_at: '2016-10-13T06:00:01.767Z'
disclosed_at: '2016-10-15T02:40:09.971Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- http-response-splitting
---

# URI Obfuscation

## Metadata

- HackerOne Report ID: 175529
- Weakness: HTTP Response Splitting
- Program: brave
- Disclosed At: 2016-10-15T02:40:09.971Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Typically, when obfuscating a URL, you must trick someone into viewing a website they did not want to view by tempting them with something they are familiar with.

## Products affected: 

Latest Version of Brave in Windows

## Steps To Reproduce:
We can trick someone into viewing it like this:
http://example.com@sample.com
This will make the user think they are going to go to example.com, when really they are going to sample.com.

Live POC:
https://brave.com@secuna.ph/

They thought they will be redirect to brave.com but the page displays secuna.ph

I attached a picture and make sure to focus your eyes in the URL Address.

## Supporting Material/References:

{F127608}

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
