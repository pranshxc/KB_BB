---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '201314'
original_report_id: '201314'
title: Enumeration in unsubscribe -function of /omatalousuk (viestinta.lahitapiola.fi)
weakness: Privilege Escalation
team_handle: localtapiola
created_at: '2017-01-26T10:37:41.761Z'
disclosed_at: '2017-02-04T19:07:20.036Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- privilege-escalation
---

# Enumeration in unsubscribe -function of /omatalousuk (viestinta.lahitapiola.fi)

## Metadata

- HackerOne Report ID: 201314
- Weakness: Privilege Escalation
- Program: localtapiola
- Disclosed At: 2017-02-04T19:07:20.036Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,
I would like to report an issue where malicious user can unsubscribe any customer email subscription from viestinta.lahitapiola.fi. 
I am not sure if this in scope, but i took the liberty to bring forward to you, so that you can fix the bug.

**Impact**
Subscribe or unsubscribe is always a personal/customer choice. but what if a malicious user unsubscribe without the knowledge/Authority of the valuable customer who would like to get a regular update from the company? What if an attacker unsubscribe ALL the customer email subscription? I assume finding valid email of customers would not be big deal for an Attacker.
Hence, this could impact company's business.  

**Step to reproduce**:
Goto
http://viestinta.lahitapiola.fi/webApp/omatalousuk?email=

in the ```email=``` param enter any email id
for example, enter```abcd123@gmail.com``` will get a respond ```No customer found, cannot unsubscribe```
for a vaild customer email, ```test@gmail.com``` will get a respond ```Unsubscribe```

with this, a malicious user would exploit this vulnerability.

I've attach some screen shot of execution.
Thank you.

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
