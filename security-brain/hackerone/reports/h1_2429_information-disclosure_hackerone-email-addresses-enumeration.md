---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2429'
original_report_id: '2429'
title: Hackerone Email Addresses Enumeration
weakness: Information Disclosure
team_handle: security
created_at: '2014-02-28T14:53:23.932Z'
disclosed_at: '2016-06-17T23:45:16.010Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 24
tags:
- hackerone
- information-disclosure
---

# Hackerone Email Addresses Enumeration

## Metadata

- HackerOne Report ID: 2429
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2016-06-17T23:45:16.010Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Enumeration of email addresses of already registered users is possible, and or, checking if a user with specific email address is registered in the website  and will then be used for phising attacks or any malicious intent.

In the "Forgot Password" section, there is an implemented security measure regarding this specific flaw.

The page does not disclose anything to someone who does not own that email address..

See attached ( hackerone1.jpg )

But, in the registration form. It defeats the implementation against "email address enumeration," since it currently displays, "email has already taken" when an attacker tried to register of an already registered email address.

See attached ( hackerone2.jpg )

I have read this workaround in a post by sir Troy Hunt,  sending an email, a notification that the user is already registered ( if registered ) or a link to continue the registration process ( if still not registered ).

I believe, security weighs more than usability here and it does not hamper again, hackerone's usability.

Thank you very much.

Cheers,
Clifford Trigo

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
