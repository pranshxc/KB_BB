---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '4795'
original_report_id: '4795'
title: Bypass auth.email-domains
weakness: Improper Authentication - Generic
team_handle: concretecms
created_at: '2014-03-25T20:57:05.737Z'
disclosed_at: '2014-04-30T18:16:12.824Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- improper-authentication-generic
---

# Bypass auth.email-domains

## Metadata

- HackerOne Report ID: 4795
- Weakness: Improper Authentication - Generic
- Program: concretecms
- Disclosed At: 2014-04-30T18:16:12.824Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Email addresses are stored as VARCHAR(64). the length is verified on client side only , using a proxy(temper data) attacker can add  longer length email which can be further abused .Exploiting this is rather straightforward: get an email address of 128 characters long . Now register with your 128 character email address with @allowed-domain.com appended to it. The @allowed-domain.com part will be truncated because MySQL can’t store it, and you will receive a verification email on your 128 character email address.

This is especially easy if you’re using a Gmail address: if you own attacker@gmail.com, you’ll also receive any mails sent to attacker+aaaaaaaaaaa…aaa@gmail.com.

snap attached : a POC for a truncated email address

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
