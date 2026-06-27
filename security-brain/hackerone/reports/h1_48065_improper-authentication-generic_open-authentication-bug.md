---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '48065'
original_report_id: '48065'
title: open authentication bug
weakness: Improper Authentication - Generic
team_handle: coinbase
created_at: '2015-02-18T13:26:26.398Z'
disclosed_at: '2015-03-11T16:19:22.122Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- improper-authentication-generic
---

# open authentication bug

## Metadata

- HackerOne Report ID: 48065
- Weakness: Improper Authentication - Generic
- Program: coinbase
- Disclosed At: 2015-03-11T16:19:22.122Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,
If developer registers one of the three url's with out http protocol (ex:example.com) in oauth registration then he would be redirected to www.coinbase.comexample.com.This makes the user to redirect to another site than the real application.Attacker could take advantage of this and steal the token using that site as a medium.
Type:Oauth
impact:high
authentication:yes
this works if developer does a mistake but the vulnerability lies in the coinbase oauth.
Proof of concept:
https://www.coinbase.com/oauth/authorize?response_type=code&client_id=3616ab93541ef90540a0c991e113b22c1ccefa96996f70fcdc49a68d900cb761&redirect_uri=prashanthvarma.in/code.php&scope=user

Thank you,
prashanth varma

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
