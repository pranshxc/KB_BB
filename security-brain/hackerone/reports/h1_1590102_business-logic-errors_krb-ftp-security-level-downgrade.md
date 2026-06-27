---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1590102'
original_report_id: '1590102'
title: 'KRB-FTP: Security level downgrade'
weakness: Business Logic Errors
team_handle: curl
created_at: '2022-06-02T20:58:34.467Z'
disclosed_at: '2022-06-05T20:58:34.335Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 1
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# KRB-FTP: Security level downgrade

## Metadata

- HackerOne Report ID: 1590102
- Weakness: Business Logic Errors
- Program: curl
- Disclosed At: 2022-06-05T20:58:34.335Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

## Summary:
libcurl doesn't fail the FTP connection if Kerberos authentication fails for some reason, but rather reverts back to using regular clear text password authentication.

The logic is in`lib/ftp.c` `ftp_statemachine`: https://github.com/curl/curl/blob/07a9b89fedaec60bdbc254f23f66149b31d2f8da/lib/ftp.c#L2706

This means that active attacker in a man in the middle position can downgrade any attempt to use Kerberos FTP to regular one by merely forcing the Kerberos authentication to fail.

The more secure course of action would be to fail the FTP connection if Kerberos authentication fails. If such change is not deemed necessary the current limitations should be documented.

## Steps To Reproduce:

  1. MitM the connection and make the kerberos authentication fail
  2. `curl --krb private ftp://victim.tld/`

## Impact

- Security level downgrade.

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
