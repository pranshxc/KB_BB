---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '92716'
original_report_id: '92716'
title: HackerOne Private Programs users disclosure and de-anonymous-ize
weakness: Information Disclosure
team_handle: security
created_at: '2015-10-07T06:58:37.515Z'
disclosed_at: '2015-12-08T04:18:04.456Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
- information-disclosure
---

# HackerOne Private Programs users disclosure and de-anonymous-ize

## Metadata

- HackerOne Report ID: 92716
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2015-12-08T04:18:04.456Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi HackerOne Team,
I have found a bug in HackerOne Platform allows any attacker to deanonymousize any security researcher using the platform and the most wild usage is to disclose some information about this security researcher if he is invited to a private program or not.
Unfortunately HackerOne is replying 404 response to the non-found researchers/programs this will allow attackers to harvest and deanonymousize researchers/programs.

In-depth analysis:
[*]When user is logged out and start to hit a private hackerone program link so we have this response code states:
302 means program is exist but you have to sign in to check if you're eligible to see it or not
404 means there is no program yet
200 any user is able to access this program / program is public

[*]When the user is logged in and start to hit a private hackerone program link so we have this response code states::
404 means you're not invited to this program / program is not exist yet "onerror event is triggered"
200 means you're eligible to see the program "onload event is triggered"

PoC Code:
<html>
<script src="https://hackerone.com/bookingcom" onload="javascript:alert('Yes the logged in user is invited to this private program and there is a program called bookingcom for sure');" onerror="javascript:alert('No, This user is not invited to this private program or there is no private program called bookingcom');"></script>
</html>

PoC Video:
https://youtu.be/Z_NBSNBxarY

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
