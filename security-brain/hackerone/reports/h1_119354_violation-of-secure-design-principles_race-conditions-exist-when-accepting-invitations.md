---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '119354'
original_report_id: '119354'
title: Race Conditions Exist When Accepting Invitations
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2016-02-29T01:19:47.888Z'
disclosed_at: '2016-04-26T02:27:42.008Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- violation-of-secure-design-principles
---

# Race Conditions Exist When Accepting Invitations

## Metadata

- HackerOne Report ID: 119354
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2016-04-26T02:27:42.008Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi All,
Further to my last two comments on report #118312 and realizing that tokens are being stored in the DB, I realized there is probably a race condition vulnerability which allows invitation tokens to be consumed at least twice depending on the server/database response time.

I tested it tonight and was able to authenticate two accounts on one invite for my test company, test22 simply by clicking the accept button quickly in two separate browsers with two separately logged in users. I've attached screenshots of the two confirmation emails back to the administrator -- they both show the same receipt time... I know this doesn't prove the race condition so if required, I can try and duplicate it in a video if required. It only took two attempts. I was hoping you might be able to see something in the server logs - it happened at 7:58pm EST

I know this isn't necessarily a huge vulnerability in and of itself but I was thinking, a) an invitation should only be able to be accepted once and b) if I'm right with #118312 and the invitation tokens are vulnerable to a timing attack (which looks more likely given the race condition here), an attacker could accept one multiple times and the confusion for the administrator could give the attacker more time to browse reports...

Thoughts?

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
