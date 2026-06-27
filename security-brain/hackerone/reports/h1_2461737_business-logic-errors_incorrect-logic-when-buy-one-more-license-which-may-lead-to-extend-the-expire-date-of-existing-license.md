---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2461737'
original_report_id: '2461737'
title: Incorrect logic when buy one more license which may lead to extend the expire
  date of existing license
weakness: Business Logic Errors
team_handle: portswigger
created_at: '2024-04-13T08:08:42.651Z'
disclosed_at: '2024-04-16T07:41:26.935Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 53
asset_identifier: portswigger.net
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Incorrect logic when buy one more license which may lead to extend the expire date of existing license

## Metadata

- HackerOne Report ID: 2461737
- Weakness: Business Logic Errors
- Program: portswigger
- Disclosed At: 2024-04-16T07:41:26.935Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi Team,

I noticed a bug in the licenses which may lead to extend the expire date of existing license. To be honest, it is hard for me to reproduce it. I was plan to see if the license still works after ███████. I think it's better to report this issue to you althought it may prove it is just a display issue. 

Background: 
when our company buy one more license with 5 years. Our existing license with 4 users will expire on ████. After we pay the money and got the new license. I revisit the following page and found something interesting. My existing license change from 4 users to 1 user, but the expire date is change to ███. 
██████

1. Make sure you have an existing license (in my case, we have a 4 users licenses which will expire on ██████████). 
2. Buy a new one user license with 5 years and pay it.
3. After you receive the license, check it on the following page.
█████

Observer result:
1. The existing license has change from 4 user to 1 user, but the expire date is █████████. I don't try to see if we can still use the left of the license because it will consume our licenses. 
2. The new license should expire at around ███████ but now it is ███. This means the new license expire date is extended. 

You can track my accout to debug this issue. If you need any help from me. Please feel free to let me know. Thanks!
████

User can use this way to extend the existing license. For example, you can just buy one year and it will expire next year. Then buy one more license which will expire 10 years. Now you have two license both will expire 10 years.

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
