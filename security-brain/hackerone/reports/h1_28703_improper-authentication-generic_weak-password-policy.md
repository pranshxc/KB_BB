---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '28703'
original_report_id: '28703'
title: Weak password policy
weakness: Improper Authentication - Generic
team_handle: irccloud
created_at: '2014-09-20T09:59:23.896Z'
disclosed_at: '2014-11-27T21:09:56.710Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# Weak password policy

## Metadata

- HackerOne Report ID: 28703
- Weakness: Improper Authentication - Generic
- Program: irccloud
- Disclosed At: 2014-11-27T21:09:56.710Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi there,

I noticed that the website does not prevent an user from using this email address as a password. 
This can lead to some poor password decisions on the clientside.  

#Steps to reproduce

- 1. Create a new account and use the email address as the password.
- 2. Reset your password and choose your email address as the password. 

In both cases, the application does not prevent this decision. 

To improve the password strength, the application should avoid 1-to-1 usage of personal information as the account password. 

I'm aware that you're using rate-limiting to prevent brute-force attacks, but in that case it's just a single email/email authentication request.

Let me know what you think about it.

Best regards,
Sebastian

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
