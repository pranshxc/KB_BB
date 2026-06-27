---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '242622'
original_report_id: '242622'
title: Possible User Session Hijack using Invalid HTTPS certificate on inside.gratipay.com
  domain
weakness: Violation of Secure Design Principles
team_handle: gratipay
created_at: '2017-06-23T14:27:45.366Z'
disclosed_at: '2017-06-24T14:00:56.967Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# Possible User Session Hijack using Invalid HTTPS certificate on inside.gratipay.com domain

## Metadata

- HackerOne Report ID: 242622
- Weakness: Violation of Secure Design Principles
- Program: gratipay
- Disclosed At: 2017-06-24T14:00:56.967Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Good evening team!

This is a theoretical risk but I thought it was still worth reporting since every endpoint and any data flowing through inside.gratipay.com is unencrypted.

POC

https://inside.gratipay.com

And every sub directory under inside.gratipay.com.

Description

Since the certificate is only valid through *.herokuapp.com the domain is sending a warning message about MITM attacks. This warning is valid because all data is not being HTTPS encrypted.

The warning is also pretty scary to anyone browsing inside.gratipay.com for information on how to contribute.

Browsers Verified In

Chrome
Firefox
Patch

Add a valid certificate on inside.gratipay.com.

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
