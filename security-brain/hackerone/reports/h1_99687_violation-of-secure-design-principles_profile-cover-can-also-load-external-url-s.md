---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '99687'
original_report_id: '99687'
title: profile cover can also load external URL's
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2015-11-14T17:48:38.493Z'
disclosed_at: '2015-12-02T10:48:08.841Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- violation-of-secure-design-principles
---

# profile cover can also load external URL's

## Metadata

- HackerOne Report ID: 99687
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2015-12-02T10:48:08.841Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I have to option to change my cover background (https://hackerone.com/{program_name}/edit). 
When I insert `#360e0e url('http://www.google.com')` as background "color" it will make a connection to http://www.google.com (If IE is used).

I can't save it so it won't affect any other people but it doesn't look "by design".

Kind regards,

Olivier

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
