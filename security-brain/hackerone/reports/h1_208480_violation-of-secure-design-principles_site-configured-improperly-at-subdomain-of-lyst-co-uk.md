---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '208480'
original_report_id: '208480'
title: Site configured improperly at subdomain of lyst.co.uk
weakness: Violation of Secure Design Principles
team_handle: lyst
created_at: '2017-02-23T20:03:27.095Z'
disclosed_at: '2017-03-29T11:59:17.954Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 17
tags:
- hackerone
- violation-of-secure-design-principles
---

# Site configured improperly at subdomain of lyst.co.uk

## Metadata

- HackerOne Report ID: 208480
- Weakness: Violation of Secure Design Principles
- Program: lyst
- Disclosed At: 2017-03-29T11:59:17.954Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Steps to reproduce the issue:

Go to : "https://w.lyst.co.uk/"

It will give you message

```
The owner of w.lyst.co.uk has configured their website improperly.
To protect your information from being stolen, 
Firefox has not connected to this website.
```
Image:
{F163225}
A attacker will send this link to user, where he will be shown this message, will break her/his trust from lyst.

Tested in Firefox latest version.

Thanks

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
