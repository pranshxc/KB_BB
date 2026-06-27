---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '639682'
original_report_id: '639682'
title: Khan Academy ClickJacking to Steal Users's Credintials
team_handle: khanacademy
created_at: '2019-07-10T17:57:58.666Z'
disclosed_at: '2021-03-31T22:26:23.642Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
---

# Khan Academy ClickJacking to Steal Users's Credintials

## Metadata

- HackerOne Report ID: 639682
- Weakness: 
- Program: khanacademy
- Disclosed At: 2021-03-31T22:26:23.642Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

#DESCRIPTION

1. It ask to login to https://alerta.khanacademy.org  with google account.
2. It doesn't give access to any normal user.
3. That's why after trying to login with GOOGLE account it shows a error message prompt with user's sensitive information including [email, code/access token and client id etc.]
4. Let's steal it via Click Jacking!

Note: If victim is already logged into his google account, attacker can easily steal victim's credintials including [email, code/access token and client id etc.]

#Usually we always logged into our google account, so it's quite easy to steal victim's credintials.

#Step to Re-Produce:

Step 1. Let's make [ Script+PoC ] via BurpSuite! {F526049}

Step 2. Login to your google account.

Step 3. Exploition!

Watch my proof of concept video carefully!

████

Cheers!

## Impact

Attacker can easily steal victim's credintials including [email, code/access token and client id etc.]

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
