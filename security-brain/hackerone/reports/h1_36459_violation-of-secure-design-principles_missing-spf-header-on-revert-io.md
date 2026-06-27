---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '36459'
original_report_id: '36459'
title: Missing SPF header on revert.io
weakness: Violation of Secure Design Principles
team_handle: thisdata
created_at: '2014-11-17T23:09:18.039Z'
disclosed_at: '2015-01-18T19:45:22.283Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# Missing SPF header on revert.io

## Metadata

- HackerOne Report ID: 36459
- Weakness: Violation of Secure Design Principles
- Program: thisdata
- Disclosed At: 2015-01-18T19:45:22.283Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I noticed that there is no TXT record containing a SPF header:

#PoC
```
> dig TXT revert.io +short
"google-site-verification=ix6OUwvbN9AJLTcdg3ulWcMibIWGgUy_zWEXrWeRYE4"
```

The [SPF Header](http://de.wikipedia.org/wiki/Sender_Policy_Framework) can be used to prevent phishers from impersonating you/your company in the emails' FROM header. 

#Fix
You can fix that by generating an SPF-TXT record with all your outgoing mailservers.

All the best,
Sebastian

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
