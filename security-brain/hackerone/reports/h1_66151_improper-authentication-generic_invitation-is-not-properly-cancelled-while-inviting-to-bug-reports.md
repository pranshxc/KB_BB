---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '66151'
original_report_id: '66151'
title: Invitation is not properly cancelled while inviting to bug reports.
weakness: Improper Authentication - Generic
team_handle: security
created_at: '2015-06-05T14:05:01.385Z'
disclosed_at: '2015-07-10T00:32:32.240Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# Invitation is not properly cancelled while inviting to bug reports.

## Metadata

- HackerOne Report ID: 66151
- Weakness: Improper Authentication - Generic
- Program: security
- Disclosed At: 2015-07-10T00:32:32.240Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This issue is a little confusing. So, if you are not able to reproduce let me know i will send you a video to help reproduce the issue.

Reproduction Steps :
1) Let's say you are User A who is inviting a user B to abug report, User A goes to + sign(adding participants) and adds a email address there.
2) User B gets an email immediately about an invitation, he accepts it and sees the bug report.
3) User A after few minutes of sending invitations realizes he made a mistake in email, and cancels the invitation which is still showing pending in his side. 
4) User A is shown a message " The invitation to UserB has been successfully rejected.", he thinks now the User B is not able to see the bug report anymore. But to his expectation, User B can still see the bug report.

So what is happening?
When User A clicked on the cancel sign to invitation that showed "pending", the cancel signed only made the invitation send to email invalid. But since user B has already accepted the invitation, User A's clicking on him won't remove User B from the bug report.

So what should have actually happened?
When User A clicked on cancel sign to invitation that was showing "pending", it should check if the user B has already join the bug report or not. And if User B hasn't it should make invitation code invalid, and if User B has already accepted and joined the Bug report, it should revoke the User B's access from Bug report.

I hope this clear enough to understand.

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
