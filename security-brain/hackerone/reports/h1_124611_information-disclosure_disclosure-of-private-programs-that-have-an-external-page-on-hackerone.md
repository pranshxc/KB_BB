---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '124611'
original_report_id: '124611'
title: Disclosure of private programs that have an "external" page on HackerOne
weakness: Information Disclosure
team_handle: security
created_at: '2016-03-20T08:51:54.051Z'
disclosed_at: '2016-04-01T08:31:28.954Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- information-disclosure
---

# Disclosure of private programs that have an "external" page on HackerOne

## Metadata

- HackerOne Report ID: 124611
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2016-04-01T08:31:28.954Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hay again ,

We know that there are some companies have "external" page on HackerOne :
https://hackerone.com/directory?query=type%3Aexternal&sort=name%3Aascending&page=1

Some of those companies are hosting private programs as well , (with the same handles)

We can pick up any program from the external programs list , and find out if it hosting a private program or not , by applying this 

https://hackerone.com/<program_handle>/thanks 

If it returned 200 OK statue with the thanks page of demo programs with demo thanked researchers , then it's hosting a private program on HackerOne {F79965} .

I think it's the same as #116029 minus the activities disclosure part , which obviously pumped up his bounty :D

Thanks,

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
