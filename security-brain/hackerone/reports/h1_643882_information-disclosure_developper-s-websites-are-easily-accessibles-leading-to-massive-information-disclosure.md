---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '643882'
original_report_id: '643882'
title: Developper's websites are easily accessibles leading to massive information
  disclosure
weakness: Information Disclosure
team_handle: radancy
created_at: '2019-07-15T20:45:19.110Z'
disclosed_at: '2019-07-18T15:50:29.552Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 20
tags:
- hackerone
- information-disclosure
---

# Developper's websites are easily accessibles leading to massive information disclosure

## Metadata

- HackerOne Report ID: 643882
- Weakness: Information Disclosure
- Program: radancy
- Disclosed At: 2019-07-18T15:50:29.552Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Domain and URL:**
[*.devmaximum.com]
[███████████.acc.devmaximum.com]

Hello,

I've found a couple hundred of devmaximum websites with personal datas. 

I know this subdomains are out of scope, i've discovered them with [devmaximum.maximum.nl]'s SSL certificate. But in less than 30 minutes of testing i've discovered 116 uniques ███.ln emails addresses, here is a sample:
████████

Maximum's developers are using admin:admin as main password to access the websites.

## Impact

There are many impacts possible, attackers can use this massive email record (there are ██████
active users according to the statistics) to forge user:password combinaisons, and login in in █████████.nl website.

And that's only the first developper's website, i have 344 record only with Sublist3r (subdomain enumeration tool).

So I have a question, do you want me to keep digging into this, or should I stop my tests ? If you want me to dig in further, can you please add the devmaximum.com domain in the scope ?

Thanks,

Best regards,

Sicarius.

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
