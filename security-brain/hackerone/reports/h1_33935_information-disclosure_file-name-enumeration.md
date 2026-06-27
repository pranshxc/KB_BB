---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '33935'
original_report_id: '33935'
title: File Name Enumeration
weakness: Information Disclosure
team_handle: security
created_at: '2014-11-04T20:21:36.697Z'
disclosed_at: '2014-11-17T22:28:55.710Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- information-disclosure
---

# File Name Enumeration

## Metadata

- HackerOne Report ID: 33935
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2014-11-17T22:28:55.710Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi guys,
I am kind of surprised no one hast reported this issue yet.
 (or maybe they have and due to the severity it was never patched?)

An example of this behavior would be:

https://hackerone.com//%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd  (which is a valid attempt even though we get an error saying file not found because..)

https://hackerone.com//%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd_DOESNTEXIST will rediredt us to a 404 page.


Let me know if you need more info from my end.

Thanks,
Ben

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
