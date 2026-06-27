---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '824909'
original_report_id: '824909'
title: Subdomain Takeover uptime
weakness: Privilege Escalation
team_handle: btfs
created_at: '2020-03-19T21:29:44.357Z'
disclosed_at: '2020-05-05T20:50:32.622Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- privilege-escalation
---

# Subdomain Takeover uptime

## Metadata

- HackerOne Report ID: 824909
- Weakness: Privilege Escalation
- Program: btfs
- Disclosed At: 2020-05-05T20:50:32.622Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Team:

i can't report it to the company so i hope to accept it as a valid bug , i found subdomain takeover in your subdomain ```uptime.btfs.io``` , i found this subdomain pointed to uptimerobot and not claimed so i signedup in uptimerobot and claimed it.

POC:
------

1 - open https://uptime.btfs.io/
2 - you need a password to login ```A123456789```
3 - {F753695}

## Impact

- Subdomain takeover can be abused to do several things like :
Malware distribution
Phishing / Spear phishing
XSS
Authentication bypass
Legitimate mail sending and receiving on behalf of ford subdomain

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
