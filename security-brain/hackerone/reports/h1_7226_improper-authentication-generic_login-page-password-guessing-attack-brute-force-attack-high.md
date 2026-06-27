---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7226'
original_report_id: '7226'
title: Login page password-guessing attack(Brute-force attack-High).
weakness: Improper Authentication - Generic
team_handle: irccloud
created_at: '2014-04-11T18:33:29.040Z'
disclosed_at: '2014-04-26T09:36:36.155Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# Login page password-guessing attack(Brute-force attack-High).

## Metadata

- HackerOne Report ID: 7226
- Weakness: Improper Authentication - Generic
- Program: irccloud
- Disclosed At: 2014-04-26T09:36:36.155Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,
I found a Brute forcing attacking on your website.

A common threat web developers face is a password-guessing attack known as a brute force attack. A brute-force attack is an attempt to discover a password by systematically trying every possible combination of letters, numbers, and symbols until you discover the one correct combination that works. 

This login page doesn't have any protection against password-guessing attacks (brute force attacks). It's recommended to implement some type of account lockout after a defined number of incorrect password attempts. Consult Web references for more information about fixing this problem.

I am tested 10 invalid credentials and no account lockout was detected.This means it's vuln to Brute forcing attack.

Vuln page- Login page

My http request-
POST / HTTP/1.1
Content-Length: 63
Content-Type: application/x-www-form-urlencoded
Referer: http://www.irccloud.com/
Host: www.irccloud.com
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.63 Safari/537.36
Accept: */*

email=07CA51kX%40www.irccloud.com&org_invite=&password=SrEeHaRiDasSsS

Response- 
HTTP/1.1 302 Found
Cache-Control: no-cache
Content-length: 0
Location: https://www.irccloud.com/
Connection: close

Impact of this vuln-
An attacker may attempt to discover a weak password by systematically trying every possible combination of letters, numbers, and symbols until it discovers the one correct combination that works.


Fix-
It's recommended to implement some type of account lockout after a defined number of incorrect password attempts. 

More Details- https://www.owasp.org/index.php/Blocking_Brute_Force_Attacks

Best,

Sreehari Haridas

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
