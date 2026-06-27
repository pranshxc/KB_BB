---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2244229'
original_report_id: '2244229'
title: Cross-Domain Leakage of X Username / UserID due to  Dynamically Generated JS
  File
weakness: Information Disclosure
team_handle: x
created_at: '2023-11-08T02:03:08.454Z'
disclosed_at: '2024-05-10T22:40:32.373Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 47
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Cross-Domain Leakage of X Username / UserID due to  Dynamically Generated JS File

## Metadata

- HackerOne Report ID: 2244229
- Weakness: Information Disclosure
- Program: x
- Disclosed At: 2024-05-10T22:40:32.373Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** 

It was found that twitter.com hosts a specific javascript file whose content is partly dynamically generated, depending on the requestor's user authentication cookie. This dynamic part actually reveals the X's User ID of the requestor. Since the Same-Origin-Policy doesn't apply to javascript file imports, an attacker can force a victim X user to import it from a malicious cross-domain application, then extract the User-ID, leading to the retrieval of the associated X username (via X API).

**Description:** 

The leaky JS file is the following: `https://twitter.com/sw.js`

When requested with the cookie 'auth_token', the attribute '__INITIAL_STATE__ ' is populated in the following way:

```javascript
self.__INITIAL_STATE__ = {"userId":"█████"};
```

## Steps To Reproduce:

  1. Log in to your X account
  2. Visit the following malicious website: `███████`
  3. Your X User ID has been retrieved

## Impact

X users become precisely identifiable from any remote website.

This implies the following:

- Privacy / Confidentiality issue
- Facilitation of X users tracking
- Facilitation of phishing attacks at scale via better targeting 
- Facilitation of potential CSRF attacks at scale, for request depending on userId / username or any other public attribute that would initially be unknown to an attacker willing to target a maximum number of users.

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
