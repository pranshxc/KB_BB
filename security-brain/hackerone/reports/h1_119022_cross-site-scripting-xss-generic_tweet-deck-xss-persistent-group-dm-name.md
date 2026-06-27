---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '119022'
original_report_id: '119022'
title: Tweet Deck XSS- Persistent- Group DM name
weakness: Cross-site Scripting (XSS) - Generic
team_handle: x
created_at: '2016-02-26T22:08:11.093Z'
disclosed_at: '2016-03-04T19:03:47.498Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Tweet Deck XSS- Persistent- Group DM name

## Metadata

- HackerOne Report ID: 119022
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: x
- Disclosed At: 2016-03-04T19:03:47.498Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Hello**

Group names in tweetdeck.twitter.com aren't filtered properly, giving scope for Cross site vulnerability attacks.
Challenge I have faced while escalating the xss:
- group name can only be 9 character long.

How i bypassed it:
Set multiple group names with different payloads, which means we can craft a good lengthy xss exploit using multiple group names.

Steps to reproduce:
- Create a Twitter DM group on twitter.com with group name ``<script>alert(1);//``
- go to https://tweetdeck.twitter.com/ to trigger the xss

Exploitation:
Group names can be changed by any user in the group
you can invite any user to https://tweetdeck.twitter.com/

Screenshot attached.

Environment : 
Works on all modern browsers

**Regards,
WeSecureApp**

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
