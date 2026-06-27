---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '57914'
original_report_id: '57914'
title: HTML injection in email sent by romit.io
weakness: Command Injection - Generic
team_handle: enter
created_at: '2015-04-23T17:24:46.665Z'
disclosed_at: '2015-11-26T20:49:08.402Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- command-injection-generic
---

# HTML injection in email sent by romit.io

## Metadata

- HackerOne Report ID: 57914
- Weakness: Command Injection - Generic
- Program: enter
- Disclosed At: 2015-11-26T20:49:08.402Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Issue**
It is possible for the attacker to inject arbitary HTML code in the email sent by romit.io as "<" in username is not sanitized when sending mail to the user. This can be used to redirect user to unwanted websites or spam from romit.io

**PoC**
1. Go to settings in your account and change the Nickname to some HTML like
    "> <a href="google.com">    OR
    "><img src="sth bad"             OR
    <!--

2. Save your settings.
3. Share your wallet with any user by providing phone number.


Thanks
crab

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
