---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '9008'
original_report_id: '9008'
title: 'Criptographic Issue: Strisct Transport Security with not good max age..(TOO
  SHORT!)'
weakness: Cryptographic Issues - Generic
team_handle: localize
created_at: '2014-04-22T10:20:01.211Z'
disclosed_at: '2014-04-23T03:19:51.320Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cryptographic-issues-generic
---

# Criptographic Issue: Strisct Transport Security with not good max age..(TOO SHORT!)

## Metadata

- HackerOne Report ID: 9008
- Weakness: Cryptographic Issues - Generic
- Program: localize
- Disclosed At: 2014-04-23T03:19:51.320Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello again team of Localize!

I have already reported this bug to the HackerOne team..and they fix it..not immediately, because it's low priority but they fix it!

Report: https://hackerone.com/reports/3709 :))

Issue: Strict Transport Security with too short max age.

Description: Your site use a good "Strict Transport Security" but with short MAX AGE!

Severity: See more information below.

Proof of Concept by ssllabs.com (100% affidability):

http://grabilla.com/04416-ffdc6c21-b92b-45e6-8a41-36cf650bc2f2.html

"Strict Transport Security (HSTS) 	Yes   max-age=1209600   TOO SHORT (less than 180 days)"

If you want to see the full scan with your "eyes" check it here: https://www.ssllabs.com/ssltest/analyze.html?d=localize.im&s=217.70.186.107

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
