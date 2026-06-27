---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '42161'
original_report_id: '42161'
title: stored xss in transaction
weakness: Cross-site Scripting (XSS) - Generic
team_handle: enter
created_at: '2014-12-30T12:51:58.437Z'
disclosed_at: '2015-04-03T14:00:56.349Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# stored xss in transaction

## Metadata

- HackerOne Report ID: 42161
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: enter
- Disclosed At: 2015-04-03T14:00:56.349Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

1. Open wallet settings and remove maxlength="30" from wallet name input
2. Change name to something like this  asdf'"><script>alert(1)</script>
3. Go to "Send bitcoin" and make inbound transfer from one wallet to another with description: desc<script>alert('xss in description')</script>
4. Submit form
5. After submit we got xss both in "from account" name and "to account" name
6. Go to transaction history https://wallet.robocoin.com/account/6428d1d8-c499-46ab-8587-74260d898f34
7. Open single transaction details and we got xss in  "from account" name, "to account" name and description.
"To Robocoin wallet" feature has the same fields "from account" and description and may be also affected. If you approve my second account white.hat.audit@gmail.com i will test it. And i think that this issue may affect admin panel.

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
