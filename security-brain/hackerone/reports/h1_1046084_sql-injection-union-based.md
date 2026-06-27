---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1046084'
original_report_id: '1046084'
title: SQL Injection Union Based
team_handle: automattic
created_at: '2020-11-28T12:47:00.469Z'
disclosed_at: '2021-01-01T09:19:02.827Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 126
tags:
- hackerone
---

# SQL Injection Union Based

## Metadata

- HackerOne Report ID: 1046084
- Weakness: 
- Program: automattic
- Disclosed At: 2021-01-01T09:19:02.827Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Hello, 

I have found a SQL Injection Union Based on `https://intensedebate.com/commenthistory/$YourSiteId `
The `$YourSiteId` into the url is vulnerable to SQL Injection.

## Steps to reproduce

1.  Logging into `https://intensedebate.com`

2. After create your own site on `https://intensedebate.com/install` and follow all steps

3. Now you need to know your site id, to get then you need go to `https://intensedebate.com/user-dashboard` and you can see on the right side of the page your site list, choice your site and click to the link `Overview`.
You will be redirected to `https://intensedebate.com/dash/$YourSiteId`.

4. Now you have your site id,  go to the vulnerable URL with your site id `https://intensedebate.com/commenthistory/$YourSiteId`.
 
5. Now Trigger the SQL Injection with this following link `https://intensedebate.com/commenthistory/$YourSiteId%20union%20select%201,2,@@VERSION%23` (!) You need to do this with your own site id (!)

6. Now you can see `10.1.32-MariaDB` on the page.

## POC 

@@VERSION

{F1096977}

current_user()

{F1096976}

Video POC

## IMPORTANT
Can you see my comment into [#1044698](https://hackerone.com/reports/1044698) ??
 And I no longer want to put all SQL Injection issues on into my initial report [#1042746](https://hackerone.com/reports/1042746), because i don't win any reputations 

Thank you,

Fuzzme.

## Impact

Full database access holding private user information and Reflected Cross-Site-Scripting

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
