---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145452'
original_report_id: '145452'
title: Share owner has no possibility to list all existing derived shares
weakness: Improper Authentication - Generic
team_handle: nextcloud
created_at: '2016-06-17T15:52:32.076Z'
disclosed_at: '2016-12-13T16:20:08.706Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- improper-authentication-generic
---

# Share owner has no possibility to list all existing derived shares

## Metadata

- HackerOne Report ID: 145452
- Weakness: Improper Authentication - Generic
- Program: nextcloud
- Disclosed At: 2016-12-13T16:20:08.706Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I found a bug where a shared link of particular file can disclose all files of that folder. 

###Steps to reproduce

+ Make a group( ```http://*/nextcloud/index.php/settings/users```) and a standard user in it.
+ Now goto any folder and change it to gallery view
{F99993}

+ Invite that group which u made in step 1 with ``share`` privilege .
+ From standard user account, goto that shared folder and make a shared link of any file. E.g:

{F99992}

+ Untick the ``can share`` privilege from that group using folder owner account. Eg: 

{F99994}




Now the shared link which was created by standard user will work as folder shared link. And when folder untick the ``can share`` privilege public is automatically created without asking folder owner.

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
