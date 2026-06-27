---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2224'
original_report_id: '2224'
title: Bypass auth.email-domains
weakness: Improper Authentication - Generic
team_handle: phabricator
created_at: '2014-02-23T16:08:39.974Z'
disclosed_at: '2014-03-25T18:23:30.689Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- improper-authentication-generic
---

# Bypass auth.email-domains

## Metadata

- HackerOne Report ID: 2224
- Weakness: Improper Authentication - Generic
- Program: phabricator
- Disclosed At: 2014-03-25T18:23:30.689Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Email addresses are stored as `VARCHAR(128)`. However, Phabricator does not verify the length of an email address upon registration. This allows attackers to bypass the allowed email-domains defined in `auth.email-domains`.

Exploiting this is rather straightforward: get an email address of 128 characters long ([This StackOverflow answer](http://stackoverflow.com/a/574698/2425609) indicates that the maximum length of an email address is 254 characters). Now register with your 128 character email address with `@allowed-domain.com` appended to it. The `@allowed-domain.com` part will be truncated because MySQL can’t store it, and you will receive a verification email on your 128 character email address.

This is especially easy if you’re using a Gmail address: if you own `attacker@gmail.com`, you’ll also receive any mails sent to `attacker+aaaaaaaaaaa…aaa@gmail.com`.

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
