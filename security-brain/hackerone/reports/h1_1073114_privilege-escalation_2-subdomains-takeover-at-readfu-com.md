---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1073114'
original_report_id: '1073114'
title: 2 Subdomains Takeover at readfu.com
weakness: Privilege Escalation
team_handle: x
created_at: '2021-01-06T22:29:46.130Z'
disclosed_at: '2021-03-15T15:37:12.131Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 34
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# 2 Subdomains Takeover at readfu.com

## Metadata

- HackerOne Report ID: 1073114
- Weakness: Privilege Escalation
- Program: x
- Disclosed At: 2021-03-15T15:37:12.131Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi ,
I believe that `readfu.com` is now belong to `Twitter,inc`. I was able to takeover 2 subdomains via Heroku Services & Normal domain Buy!
{F1147316}

# `Poc :` 

 * Please visit http://alpha.readfu.com/  via Heroku

steps : https://youtu.be/mpPXrvhvD4A

* Please check dns of `rb.readfu.com	` you will see it `hqn.ro`

`hqn.ro` is  available to Buy for 9 euro at https://www.eureg.ro/

so anyone can buy it and Takeover `rb.readfu.com`

{F1147314}

# `Suggested fix :` 
> remove your subdomains DNS`

## Impact

Takeovers can be use in many things :

Malware
Phishing / Spear phishing
XSS
Authentication bypass
Open Redirects
True access
.. etc

Kind Regards,
Mohamed Haron.

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
