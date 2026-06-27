---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '134206'
original_report_id: '134206'
title: Defect-Security | Driver-Broken Authentication | Able to update the Subscription
  Setting anonymously
weakness: Improper Authentication - Generic
team_handle: uber
created_at: '2016-04-24T14:06:41.526Z'
disclosed_at: '2016-07-26T00:31:07.386Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# Defect-Security | Driver-Broken Authentication | Able to update the Subscription Setting anonymously

## Metadata

- HackerOne Report ID: 134206
- Weakness: Improper Authentication - Generic
- Program: uber
- Disclosed At: 2016-07-26T00:31:07.386Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Steps to execute the issue/defect

1:Logged into account on domain (https://riders.uber.com) with one of the accounts (account type-Driver)

2:Now go to Manage your email subscription settings and note the link mentioned below


-View the subscription setting (i.e. subscription setting Uber Global Updates -checked)

-note the url -https://subscriptions.uber.com/user/483c39a2-9e7a-43fb-91a4-980370aa45c3/e911dd42abea2617e625d2547de8038a3e9a42b47097ad570d4b68b1ce25dba9?_ga=1.134668273.1418643578.1461496136

3:Now go to another browser where no authentication is done, now open the same url in Google Chrome

4:After link got opened, now going to modify the subscription setting -(i.e. subscription setting Uber Global Updates -Unchecked)


5:Now Again go to Browser Firefox and refresh the same url as a result of previous step subscription setting got updated

i.e. Uber Global Updates  gets  -Unchecked  from checked


I am successfully able to update the Subscription Setting of an authenticated user anonymously

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
