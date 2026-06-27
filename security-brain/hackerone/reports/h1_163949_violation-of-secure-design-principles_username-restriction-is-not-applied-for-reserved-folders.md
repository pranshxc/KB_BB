---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '163949'
original_report_id: '163949'
title: Username Restriction is not applied for reserved folders
weakness: Violation of Secure Design Principles
team_handle: gratipay
created_at: '2016-08-28T07:50:17.569Z'
disclosed_at: '2016-12-30T07:46:36.420Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# Username Restriction is not applied for reserved folders

## Metadata

- HackerOne Report ID: 163949
- Weakness: Violation of Secure Design Principles
- Program: gratipay
- Disclosed At: 2016-12-30T07:46:36.420Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,

This issue is same as #128121 reported by a5tronaut.
He reported some of the usernames for restriction and you applied check only for those usernames. 
I think username restriction should applied for all the usersnames, those are used for a directory or a link in gratipay.

a5tronaut mentioned the sign-out.html. You restricted it but sign-out still is an available username. 

Like gratipay have the directory listing for following:
Profile, Giving , History, Emails, Routes, Settings.

But none of the above is restricted for use as an username.

I created my account of three of above username for POC purpose. When User of gratipay will click on the following link, he would expect the history, sign-out, settings page of gratipay. But he will end up visiting my gratipay account. 

**POC:**
https://gratipay.com/sign-out/
https://gratipay.com/History/
https://gratipay.com/settings/

**Fix:** 
You can fix most of this username restriction issues by not allowing . (dot) in username as i suggested in my previous report and other usernames without "." dot can be restricted explicitly.

Thanks,
Akash Saxena

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
