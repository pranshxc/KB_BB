---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '477'
original_report_id: '477'
title: Flawed account creation process allows registration of usernames corresponding
  to existing file names
team_handle: security
created_at: '2013-11-30T11:42:13.022Z'
disclosed_at: '2014-04-19T20:59:27.067Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
---

# Flawed account creation process allows registration of usernames corresponding to existing file names

## Metadata

- HackerOne Report ID: 477
- Weakness: 
- Program: security
- Disclosed At: 2014-04-19T20:59:27.067Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

As requested by Alex:
"You mentioned in the report to contact you on this account instead. Is this the email address you prefer to use for payment? If so, would you mind resubmitting the issue from this account so we can issue a payout to the proper account?"

----------

The account creation process allows to set up account names corresponding to names of server ressources, e.g. I just successfully created an account robots.txt which results in a profile path of https://hackerone.com/robots.txt and results in an bugged account as accessing account settings etc is impossible.

I'd recommend moving away from filtering names and from profiles being available directly under .com/ and changing it to something more reliable like .com/users/profilename

The robots.txt account can be deleted. I only created it for testing purpose.

Cheers,
Florian

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
