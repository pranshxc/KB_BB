---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1128701'
original_report_id: '1128701'
title: Lack warning label when receiving a letter
weakness: Phishing
team_handle: security
created_at: '2021-03-17T12:04:43.940Z'
disclosed_at: '2021-05-13T08:25:54.101Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 33
asset_identifier: http://hackerone.com/graphql
asset_type: URL
max_severity: critical
tags:
- hackerone
- phishing
---

# Lack warning label when receiving a letter

## Metadata

- HackerOne Report ID: 1128701
- Weakness: Phishing
- Program: security
- Disclosed At: 2021-05-13T08:25:54.101Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi team,

When using the function `ShareReportViaEmail` the email is sent to the email address specified by the hacker.This email looks legitimate and comes from verification email addresses, leaving no doubt about it being replaced. This endpoint also applies to sandbox reports which makes it possible to insert any information.

Our team believes that it is worth adding a label that would warn that this email was sent from a sandbox report, which would make it clear about possible social engineering, for example, how is it done when you are invited to a sandbox program

## Steps To Reproduce:

1. Create sandboxed program
2. Create fake asset, for example : https://hackerone.com
3. Create report 

Asset: `https://hackerone.com` , Weakness: `SQL Injection (cwe-89)`, Severity: `Critical`

4. GraphQL query:

`{"query":"mutation Createvpncredentialsmutation($input0:ShareReportViaEmailInput!) {shareReportViaEmail(input:$input0) {errors{edges{node{field,message,type}}},was_successful,clientMutationId}}","variables":{"input0":{"message":"If you would like to participate in the retest of this report , the payout for retest is 500$, please reply to this email : [haxta4ok00@wearehackerone.com] and we will send you an invite [HackerOne Retest Team]","emails":"USERNAME_of_HACKER@wearehackerone.com","report_id":"gid://hackerone/Report/ID_SANDBOXED_REPORT","clientMutationId":"0"}}}`


{F1233403}

In our opinion, this letter looks very plausible, which may provoke a response to send a response from the original mail to @wearehackerone.com, thereby revealing he email. Because to pay the retest, you will need the original account 

## Recommendation:

Our team believes that it makes sense to add a warning to this email template, indicating that it was sent from the sandbox and may not be related to the data specified in it

Thanks!

## Impact

The ability to get hackers ' email through social engineering

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
