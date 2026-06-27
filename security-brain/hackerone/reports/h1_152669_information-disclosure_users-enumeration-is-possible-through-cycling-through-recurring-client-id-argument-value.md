---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '152669'
original_report_id: '152669'
title: Users enumeration is possible through cycling through recurring[client_id]
  argument value.
weakness: Information Disclosure
team_handle: harvest
created_at: '2016-07-20T20:39:02.128Z'
disclosed_at: '2016-09-10T15:54:53.060Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
tags:
- hackerone
- information-disclosure
---

# Users enumeration is possible through cycling through recurring[client_id] argument value.

## Metadata

- HackerOne Report ID: 152669
- Weakness: Information Disclosure
- Program: harvest
- Disclosed At: 2016-09-10T15:54:53.060Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Details:**  
An attacker can enumerate the names of companies on your site by going to the URL `https://harvesterxxx.harvestapp.com/recurring_invoices/new?utf8=%E2%9C%93&recurring[client_id]=4677449&new_client[name]=` and cycling through the numerical value of the `recurring[client_id]=` argument, which will view their names in the header of the page.  
  
**PoC:**  
1. Visit the aforementioned URL `https://harvesterxxx.harvestapp.com/recurring_invoices/new?utf8=%E2%9C%93&recurring[client_id]=4677449&new_client[name]=`
2. increase or decrease the numerical value of the argument `recurring[client_id]=`  
3. Now you can enumerate through the names of companies on Harvestapp.com  
  
*PS: i couldn't really determine whether or not this behavior was intentional or not but when i tried to submit a recurring invoice on behalf of the enumerated users the server returned an error, which led me to think that the names weren't supposed to be shown in the first place since this would fall under "information disclosure"*

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
