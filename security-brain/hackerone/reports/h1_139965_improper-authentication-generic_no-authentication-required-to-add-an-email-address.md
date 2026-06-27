---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '139965'
original_report_id: '139965'
title: No authentication required to add an email address.
weakness: Improper Authentication - Generic
team_handle: phabricator
created_at: '2016-05-20T15:49:07.688Z'
disclosed_at: '2016-05-27T00:55:50.533Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- improper-authentication-generic
---

# No authentication required to add an email address.

## Metadata

- HackerOne Report ID: 139965
- Weakness: Improper Authentication - Generic
- Program: phabricator
- Disclosed At: 2016-05-27T00:55:50.533Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi Team,
I hope this mongoose I'm sending will help make phabricator safer.

Description:
==========
The issue in question, is that whenever you add a new email address to your account, no additional authentication is required. Furthermore, when the account has 2FA enabled, it's not necessary to enter high security mode when adding a new email address (But it is necessary to authenticate and login).

Of course a malicious individual would have to have access to an open account or hijack the session cookie. But since the session cookies have a long expiration period, it makes this attack more plausible. Specially considering that most people don't logout of their accounts when they are done using them, they just close the tab/browser.

Impact:
=======
A malicious individual with access to an account, can add and validate an email address which can later on be used to get a one time login link and change the user password, thus compromising the account completely.

Recommendation:
===============
Enforce asking the user for the account password prior to adding the new email address. In addition, if 2FA is active on the account, require high security mode to add a new email address.

I'm attaching screenshots of a step by step.
Kind Regards,
Alex.

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
