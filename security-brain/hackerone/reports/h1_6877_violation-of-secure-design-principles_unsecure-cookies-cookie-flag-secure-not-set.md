---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6877'
original_report_id: '6877'
title: Unsecure cookies, cookie flag secure not set
weakness: Violation of Secure Design Principles
team_handle: irccloud
created_at: '2014-04-10T21:34:38.332Z'
disclosed_at: '2014-05-15T16:16:10.381Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# Unsecure cookies, cookie flag secure not set

## Metadata

- HackerOne Report ID: 6877
- Weakness: Violation of Secure Design Principles
- Program: irccloud
- Disclosed At: 2014-05-15T16:16:10.381Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Since you are running on a secure connection, https, you should be ensuring that everything runs securely on your client's / visitors case. I have check the cookie session of IRCCloud and found out that it is not flag as secure.

Whenever a cookie contains sensitive information or is a session token, then it should always be passed using an encrypted tunnel. For example, after logging into an application and a session token is set using a cookie, then verify it is tagged using the ";secure" flag. If it is not, then the browser believes it safe to pass via an unencrypted channel such as using HTTP.

Clifford Trigo

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
