---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '3709'
original_report_id: '3709'
title: 'Criptographic Issue: Strisct Transport Security with not good max age..(TOO
  SHORT!)'
weakness: Cryptographic Issues - Generic
team_handle: security
created_at: '2014-03-11T14:05:18.187Z'
disclosed_at: '2014-04-22T10:16:47.725Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cryptographic-issues-generic
---

# Criptographic Issue: Strisct Transport Security with not good max age..(TOO SHORT!)

## Metadata

- HackerOne Report ID: 3709
- Weakness: Cryptographic Issues - Generic
- Program: security
- Disclosed At: 2014-04-22T10:16:47.725Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello team of HackerOne!

I am Simone, and today I will report you a criptographic issue on your site!


Issue: Strict Transport Security with too short max age.

Description: Your site use a good "Strict Transport Security" but with short MAX AGE!

Severity: See more information below.

Proof of Concept by ssllabs.com (100% affidability):

http://grabilla.com/0430b-dd84e505-e1c9-45bb-b537-9a975fd6124f.html#update

"Strict Transport Security (HSTS) 	Yes   max-age=2678400; includeSubdomains   TOO SHORT (less than 180 days)"

If you want to see the full scan with your "eyes" check it here: https://www.ssllabs.com/ssltest/analyze.html?d=hackerone.com&s=190.93.242.102

Also..See more information here:

https://community.qualys.com/thread/10857


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
