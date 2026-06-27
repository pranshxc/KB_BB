---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '972601'
original_report_id: '972601'
title: Open Redirect at https://oauth.secure.pixiv.net
weakness: Open Redirect
team_handle: pixiv
created_at: '2020-09-02T01:56:14.267Z'
disclosed_at: '2020-12-22T01:24:27.491Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 25
asset_identifier: accounts.pixiv.net
asset_type: URL
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Open Redirect at https://oauth.secure.pixiv.net

## Metadata

- HackerOne Report ID: 972601
- Weakness: Open Redirect
- Program: pixiv
- Disclosed At: 2020-12-22T01:24:27.491Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hello @pixiv security team,  i hope you are well, i noticed you can redirect users to another domain if you send an invalided scope.

**Vulnerable Url**

* `https://oauth.secure.pixiv.net/v2/auth/authorize?client_id=Y1olfIApoCNuSGzx9kTgIbf5Wk4R&redirect_uri=https%3A%2F%2Fsketch.pixiv.net%2Fsession%2Fpixiv%2Fcallback&response_type=code&scope=read-email+read-x-restrict+read-birth+write-upload+read-profile+write-profile+read-favorite-users&state=security_token%3D5cb310fefea19a5cb56307af3488a816921413bc70b5b142%2Crequest_type%3Ddefault`

## Steps To Reproduce:

  *   In the request looks for the **scope** parameter and change his value to *ggg*.
 
  *    Looks for the **redirect_uri** parameter and change it for an arbitrary domain, i.e `https://example.com`

  *   Open the link in your browser and done.
  
  *   `https://oauth.secure.pixiv.net/v2/auth/authorize?client_id=Y1olfIApoCNuSGzx9kTgIbf5Wk4R&redirect_uri=https%3A%2F%2Fexample.com%2Fsession%2Fpixiv%2Fcallback&response_type=code&scope=ggg&state=security_token%3D5cb310fefea19a5cb56307af3488a816921413bc70b5b142%2Crequest_type%3Ddefault`

{F972733}

## Impact

It may lead users to a phishing site and an attacker can steals his credentials.

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
