---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '163904'
original_report_id: '163904'
title: Username can be used to trick the victim on the name of www.gratipay.com
weakness: Violation of Secure Design Principles
team_handle: gratipay
created_at: '2016-08-27T22:33:45.000Z'
disclosed_at: '2016-12-30T07:47:33.396Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 5
tags:
- hackerone
- violation-of-secure-design-principles
---

# Username can be used to trick the victim on the name of www.gratipay.com

## Metadata

- HackerOne Report ID: 163904
- Weakness: Violation of Secure Design Principles
- Program: gratipay
- Disclosed At: 2016-12-30T07:47:33.396Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,

I found a vulnerability in www.gratipay.com

**Steps to reproduce:**
1. Login in gratipay using any social account which do not provide the email to gratipay.
2. In my case i use twiiter.com, i got the message from gratipay that no Email id is associated with this account.
3. Click on settings and change the username to the malicious site. (I used www.attacker.com)
4. Click on the email.
5. Add the Victim's Email Id.
6. Done. Email Sent to Victim with attacker's malicious site or phising page.

**Impact:**
Using this vulnerability an attacker can use a malcious script or a phising page to trick the victims. Username of gratipay (In case of this report attacker's site) will be renders as a link. Victim Just need to click on that link. since the email is from trusted domain like gratipay.com, victim will definitely want to click on the link which could be end up to takeover his account etc.

**Fix:** It can be fixed by do not allowing . (dot) in usernames of gratipay. 


I also attached the screen shot of email sent for invitation to victim, in which account name is renders as a link.

Thanks,
Akash Saxena

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
