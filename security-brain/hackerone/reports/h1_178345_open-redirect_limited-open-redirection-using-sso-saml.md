---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '178345'
original_report_id: '178345'
title: Limited Open redirection using SSO-SAML
weakness: Open Redirect
team_handle: security
created_at: '2016-10-27T06:44:35.351Z'
disclosed_at: '2017-03-26T08:34:22.061Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
tags:
- hackerone
- open-redirect
---

# Limited Open redirection using SSO-SAML

## Metadata

- HackerOne Report ID: 178345
- Weakness: Open Redirect
- Program: security
- Disclosed At: 2017-03-26T08:34:22.061Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

**Endpoint:** https://hackerone.com/users//saml/sign_in?email=teste@snapchat.com&remember_me=true

Recently, you have patched an open redirection issue which was reported as #171398. 
I found a bypass of that patch. 

**Steps to reproduce:** 
1. Add following in comment/report : 
```https://hackerone.com/users//saml/sign_in?email=teste@snapchat.com&remember_me=true``` 
2. Click on link. 
3. You will redirected on SSO URL without going through **External Link Warning** page. 
4. Done.

PoC  : 
https://hackerone.com/users/saml/sign_in?email=teste@snapchat.com&remember_me=true (Through external warning page)
https://hackerone.com/users//saml/sign_in?email=teste@snapchat.com&remember_me=true (Without external warning page)

**Suggested Fix:** Use more stronger regular expression and filtration at this endpoint.

Best regards,
Shailesh

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
