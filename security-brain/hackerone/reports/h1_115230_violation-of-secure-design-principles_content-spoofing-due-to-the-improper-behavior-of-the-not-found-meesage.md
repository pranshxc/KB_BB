---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '115230'
original_report_id: '115230'
title: Content spoofing due to the improper behavior  of the not-found meesage
weakness: Violation of Secure Design Principles
team_handle: keybase
created_at: '2016-02-07T17:11:30.230Z'
disclosed_at: '2016-02-08T15:37:35.004Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# Content spoofing due to the improper behavior  of the not-found meesage

## Metadata

- HackerOne Report ID: 115230
- Weakness: Violation of Secure Design Principles
- Program: keybase
- Disclosed At: 2016-02-08T15:37:35.004Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hay ,

At dist.keybase.io , It's possible to inject text in the not-found message in order to trick the user to make him visit website or do something an attacker might be interested in .

PoC :
https://goo.gl/3WO6iH 

I've shortened this one because it's really long , it's needed to be on google chrome , maximized window , bookmarks bar hidden and screen with 1366 x 768 resolution in order to be displayed like image 1.png 

That was complicated , I know , but it was just to prove the point that it can be modified to be more convincing  .

here's   the simple PoC 

https://dist.keybase.io////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////However,it.has.been.moved.to.our.new.website.at.HTTP://EVIL.ATTACKER.COM////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

I think it's not a very good idea to return the user input in the not-found message body , I also think it's easy to fix .

Happy fixing ,
Enjoy your weekend ,

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
