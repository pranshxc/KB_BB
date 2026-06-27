---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '83856'
original_report_id: '83856'
title: 's2.owncloud.com: SSL Session cookie without secure flag set'
weakness: Information Disclosure
team_handle: owncloud
created_at: '2015-08-21T11:27:25.429Z'
disclosed_at: '2016-01-27T23:25:23.592Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- information-disclosure
---

# s2.owncloud.com: SSL Session cookie without secure flag set

## Metadata

- HackerOne Report ID: 83856
- Weakness: Information Disclosure
- Program: owncloud
- Disclosed At: 2016-01-27T23:25:23.592Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

URL: https://s2.owncloud.com/

Issue detail
The following cookie was issued by the application and does not have the secure flag set:

    _session_id=0fdc40cc016d1e70b1567b0071e5dcd2; expires=Sat Aug 22 03:45:12 2015; path=/; domain=s2.owncloud.com; max-age=86387; httponly

The cookie appears to contain a session token, which may increase the risk associated with this issue. You should review the contents of the cookie to determine its function.

Issue background
If the secure flag is set on a cookie, then browsers will not submit the cookie in any requests that use an unencrypted HTTP connection, thereby preventing the cookie from being trivially intercepted by an attacker monitoring network traffic. If the secure flag is not set, then the cookie will be transmitted in clear-text if the user visits any HTTP URLs within the cookie's scope. An attacker may be able to induce this event by feeding a user suitable links, either directly or via another web site. Even if the domain which issued the cookie does not host any content that is accessed over HTTP, an attacker may be able to use links of the form http://example.com:443/ to perform the same attack.

Issue remediation
The secure flag should be set on all cookies that are used for transmitting sensitive data when accessing content over HTTPS. If cookies are used to transmit session tokens, then areas of the application that are accessed over HTTPS should employ their own session handling mechanism, and the session tokens used should never be transmitted over unencrypted communications.

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
