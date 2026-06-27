---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '400781'
original_report_id: '400781'
title: Browser Self XSS Protection not implemented
weakness: Information Disclosure
team_handle: weblate
created_at: '2018-08-27T06:35:12.935Z'
disclosed_at: '2018-09-26T09:22:28.258Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- information-disclosure
---

# Browser Self XSS Protection not implemented

## Metadata

- HackerOne Report ID: 400781
- Weakness: Information Disclosure
- Program: weblate
- Disclosed At: 2018-09-26T09:22:28.258Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi

Self XSS Protection not used ,An attacker  can trick users to insert JavaScript in browser console.

A Self-XSS scam usually works by promising to help you access somebody else's account. Instead, the scammer tricks you into gaining access to your account for fraud, spam and tricking more people into a scam.

I see that you have not enabled 'Self XSS Protection ' on https://weblate.org/ , This technique prevents user from getting tricked into injecting js themselves and allow attackers to socially engineering them..

For example, Facebook have : http://gyazo.com/3b448c200124053b60b622d0149e242d https://www.facebook.com/selfxss

But you don't have it, You should ,  to protect your  users , it prevents the users from  getting  tricked and be safe. Its a best practice every website should follow for a safer web!

This bug has been fixed by many websites including Facebook. So its strongly advised you to fix it.

[Similar fixed issue](https://hackerone.com/reports/76307)

## Impact

Users with low knowledge can be tricked to attack themselves via xss attacks.

#Ref
-  https://stackoverflow.com/questions/21692646/how-does-facebook-disable-the-browsers-integrated-developer-tools
- https://facebook.com/selfxss

Regards

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
