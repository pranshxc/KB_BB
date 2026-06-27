---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '789260'
original_report_id: '789260'
title: Past payments using the Direct Debit method keep subscriptions active even
  if payments fail
weakness: Business Logic Errors
team_handle: nordsecurity
created_at: '2020-02-05T11:30:02.580Z'
disclosed_at: '2020-02-21T11:27:54.857Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
asset_identifier: '*.nordvpn.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Past payments using the Direct Debit method keep subscriptions active even if payments fail

## Metadata

- HackerOne Report ID: 789260
- Weakness: Business Logic Errors
- Program: nordsecurity
- Disclosed At: 2020-02-21T11:27:54.857Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I think this is a vulnerability that has no impact but it violates

I found many accounts that are actively subscribed even though the payment failed, this is because the payment uses the Direct Debit method, and you have deleted it.

Because Direct Debit payments have been deleted and no longer work or can be used or cannot be detected by the system, maybe because of this the system considers payments to be legitimate and gets a subscription.

Maybe you can deactivate all subscriptions for accounts that don't have successful payments.

I know this is not a vulnerability that I report, but this is an invasion of your site's privacy.

thanks.

## Impact

Payment failed but get a subscription.

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
