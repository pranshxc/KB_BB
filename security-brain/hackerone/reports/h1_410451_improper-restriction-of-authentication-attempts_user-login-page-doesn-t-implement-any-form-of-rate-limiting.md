---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '410451'
original_report_id: '410451'
title: User login page doesn't implement any form of rate limiting
weakness: Improper Restriction of Authentication Attempts
team_handle: security
created_at: '2018-09-17T05:54:18.802Z'
disclosed_at: '2019-01-04T11:00:10.295Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 40
asset_identifier: https://ctf.hacker101.com
asset_type: URL
max_severity: low
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# User login page doesn't implement any form of rate limiting

## Metadata

- HackerOne Report ID: 410451
- Weakness: Improper Restriction of Authentication Attempts
- Program: security
- Disclosed At: 2019-01-04T11:00:10.295Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

**Summary:**
As a best practice a login page should have a rate limitting just like hackerone.com

**Vulnerable Request**
```
POST /auth/post_login HTTP/1.1
Host: ctf.hacker101.com
User-Agent: <redacted>
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://ctf.hacker101.com/
Content-Type: application/x-www-form-urlencoded
Content-Length: 73
Cookie:<some cookie>
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1

csrf=<csrf token>&username=<target username>&password=<vulnerable parameter>
```
### Steps To Reproduce

1. Tamper login page and send the request to Burp Intruder
2. Configure the payloads
3. Start the Burp Intruder

**Proof Of Concept**
██████

Notice the Content Length as highlited on my screenshot

## Impact

An attacker can freely bruteforce any username and can takeover any account

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
