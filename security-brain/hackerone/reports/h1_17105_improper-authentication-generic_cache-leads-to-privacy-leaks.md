---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '17105'
original_report_id: '17105'
title: Cache leads to Privacy leaks
weakness: Improper Authentication - Generic
team_handle: security
created_at: '2014-06-21T09:06:10.286Z'
disclosed_at: '2014-07-17T22:42:03.726Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# Cache leads to Privacy leaks

## Metadata

- HackerOne Report ID: 17105
- Weakness: Improper Authentication - Generic
- Program: security
- Disclosed At: 2014-07-17T22:42:03.726Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**POC IS ATTACHED**
______________________________________________________________
**Description:**
---------------------------
This bug allows me to see others users usernames even if they don't want to.
___________________________________________________________

__Steps to reproduce:__
--------------------------------------

1. Log in to account A
2. Change password of account A
3. You will be automatically logged out.
4. Log in with account B
5. You will see Account A edit page 
6. This means Privacy leak (Username of A)

____________________________________________________________

**Exploit scenario:**
-----------------------------------
User ABC wants to be completely anonymous , He signed up for Hackerone but still want to be hidden, He never tell anyone his username. But one day he changed his password and he was logged out automatically.Then immediately his friend asked for his PC, Thinking that he was logged out, and his friend won't see his information.His friend logged in with his own account. The next screen he sees is http://hackeone.com/ABC/edit he was surprised, by seeing this he now knows that His friend just logged out from hackerone so it must be his account. But ABC trusted Hackerone that once logged out his cache and username  will be deleted(no forever).

**BTW: When I make your website get a 523 error , Is it vulnerability?**

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
