---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1552110'
original_report_id: '1552110'
title: OAUTH2 bearer not-checked for connection re-use
weakness: Improper Authentication - Generic
team_handle: ibb
created_at: '2022-04-27T16:16:35.630Z'
disclosed_at: '2022-04-29T11:34:09.285Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# OAUTH2 bearer not-checked for connection re-use

## Metadata

- HackerOne Report ID: 1552110
- Weakness: Improper Authentication - Generic
- Program: ibb
- Disclosed At: 2022-04-29T11:34:09.285Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

libcurl might reuse OAUTH2-authenticated connections without properly making
sure that the connection was authenticated with the same credentials as set
for this transfer. This affects SASL-enabled protcols: SMTP(S), IMAP(S),
POP3(S) and LDAP(S) (openldap only).

libcurl maintains a pool of connections after a transfer has completed. The
pool of connections is then gone through when a new transfer is requested and
if there's a live connection available that can be reused, it is preferred
instead of creating a new one.

A connection that is successfully created and authenticated with a user name +
OAUTH2 bearer could subsequently be reused even for user + [other OAUTH2
bearer], even though that might not even be a valid bearer. This could lead to
an authenticion bypass, either by mistake or by a malicious actor.

The problem can be demontrated using an imap server supporting OAUTH2 authentication using command:

`curl 'imap://server:port/path/;MAILINDEX=1' --login-options 'AUTH=OAUTHBEARER' -u user: --oauth2-bearer validbearer --next 'imap://server:port/path/;MAILINDEX=1' --login-options 'AUTH=OAUTHBEARER' -u user: --oauth2-bearer anything`

Note:
This vulnerability has been assigned CWE-305 "Authentication Bypass by Primary Weakness" that is not selectable on the current IBB form.

## Impact

Unauthorized access.

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
