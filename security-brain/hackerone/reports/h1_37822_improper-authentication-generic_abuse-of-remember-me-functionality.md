---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '37822'
original_report_id: '37822'
title: Abuse of "Remember Me" functionality.
weakness: Improper Authentication - Generic
team_handle: x
created_at: '2014-11-29T16:01:53.743Z'
disclosed_at: '2014-12-29T17:45:58.177Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# Abuse of "Remember Me" functionality.

## Metadata

- HackerOne Report ID: 37822
- Weakness: Improper Authentication - Generic
- Program: x
- Disclosed At: 2014-12-29T17:45:58.177Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Steps to Reproduce:-
1. Navigate to https://twitter.com/login, Fill up the required details and click on the "Log in" button. Make sure you have checked "Remember Me" check-box.
2. Login Successfully, Analyze the cookie using FireBug, specially "auth_token" and "remember_checked_on". These cookies have expiration date which is of November 2024, almost 10 years from the first login.
Note:- Kindly find snapshots for more details.

Vulnerability Title :- Abuse of "Remember Me" functionality.

Vulnerability Description :- Twitter Application has "Remember Me" functionality, which allows user to logged in for 3651 days(9 years, 11 months, 29 days - almost 10 years). Remember me functionality generally decreases security of an application and ideally should be avoided, because "remember me" permanently(for almost 10 years) stores a session token, if an attacker can access this credential it can lead to them gaining access to the application.

Remediation :- 
-Avoid implementing remember me functionality if possible If remember me functionality is required consider only using it to remember the users user id, rather than having the functionality allow a complete login. If complete login is required, application should never allow user to keep logged in for long time ex. 10 Years.
-High value applications MUST NOT possess remember me functionality.
-Medium value applications SHOULD NOT contain remember me functionality. If present, the user MUST opt-in to remember me. The system SHOULD strongly warn users that remember me is insecure particularly on public computers
-Low value applications MAY include an opt-in remember me function. There should be a warning to the user that this option is insecure, particularly on public computers.

For more details, Kindly check https://www.owasp.org/index.php/Guide_to_Authentication#Remember_Me.

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
