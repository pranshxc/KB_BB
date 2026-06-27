---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '36211'
original_report_id: '36211'
title: 'Logic Issue with Reputation: Boost Reputation Points'
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2014-11-16T16:06:58.345Z'
disclosed_at: '2015-04-28T04:51:43.873Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- violation-of-secure-design-principles
---

# Logic Issue with Reputation: Boost Reputation Points

## Metadata

- HackerOne Report ID: 36211
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2015-04-28T04:51:43.873Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I'm disclosing a bug that can allow a program member to escalate a profile reputation by +2 points indefinitely till the extent he/she wants and the process will be somewhat stealthy as there won't be a trace on member's profile (say fake resolved bugs etc). 


**Prologue**

BugBug - Imaginary program at HackerOne
User A - Member of BugBug  at HackerOne
User B - A test account
User C - Another test account

**Issue and Repro**

1. Create a ticket with user B at BugBug
2. Create a ticket with user C at BugBug
3. Mark user C's ticket as resolved 
4. Mark user B's ticket as Duplicate of user C's ticket
5. Now reopen user C's ticket and mark it as resolved.
6. Repeat the last step, that is step 5 for 50 times and you'll see user B's reputation will boost up by 100 points. And of course there won't be any trace on user B's profile publicly as the ticket is marked duplicate.  

P.S: All program associated steps are done by user A like marking ticket as resolved/dupe


To avoid confusion here's a short video as well - [Dropbox](https://www.dropbox.com/s/rsaa6havq08fk7p/Reputation%20Logic.mov?dl=0)

Thanks,
Prakhar Prasad

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
