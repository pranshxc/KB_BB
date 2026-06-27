---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '3227'
original_report_id: '3227'
title: Control Characters Not Stripped From Username on Signup
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2014-03-04T21:46:39.784Z'
disclosed_at: '2014-03-11T20:33:27.097Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- violation-of-secure-design-principles
---

# Control Characters Not Stripped From Username on Signup

## Metadata

- HackerOne Report ID: 3227
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2014-03-11T20:33:27.097Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey,

To be honest, I'm not sure if there is any *real* security implications of this bug, but it's (IMO) something which should be fixed at some point (since it'll be pretty easy).

On signup, the username you chose has to be alphanumeric. If you submit someone else's username, followed by a null-byte (`%00`), you'll get an error indicating that the username has been taken (expected behaviour). Same with `%20`. However, if you submit the username followed by a control character, such as a new line (`%0a`), the request will go through and you'll be signed up.

There are a couple of consequences of this. The first is that your profile can't be viewed (which also means you can't update your own settings!). You'll get a 404.

The second is that any bug reports you submit will look like another user submitted them. Again, not that big of a deal.

### Proof-of-Concept
1. Browse to https://hackerone.com/users/sign_up
2. Enter any details, make sure your username is followed by `%0a` (use Burp to append it)
3. Confirm your email, then login
4. Click your profile picture in the top right
5. You'll get a 404

If you need anymore information just shout,
Cheers,
Jack

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
