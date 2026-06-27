---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '265706'
original_report_id: '265706'
title: '[rt.torproject.org] No Rate Limitting on Login Form'
weakness: Improper Restriction of Authentication Attempts
team_handle: torproject
created_at: '2017-09-04T03:22:39.943Z'
disclosed_at: '2023-11-28T09:01:38.643Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 7
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# [rt.torproject.org] No Rate Limitting on Login Form

## Metadata

- HackerOne Report ID: 265706
- Weakness: Improper Restriction of Authentication Attempts
- Program: torproject
- Disclosed At: 2023-11-28T09:01:38.643Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello Team,

**Description**
I just Notice that you didn't implement a captcha or Rate Limiting on one of your sub-domain which is vulnerable to brute force.

**Proof Of Concept**
Download {F218177} 
You can use your own wordlist to test my python script
Usage:
```
~$ python tor.py -t username -p passwordlist.txt
```
it should be just like this if the script runs 
{F218178}

Results on burpsuite when i try to login 500 times
{F218179}

**Fix / Mitigation**
You can implement a Rate Limit or Captcha in Login Form :)

Let me know if you needs more info and i will look forward to your reply.
Kind Regards,

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
