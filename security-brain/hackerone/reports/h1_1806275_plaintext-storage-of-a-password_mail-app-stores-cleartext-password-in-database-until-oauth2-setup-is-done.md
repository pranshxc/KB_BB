---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1806275'
original_report_id: '1806275'
title: Mail app stores cleartext password in database until OAUTH2 setup is done
weakness: Plaintext Storage of a Password
team_handle: nextcloud
created_at: '2022-12-15T10:21:14.461Z'
disclosed_at: '2023-03-08T09:49:01.303Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
asset_identifier: nextcloud/mail
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- plaintext-storage-of-a-password
---

# Mail app stores cleartext password in database until OAUTH2 setup is done

## Metadata

- HackerOne Report ID: 1806275
- Weakness: Plaintext Storage of a Password
- Program: nextcloud
- Disclosed At: 2023-03-08T09:49:01.303Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

The Mail app usually stores the user password encrypted. For XOAUTH2 the encrypted access token is stored in the same columns. However, during the time of the setup, XOAUTH2 accounts have the password in clear text in the database.

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  0. Configure Gmail Oauth client ID and secret as Nextcloud admin
  1. Open the Mail app
  2. Open the setup page
  3. Enter values for display name
  4. Enter a random value for the password
  5. Enter the gmail address

-> password field hides

  6. Continue the setup

Once the Gmail consent popup shows, look into oc_mail_accounts and the last entry.

inbound_password and outbound_password have the random value entered for the password.

## Supporting Material/References:

  * N/A

## Impact

A DBA could read the plaintext password

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
