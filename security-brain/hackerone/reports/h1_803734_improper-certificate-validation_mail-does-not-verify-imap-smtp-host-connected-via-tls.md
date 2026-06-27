---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '803734'
original_report_id: '803734'
title: Mail does not verify IMAP/SMTP host connected via TLS
weakness: Improper Certificate Validation
team_handle: nextcloud
created_at: '2020-02-24T14:56:20.816Z'
disclosed_at: '2020-06-03T08:13:31.148Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- improper-certificate-validation
---

# Mail does not verify IMAP/SMTP host connected via TLS

## Metadata

- HackerOne Report ID: 803734
- Weakness: Improper Certificate Validation
- Program: nextcloud
- Disclosed At: 2020-06-03T08:13:31.148Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The Mail app should verify that the servers it connects to are listed in the certificate's CN. Otherwise the connection should be aborted.

Originally reported at https://github.com/nextcloud/mail/issues/308

## Impact

The app could be forced into connecting to an insecure server.

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
