---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '152080'
original_report_id: '152080'
title: Broken authentication and session management flaw
weakness: Improper Authentication - Generic
team_handle: coursera
created_at: '2016-07-18T16:08:54.964Z'
disclosed_at: '2016-08-18T06:58:35.572Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- improper-authentication-generic
---

# Broken authentication and session management flaw

## Metadata

- HackerOne Report ID: 152080
- Weakness: Improper Authentication - Generic
- Program: coursera
- Disclosed At: 2016-08-18T06:58:35.572Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

In this Loop Hole The Application does not destroy session after logout.. means the cookies are working to login to user account & change account Information, The Cookies are usable after many hours of logout about after 1 day i'm able to access the account & edit info.

Steps To Reproduce This Issue:

1: go to coursera.org

2. Login to your account.......

3. Get the cookies using " Brub Suite" or "EditThisCookie" 

4: Logout from the account...

5: Clear all the cookies related to coursera.org

6: Save the cookies you copied in a text file...

7: Now Injact/Import Old Cookies to the coursera.org by "EditThisCookie"... 

8: as u can see.. you will be again logged In to coursera.org account.. using old session cookies..

For More Information about This Vulnerability You can check OWASP Guide 

https://www.owasp.org/index.php?title=Broken_Authentication_and_Session_Management&setlang=en 

Thanks, 
khizer Javed

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
