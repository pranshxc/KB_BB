---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1212337'
original_report_id: '1212337'
title: 'Bypass the fix of report #1078283 due to poor validation'
weakness: Open Redirect
team_handle: khanacademy
created_at: '2021-05-29T02:29:33.482Z'
disclosed_at: '2021-07-08T19:25:27.515Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- open-redirect
---

# Bypass the fix of report #1078283 due to poor validation

## Metadata

- HackerOne Report ID: 1212337
- Weakness: Open Redirect
- Program: khanacademy
- Disclosed At: 2021-07-08T19:25:27.515Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Khan Academy Team,

I was able to bypass the fix you implemented for report #1078283. 

The URL validation you implemented on the endpoint `continue` checks the presence of `khanacademy.org` however it doesn't have any boundary checking to ignore domains starting with `.org`, so if an attacker register a domain starting with `org` like this one `orghacker.com.br` and have a subdomain entry of `khanacademy` the attacker is able to bypass the current implementation and lead the victim to his controlled page.

# Steps to reproduce the issue

* Go to this page https://www.khanacademy.org/signup?isteacher=1&referral=LearnStorm&continue=https://khanacademy.orghacker.com.br
* You'll be redirected to `orghacker.com.br` which is not a domain that Khan Academy owns

## Impact

Bypass of current URL validation. Attacker can send a phishing campaign and redirect the request to a server of his control. An attacker might chain the attack to other types of attack too.

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
