---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '438240'
original_report_id: '438240'
title: Reflected Cross site Scripting (XSS) on www.starbucks.com
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: starbucks
created_at: '2018-11-09T14:12:25.058Z'
disclosed_at: '2019-03-08T14:04:25.604Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 169
asset_identifier: www.starbucks.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected Cross site Scripting (XSS) on www.starbucks.com

## Metadata

- HackerOne Report ID: 438240
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: starbucks
- Disclosed At: 2019-03-08T14:04:25.604Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** Reflected Cross site Scripting (XSS) on https://www.starbucks.com/account/signin?ReturnUrl

**Description:** The attacker can execute javascript on  the victims account just after the authentication process.

**Platform(s) Affected:**
www.starbucks.com
www.starbucks.ca
www.starbucks.com.br
www.starbucks.co.uk
www.starbucks.de
www.starbucks.fr

## Steps To Reproduce:

1. Open the url: https://www.starbucks.com/account/signin?ReturnUrl=%19Jav%09asc%09ript%3ahttps%20%3a%2f%2fwww%2estarbucks%2ecom%2f%250Aalert%2528document.domain%2529
2. Login
3. The JS will execute on users(victims) account.

## Supporting Material/References:
Screenshot:
{F373210}

## How can the system be exploited with this bug?
The attacker can execute JS code.
  

## How did you come across this bug ?
I was testing for open redirect vulnerability.


## Recommendations for fix
Content based escaping on the users input, in this case the redirect parameter.

## Impact

The attacker can execute JS code.

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
