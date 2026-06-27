---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '788420'
original_report_id: '788420'
title: Authorization for wp-admin directory are vulnerable to brute force.
weakness: Improper Restriction of Authentication Attempts
team_handle: stripo
created_at: '2020-02-03T18:44:10.022Z'
disclosed_at: '2020-02-05T15:40:31.375Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: my.stripo.email
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# Authorization for wp-admin directory are vulnerable to brute force.

## Metadata

- HackerOne Report ID: 788420
- Weakness: Improper Restriction of Authentication Attempts
- Program: stripo
- Disclosed At: 2020-02-05T15:40:31.375Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The domain https://my.stripo.email in the directory /wp-admin are not blocking amount of request in the authorization form, this leads to bruteforce attack. Where the attacker are able to guess tons of passwords without getting blocked or the password field gets locked.
This attack make it possible to gain access as an admin extremely easy and quick to get a successfully login.

To test this security issue you need to visit the link https://my.stripo.email in the directory /wp-admin
Install a bruteforce tool like: Burp intruder, Wfuzz, Hydra, Ncrack
I personality use Wfuzz and Burp.

Wfuzz command in Linux terminal: wfuzz -c -w /usr/share/seclists/Passwords/Common-Credentials/10k-most-common.txt -u https://my.stripo.email/wp-admin -d "Authorization: Basic admin:FUZZ" 

Supported links and fix tips:
https://owasp.org/www-community/attacks/Brute_force_attack
https://owasp.org/www-community/controls/Blocking_Brute_Force_Attacks

This Pictures below show status from my program as you can see with Wfuzz it hitted around 3000 passwords in like 40 secounds (calculated approximately.)
My Burp suite shows more exact response from your server.

## Impact

Get access to anadmin login quickly and while logged in the attacker can do whatever an admin can.

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
