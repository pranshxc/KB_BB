---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6927'
original_report_id: '6927'
title: Session cookie can be leaked over an unencrypted HTTP connection
weakness: Violation of Secure Design Principles
team_handle: irccloud
created_at: '2014-04-10T23:40:06.349Z'
disclosed_at: '2014-05-15T16:20:10.397Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# Session cookie can be leaked over an unencrypted HTTP connection

## Metadata

- HackerOne Report ID: 6927
- Weakness: Violation of Secure Design Principles
- Program: irccloud
- Disclosed At: 2014-05-15T16:20:10.397Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Because the session cookie, `session`, does not have the [Secure flag](https://www.owasp.org/index.php/SecureFlag) set, it is possible that the session cookie leaks over an unencrypted connection. An attacker could exploit this issue by (for example) tricking a user into clicking on a link to a page with the following HTML code:

    <img src="http://www.irccloud.com">

When the user visits the page, the browser will send a request to www.irccloud.com, over an unencrypted connection (note the **http** instead of **https**), containing the session cookie. When this happens, an attacker can easily take over the user's session with a *Man-In-The-Middle attack*.

I recommend setting the Secure flag, so browsers who support the Secure flag will prevent the transmission of a cookie in an unencrypted HTTP packet.

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
