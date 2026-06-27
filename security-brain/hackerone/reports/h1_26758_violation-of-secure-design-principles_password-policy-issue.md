---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '26758'
original_report_id: '26758'
title: Password Policy issue
weakness: Violation of Secure Design Principles
team_handle: phabricator
created_at: '2014-09-02T23:07:10.863Z'
disclosed_at: '2014-10-02T23:11:02.269Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# Password Policy issue

## Metadata

- HackerOne Report ID: 26758
- Weakness: Violation of Secure Design Principles
- Program: phabricator
- Disclosed At: 2014-10-02T23:11:02.269Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello 
I hope you are doing fine. This is a very low severity issue that i just found out in your password policy. You have a good password policy implemented with the special characters and uppercase letters and stuff but the thing is that you do not check for passwords similar to the other fields. Like if someone has put their email as same as their password or their username or real name as same as their password, there is no check for this. Which leaves the account vulnerable to guessing attacks because we of all the world know that the attacker initially goes for the similarities.

You could reproduce this by signing up for an account that has real name that is same the email address that is as username that is as same as the password (ignoring the @ and the . in the email offcourse because that is not accepted). This should be checked

Hope this helps. Awaiting your reply

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
