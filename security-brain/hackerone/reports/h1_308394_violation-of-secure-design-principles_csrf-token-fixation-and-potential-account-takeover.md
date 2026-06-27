---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '308394'
original_report_id: '308394'
title: CSRF token fixation and potential account takeover
weakness: Violation of Secure Design Principles
team_handle: khanacademy
created_at: '2018-01-23T21:10:54.327Z'
disclosed_at: '2018-04-19T22:39:54.470Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- violation-of-secure-design-principles
---

# CSRF token fixation and potential account takeover

## Metadata

- HackerOne Report ID: 308394
- Weakness: Violation of Secure Design Principles
- Program: khanacademy
- Disclosed At: 2018-04-19T22:39:54.470Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

### Details:
I have found that the csrf_token ( fkey parameter )which prevent CSRF attacks is fixed in same browser and didn't changed even user login or logout , a lot of users can use the same CSRF_token , this can be exploited such 2 ways :
 
### Shared computers:
- attacker open "https://www.khanacademy.org" and login to his account
- attacker copied the value of "fkey parameter" then he will logout
- victim will logged in his account with the same CSRF_token value (fkey parameter)
- now attacker forced the victim to change his email address to attacker emails , since he already have the valid CSRF_token

### XSS:
- due to XSS vulnerability. Attacker knows the CSRF_token for the victim so he can use this in any actions behind the victim , for example :  change user email address   

CSRF PoC to takeover user account by linked the attacker email address:

```
<html>
  <body>
    <form action="https://www.khanacademy.org/settings/linkemail" method="POST">
      <input type="hidden" name="fkey" value="CSRF_token" />
      <input type="hidden" name="email" value="[attacker-email-address]" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
```

## Impact

As i described above this can be exploited to takeover another account

Let me know if there is anything unclear

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
