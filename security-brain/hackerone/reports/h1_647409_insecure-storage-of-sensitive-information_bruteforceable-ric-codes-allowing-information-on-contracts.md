---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '647409'
original_report_id: '647409'
title: ██████████ bruteforceable RIC Codes allowing information on contracts
weakness: Insecure Storage of Sensitive Information
team_handle: deptofdefense
created_at: '2019-07-17T08:58:45.362Z'
disclosed_at: '2019-12-02T19:14:22.856Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- insecure-storage-of-sensitive-information
---

# ██████████ bruteforceable RIC Codes allowing information on contracts

## Metadata

- HackerOne Report ID: 647409
- Weakness: Insecure Storage of Sensitive Information
- Program: deptofdefense
- Disclosed At: 2019-12-02T19:14:22.856Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
I'm entirely sure if this is anything useful from an attacker's purpose. Close the report if its not sensitive or non impactful. I noticed the DoD Warning mentioned it's sensitive so I thought to report it regardless just incase

I noticed ████████  has a functionality to let you look up RIC Codes. 3 digit Alphabetical code. This can be brutefored extremely easy to reveal various contract esque information 
**Description:**

The end point located at ██████/███████/s_search/query_ric.asp?ric=XXX
Normally functions to let anyone who knows the 3 digit code to access the endpoint. There is a captcha in place but once you verify that, you're able to access it unhindered. 

The usage of 3 character is inherently weak as it's only 857375 possibilities and I was able to find several already. The possibility to bruteforce it is trivial with the previous lack of enforcement

## Impact
Medium/High? Uncertain
## Step-by-step Reproduction Instructions
Visit https://www.███/███████/s_search/query_ric.asp?ric=ERX
We can then get the RIC DODAAC and further reveal information on it
https://www.█████████/█████████/s_search/query_dodaac.asp?dodaac=EZ2822

## Product, Version, and Configuration (If applicable)
N/A
## Suggested Mitigation/Remediation Actions
Enforce a complex method to codify possibly

## Impact

I'm entirely unsure what the attacker would be able to achieve but it looks possible to reveal point of contacts for contracts which could allow targeted phishing attacks, locations of contracts, what service they're under,etc. Other wise my lack of knowledge of the structure and general importance of the contents is lost on me which is why I'm uncertain if it's worth reporting

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
