---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '241892'
original_report_id: '241892'
title: Possible user session hijack by invalid HTTPS certificate on inside.gratipay.com
  domain
weakness: Violation of Secure Design Principles
team_handle: gratipay
created_at: '2017-06-21T07:20:17.679Z'
disclosed_at: '2017-06-21T14:30:21.715Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# Possible user session hijack by invalid HTTPS certificate on inside.gratipay.com domain

## Metadata

- HackerOne Report ID: 241892
- Weakness: Violation of Secure Design Principles
- Program: gratipay
- Disclosed At: 2017-06-21T14:30:21.715Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Good evening team!

This is a theoretical risk but I thought it was still worth reporting since every endpoint and any data flowing through inside.gratipay.com is unencrypted. 

# POC

https://inside.gratipay.com

And every sub directory under inside.gratipay.com.
# Description

Since the certificate is only valid through  *.herokuapp.com the domain is sending a warning message about MITM attacks. This warning is valid because all data is not being HTTPS encrypted. 

The warning is also pretty scary to anyone browsing inside.gratipay.com for information on how to contribute.

# Browsers Verified In

  * Chrome
  * Firefox

# Patch

Add a valid certificate on inside.gratipay.com.

Stay classy, you guys rock. *Nerd emoji*.

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
