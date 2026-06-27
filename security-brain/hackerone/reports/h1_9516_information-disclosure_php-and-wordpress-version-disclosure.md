---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '9516'
original_report_id: '9516'
title: PHP and Wordpress version disclosure
weakness: Information Disclosure
team_handle: iandunn-projects
created_at: '2014-04-24T09:47:52.725Z'
disclosed_at: '2014-06-11T08:56:57.482Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# PHP and Wordpress version disclosure

## Metadata

- HackerOne Report ID: 9516
- Weakness: Information Disclosure
- Program: iandunn-projects
- Disclosed At: 2014-06-11T08:56:57.482Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

**Vulnerable File**
google-authenticator-per-user-prompt/views/requirements-error.php

**Description**
That file discloses the PHP version and Wordpress version to the world.Which is not a bug actually,but these information can be helpful to demonstrate further devastating bugs.

**Suggestion**
I saw that you rejected many path disclosure reports cause those are not in your hand.It depends upon server settings,how that will handle error messages.But this case is different.Its not actually an error message.And cant be mitigated by switching off error display.
I suggest you to keep such actions so that unauthorized users could not use this file directly.

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
