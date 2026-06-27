---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6574'
original_report_id: '6574'
title: Login page password-guessing attack
team_handle: reddapi
created_at: '2014-04-08T18:46:04.509Z'
disclosed_at: '2014-05-09T02:15:54.286Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
---

# Login page password-guessing attack

## Metadata

- HackerOne Report ID: 6574
- Weakness: 
- Program: reddapi
- Disclosed At: 2014-05-09T02:15:54.286Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello team of Reddapi!

Here to report a vulnerability on your site.

Affected site: www.reddapi.com

Vulnerability: Login page password-guessing attack

Severity:Low.

Vulnerability description:

A brute-force attack is an attempt to discover a password by systematically trying every possible combination of letters, numbers, and symbols until you discover the one correct combination that works

Attack Details:

http://www.reddapi.com/ (/login) page doesn't have any protection against password-guessing attacks (brute force attacks). It's recommended to implement some type of account lockout after a defined number of incorrect password attempts.

I personally tried many times with wrong password even though no account lockout was detected.


Fix: Implement Captcha


Well, I wait more information about this report!


Thanks and best regards,


Simone

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
