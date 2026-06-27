---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '148903'
original_report_id: '148903'
title: Airship doesn't reject weak passwords
weakness: Improper Authentication - Generic
team_handle: paragonie
created_at: '2016-07-02T19:17:57.769Z'
disclosed_at: '2016-07-02T20:32:01.708Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- improper-authentication-generic
---

# Airship doesn't reject weak passwords

## Metadata

- HackerOne Report ID: 148903
- Weakness: Improper Authentication - Generic
- Program: paragonie
- Disclosed At: 2016-07-02T20:32:01.708Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Airship doesn't reject weak passwords for the initial account. It happily accepts the password `test` for a root user `test`. This isn't a vulnerability in the software itself, but it's still listed in [vulnerabilities we prevent](https://github.com/paragonie/airship-docs/blob/master/en-us/WHY.md#vulnerabilities-we-prevent):

> **Broken Authentication**
> Airship rejects weak passwords that hackers could easily guess.

Feel free to close this as informative, but I think it's still security related, so I'll report it here.

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
