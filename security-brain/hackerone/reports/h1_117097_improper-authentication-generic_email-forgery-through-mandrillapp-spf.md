---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '117097'
original_report_id: '117097'
title: Email Forgery through Mandrillapp SPF
weakness: Improper Authentication - Generic
team_handle: gratipay
created_at: '2016-02-18T07:11:14.654Z'
disclosed_at: '2016-03-19T19:16:58.197Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- improper-authentication-generic
---

# Email Forgery through Mandrillapp SPF

## Metadata

- HackerOne Report ID: 117097
- Weakness: Improper Authentication - Generic
- Program: gratipay
- Disclosed At: 2016-03-19T19:16:58.197Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Description :-
The SPF record of gratipay.com include Mandrillapp which you are not using right now, i'm able to add gratipay.com in my account, although a further verification of domain is required but you should know that Mandrillapp allow to send email from a domain if its SPF records point Mandrill server.
I have attached a screenshot to proof my concept
1 SPF record found for the domain gratipay.com :
""  v=spf1 include:email.freshdesk.com include:spf.mandrillapp.com include:_spf.google.com -all  "
This is useful in phishing, and this type of vulnerability is news worthy (http://bits.blogs.nytimes.com/2015/04/09/sendgrid-email-breach-was-used-to-attack-coinbase-a-bitcoin-exchange/)
Vulnerability Impact Scenario :-
Using my own mandrill account I can send email which appears to originate from @gratipay.com
Patch :-
The patch is pretty simple. Complete your mandrill registration process. This will lock out other mandrill users from sending email that originates from *@gratipay.com.
Let me know if you have any other questions.
Check Screenshot.
Thanks.

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
