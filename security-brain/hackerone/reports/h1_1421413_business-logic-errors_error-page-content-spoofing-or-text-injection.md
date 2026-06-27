---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1421413'
original_report_id: '1421413'
title: Error Page Content Spoofing or Text Injection
weakness: Business Logic Errors
team_handle: judgeme
created_at: '2021-12-09T14:17:00.013Z'
disclosed_at: '2021-12-13T07:16:59.734Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 5
asset_identifier: judge.me
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Error Page Content Spoofing or Text Injection

## Metadata

- HackerOne Report ID: 1421413
- Weakness: Business Logic Errors
- Program: judgeme
- Disclosed At: 2021-12-13T07:16:59.734Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Content spoofing, also referred to as content injection, "arbitrary text injection" or virtual defacement, is an attack targeting a user made possible by an injection vulnerability in a web application. When an application does not properly handle user-supplied data, an attacker can supply content to a web application, typically via a parameter value, that is reflected back to the user. This presents the user with a modified page under the context of the trusted domain.

## Summary:

Hello team,

When i research i found sensitive path and allow me to inject text and type more words and no limit of the words to write.

## Steps To Reproduce:

POC:-

  1. Go to https://judge.me/login you will show two type of auth 1-Facebook 2-Google
-https://judge.me/auth/google_oauth2
-https://judge.me/auth/facebook
  1. Now i can inject any thig after this path auth/*****
  1. I can typw words like this website not working by any auth like google or facebook 

## Note:
I know this vuln is out of scope when this vuln after the path of domain or subdomain but in this case "The auth is the sensitive path and you should fix that by block any words after auth/**"

## How To Fix:-

  When the attacker type any thing after auth/** you should'nt show the words in the error page and fix that by "404 NOT FOUND"

## Impact

This attack is typically used as, or in conjunction with, social engineering because the attack is exploiting a code-based vulnerability and a user's trust. As a side note, this attack is widely misunderstood as a kind of bug that brings no impact.

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
