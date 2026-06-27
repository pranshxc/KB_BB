---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '260689'
original_report_id: '260689'
title: Weak Cryptography for Passwords
weakness: Weak Cryptography for Passwords
team_handle: legalrobot
created_at: '2017-08-16T12:06:08.883Z'
disclosed_at: '2017-08-21T06:19:37.816Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
asset_identifier: app.legalrobot.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- weak-cryptography-for-passwords
---

# Weak Cryptography for Passwords

## Metadata

- HackerOne Report ID: 260689
- Weakness: Weak Cryptography for Passwords
- Program: legalrobot
- Disclosed At: 2017-08-21T06:19:37.816Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi Team,

I saw while creating new account.Password is being encrypted that's good best practice.

But Issue is:

1. It is showing in the request What type of encryption(Algorithm)  is used in request.
2. I copied the encrypted password and past it online tool http://md5decrypt.net/en/Sha256/ and i was successfully able to decrypt.

As per owasp Rule you should not use Sha256 These algorithms are considered weak.

Link : https://www.owasp.org/index.php/Guide_to_Cryptography

Step To Reproduce:

1. Resister mew account in https://app.legalrobot.com/.
2. Capture the request in burpsuite tool.
3. Copy the encrypted password and paste in online tool   http://md5decrypt.net/en/Sha256/ it will successfully  decrypt the password.

Mitigation.
1. Which encryption(Algorithm) it should be displayed in the request.
2. Use strong encryption so that Man in middle attack should not be able to decrypt password.

I have attached Poc.

Tej

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
