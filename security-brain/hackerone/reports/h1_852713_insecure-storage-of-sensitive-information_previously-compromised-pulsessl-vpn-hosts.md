---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '852713'
original_report_id: '852713'
title: Previously Compromised PulseSSL VPN Hosts
weakness: Insecure Storage of Sensitive Information
team_handle: deptofdefense
created_at: '2020-04-18T04:27:27.475Z'
disclosed_at: '2020-05-27T14:25:54.096Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- insecure-storage-of-sensitive-information
---

# Previously Compromised PulseSSL VPN Hosts

## Metadata

- HackerOne Report ID: 852713
- Weakness: Insecure Storage of Sensitive Information
- Program: deptofdefense
- Disclosed At: 2020-05-27T14:25:54.096Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi again!!

Back in 2019, I had reported that a pulseSSL VPN server owned by US DoD can be compromised by a publicly available exploit. The report is #681249. As a result, the userid and passwd db was also compromised. I  found  that at least 1 userid and password combination from that compromised db can still be used. 


##PoC

Here is a screenshot of me accessing a US DoD owned website using a compromised credentials found back in 2019. I am still able to login to https://████/dana-na/auth/url_46/welcome.cgi with:

l: ███
p: █████████

███████
███████

Here is the creds from  Sep, 2019.

█████

## Impact

It is widely reported in the media that blackhat hackers around the world are still hacking fully patched PulseSSL VPN hosts because owners did not change the passwords that was compromised back in 2019. The articles that I am referring  to is at :

https://www.us-cert.gov/ncas/alerts/aa20-107a
https://thehackernews.com/2020/04/pulse-secure-vpn-vulnerability.html

##Fix
Other than patching, it is strongly advisable that the impacted organization `███`   __reset all passwords immediately__.

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
