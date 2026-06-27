---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7894'
original_report_id: '7894'
title: Full path disclosure
weakness: Information Disclosure
team_handle: localize
created_at: '2014-04-17T19:20:29.468Z'
disclosed_at: '2014-04-18T05:18:04.083Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Full path disclosure

## Metadata

- HackerOne Report ID: 7894
- Weakness: Information Disclosure
- Program: localize
- Disclosed At: 2014-04-18T05:18:04.083Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I signed up for localize with haxorsistz@gmail.com, and localize sent me a verification link which was:
`http://www.localize.io/verify/e6be646b24pdd3w6d5c27ppa9a267ee7`
When I visited that link I found it was showing the following error:
`Fatal error: Call to a member function setEmail_lastVerificationAttempt() on a non-object in /var/www/vhosts/lvps178-77-99-228.dedicated.hosteurope.de/httpdocs_localize/index.php on line 120 `
which includes the full path of the website.This should be mitigated.

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
