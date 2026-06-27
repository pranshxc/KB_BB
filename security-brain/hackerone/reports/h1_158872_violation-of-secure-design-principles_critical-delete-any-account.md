---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '158872'
original_report_id: '158872'
title: '[Critical] Delete any account'
weakness: Violation of Secure Design Principles
team_handle: olx
created_at: '2016-08-12T18:46:39.855Z'
disclosed_at: '2016-09-01T12:33:06.551Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 114
tags:
- hackerone
- violation-of-secure-design-principles
---

# [Critical] Delete any account

## Metadata

- HackerOne Report ID: 158872
- Weakness: Violation of Secure Design Principles
- Program: olx
- Disclosed At: 2016-09-01T12:33:06.551Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Guys

i found a vulnerable endpoint the can deletes any logged in user 

the vulnerable url is 
olx.com/myaccount/delete/

with only one parameter called removehash

___________

POST /account/register/ HTTP/1.1
Host: olx.com.eg
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.

removehash=f4023c8bjgV6Mfulnz00PEJ00ny%2BSo6ga%2BnU7MYC
___________
if you deleted it , request will pass with no errors 

so if a user visits a page containing an HTML FOrm with the above request , user account will be deleted


see this video 
https://youtu.be/VrRFmOI_ep0



FIX
-implement a csrf token
- check referer header before processing any action 
-validate removehash parameter

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
