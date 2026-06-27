---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '119808'
original_report_id: '119808'
title: DROWN Attack
weakness: Cryptographic Issues - Generic
team_handle: owncloud
created_at: '2016-03-01T16:45:30.958Z'
disclosed_at: '2016-03-03T16:28:14.314Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cryptographic-issues-generic
---

# DROWN Attack

## Metadata

- HackerOne Report ID: 119808
- Weakness: Cryptographic Issues - Generic
- Program: owncloud
- Disclosed At: 2016-03-03T16:28:14.314Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I want to report a drown attack in *.owncloud.com.

A cross-protocol attack was discovered that could lead to decryption of TLS
sessions by using a server supporting SSLv2 and EXPORT cipher suites as a
Bleichenbacher RSA padding oracle.  Note that traffic between clients and
non-vulnerable servers can be decrypted provided another server supporting
SSLv2 and EXPORT ciphers (even with a different protocol such as SMTP, IMAP or
POP) shares the RSA keys of the non-vulnerable server. This vulnerability is
known as DROWN (CVE-2016-0800).

You can check here: https://test.drownattack.com/?site=owncloud.com

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
