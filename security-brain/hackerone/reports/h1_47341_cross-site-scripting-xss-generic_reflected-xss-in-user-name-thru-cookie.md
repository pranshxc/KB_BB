---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '47341'
original_report_id: '47341'
title: Reflected xss in user name thru cookie
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mobilevikings
created_at: '2015-02-10T17:52:52.908Z'
disclosed_at: '2015-03-04T14:21:29.773Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected xss in user name thru cookie

## Metadata

- HackerOne Report ID: 47341
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mobilevikings
- Disclosed At: 2015-03-04T14:21:29.773Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Imagine, that we have user A with name - name<script>alert(1)</script>
And user B
User B request a sim card and the Add authorization to user A (of course this is not the common way to exploit).
As a result we have xss thru user name in flash message thru cookie.
And (!) we got properly singed cookie with xss payload
messages="29972147bc558baf382bbeb0b829d4efec82de2f$[[\"__json_message\"\0540\05425\054\"Authorization will be given to name<script>alert(1)</script> once this user confirms.\"]]"; Path=/

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
