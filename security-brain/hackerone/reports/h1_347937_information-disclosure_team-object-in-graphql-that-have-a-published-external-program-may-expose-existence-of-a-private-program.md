---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '347937'
original_report_id: '347937'
title: Team object in GraphQL that have a published external program may expose existence
  of a private program
weakness: Information Disclosure
team_handle: security
created_at: '2018-05-06T11:52:03.871Z'
disclosed_at: '2018-07-04T05:29:18.853Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 38
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Team object in GraphQL that have a published external program may expose existence of a private program

## Metadata

- HackerOne Report ID: 347937
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2018-07-04T05:29:18.853Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

Hi Team!

On Team object the parameter "i_cannot_create_jira_webhook_reasons" is not NULL and gets the following default states when called for all programs ["CANNOT_VIEW","FEATURE_GATED","PROGRAM_PERMISSION_REQUIRED"]

If a Company Program runs a Private Program or a Public On the "FEATURE_GATED" is missing (Since the feature is not gated anymore) and therefore an attacker can find if a Company is running a private program

##POC

* Company ██████ (not runnig private gives "i_cannot_create_jira_webhook_reasons":["CANNOT_VIEW","FEATURE_GATED","PROGRAM_PERMISSION_REQUIRED"]

* Company █████████ (running private) gives "i_cannot_create_jira_webhook_reasons":["CANNOT_VIEW","PROGRAM_PERMISSION_REQUIRED"]

* Even Company HackerOne  (running public) gives "i_cannot_create_jira_webhook_reasons":["CANNOT_VIEW","PROGRAM_PERMISSION_REQUIRED"]

All private programs and public has an overriden  "FEATURE_GATED" so you get the idea

#Solutiion

NULL the value maybe

PS: Thanks to @jobert who encouraged me to search deeper after the #347383 duplicate!

Thanks
**nismo**

## Impact

Knowing companies that run private programs on Hackerone

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
