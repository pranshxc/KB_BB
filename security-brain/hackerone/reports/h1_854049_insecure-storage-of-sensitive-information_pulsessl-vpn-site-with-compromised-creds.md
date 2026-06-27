---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '854049'
original_report_id: '854049'
title: PulseSSL VPN Site with Compromised Creds @ ████
weakness: Insecure Storage of Sensitive Information
team_handle: deptofdefense
created_at: '2020-04-20T10:53:00.503Z'
disclosed_at: '2020-07-30T17:48:46.720Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- insecure-storage-of-sensitive-information
---

# PulseSSL VPN Site with Compromised Creds @ ████

## Metadata

- HackerOne Report ID: 854049
- Weakness: Insecure Storage of Sensitive Information
- Program: deptofdefense
- Disclosed At: 2020-07-30T17:48:46.720Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Dear US DoD,

Back in 2019, I had reported that a pulseSSL VPN server owned by US DoD can be compromised by a publicly available exploit. The report is████████. As a result, the userid and passwd db was also compromised. I found that at least 1 userid and password combination from that compromised db can still be used.

##PoC

Here is a screenshot of me accessing a US DoD owned website using a compromised credentials found back in 2019. I am still able to login to https://████/dana-na/auth/url_3/welcome.cgi with:

l: █████████
p:  █████

█████

Here is the screenshot of the credentials that was dump back in 2019:

████

## Impact

It is widely reported in the media that blackhat hackers around the world are still hacking fully patched PulseSSL VPN hosts because owners did not change the passwords that was compromised back in 2019. The articles that I am referring to is at :

https://www.us-cert.gov/ncas/alerts/aa20-107a
https://thehackernews.com/2020/04/pulse-secure-vpn-vulnerability.html

##Fix
Other than patching, it is strongly advisable that the impacted organization `█████████` reset all passwords immediately.

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
