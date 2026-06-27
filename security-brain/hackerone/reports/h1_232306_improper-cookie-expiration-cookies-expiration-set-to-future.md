---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '232306'
original_report_id: '232306'
title: Improper Cookie expiration | Cookies Expiration Set to Future
team_handle: weblate
created_at: '2017-05-26T20:37:56.115Z'
disclosed_at: '2017-08-31T09:50:11.424Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
---

# Improper Cookie expiration | Cookies Expiration Set to Future

## Metadata

- HackerOne Report ID: 232306
- Weakness: 
- Program: weblate
- Disclosed At: 2017-08-31T09:50:11.424Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,
I have found at many instances or places from signup till getting logged into application ( in domain "demo.weblate.org"  ) that session maintaining cookies such as csrf token and session id's expiration dates are set to future date. As part of secure session management one should prohibit or avoid the use of persistent cookies specially for those cookies which contain sensitive information.Ideally application should use only cookies of non persistent nature.

Here Application is setting cookie expiration to future date.

Here an adversary may get an access to victim's cookies (session ids and csrf token ) and can reuse them in further getting valid session on behalf of them or he can directly use them for any activity which cause harm to victims.

Attached screenshots for reference please see them.


See the below mentioned link for details:

https://www.owasp.org/index.php/Testing_for_cookies_attributes_(OTG-SESS-002)

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
