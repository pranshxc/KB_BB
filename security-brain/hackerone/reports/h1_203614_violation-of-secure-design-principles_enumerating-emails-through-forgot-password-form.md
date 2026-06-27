---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '203614'
original_report_id: '203614'
title: Enumerating emails through "Forgot Password" form
weakness: Violation of Secure Design Principles
team_handle: phabricator
created_at: '2017-02-05T14:04:09.274Z'
disclosed_at: '2017-02-06T12:04:09.421Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# Enumerating emails through "Forgot Password" form

## Metadata

- HackerOne Report ID: 203614
- Weakness: Violation of Secure Design Principles
- Program: phabricator
- Disclosed At: 2017-02-06T12:04:09.421Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

mongoose mongoose mongoose

Hi! I am testing typical local installation of Phabricator.

Using the forgot password form it is possible to enumerate users emails because of message `There is no account associated with that email address.`. So attacker theoretically can figure out registered users emails and use that information later (for example, bruteforce credentials).

I think there is no need to informate user if that account is exists or not. Or you can make option to show or not show this kind of information.

Of course, you can say that there is recaptcha on login form, but in **TYPICAL** installation recaptcha is disabled, and I had no setup issues messages about that fact (for example *"Unresolved setup issue: Please enable recaptcha validation to decrease risk of bruteforcing users credentials. Resolve or ignore"*).

Be free to ask me more information.

Regards, Denis Pugachev

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
