---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '259400'
original_report_id: '259400'
title: Issues with Forgot password Error Handling
weakness: Business Logic Errors
team_handle: legalrobot
created_at: '2017-08-13T10:37:42.186Z'
disclosed_at: '2017-09-26T01:10:37.034Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
asset_identifier: app.legalrobot-test.com
asset_type: URL
max_severity: none
tags:
- hackerone
- business-logic-errors
---

# Issues with Forgot password Error Handling

## Metadata

- HackerOne Report ID: 259400
- Weakness: Business Logic Errors
- Program: legalrobot
- Disclosed At: 2017-09-26T01:10:37.034Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello @team,

I found a similar issue to #249695.Where user when giving an error email id it is not showing any error response.This is not of high impact but this might throw the users in confusing state as there is no error message user will be waiting for the server response.

Steps to reproduce:
1.go to url : https://app.legalrobot-uat.com/sign-in
2. go to forgot password option and give your email id
3.now click on the forgot password link.
4.give wrong email id and some password
5.now you will see that there is no server response .

How to resolve this?
Similar to login failure error message 403.we can also show the error message like this:
"password change failure.please check the details entered[403]" when the user is given wrong email id .
there is another issue here what if he is using this to user enumeration?that is not possible because of two reasons.
1)now legalrobot requests are turned to web socket messages it will be difficult to user enumeration
2)there wont be point of user enumeration because we will show 403 error for every registered and non-registered email id.Only for the forgot password requested email id it will show 200 ok response

Let me know if u need more information regarding this.
Thanks!

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
