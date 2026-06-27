---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '15166'
original_report_id: '15166'
title: Password reset token not expiring
weakness: Improper Authentication - Generic
team_handle: mavenlink
created_at: '2014-06-05T01:44:26.837Z'
disclosed_at: '2014-07-10T18:23:38.608Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# Password reset token not expiring

## Metadata

- HackerOne Report ID: 15166
- Weakness: Improper Authentication - Generic
- Program: mavenlink
- Disclosed At: 2014-07-10T18:23:38.608Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Old unused Password reset tokens are not expiring on mail.ru after the issuance of a new token.
**Explaination**
Suppose at 09:00 hrs I used password reset options of mavenlink and got a token on my email.Lets call it token01.But i didnot use it.
And at 09:04 hrs I used again the password reset option and got a new token,which is token02.
Now generally after the issuance of token02,the previous unused token should expire.But in case of mavenlink  its not happening.Both the tokens are remaining usable at the same time.

**Attack Scenario**
Suppose I am an attacker and I got access to the recovery email option of your mavenlink  account.I logged in to ur recovery email (suppose that is user@gmail.com).Then I used the forget password option of your mavenlink  email.I will get one password reset token.
I noted the token and then deleted the email from user@gmail.com.
In the meantime u understood that someone got access to ur account.They you reset the password of mavenlink  by issuing new token and also u changed the password of ur user@gmail.com so that any one cant hack again ur mavenlink  account.
Now its time for my exploitation.
I will use my token which is live even after your issuance of new token.and I will hack into ur mavenlink  account.

**Mitigation**
1. Use a certain living span for a token.Suppose,a token will remain valid upto 12 hours after being issued.
2. All unused tokens should expire automatically after the issuance of a new token.

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
