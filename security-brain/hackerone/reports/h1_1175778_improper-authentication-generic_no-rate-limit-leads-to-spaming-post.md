---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1175778'
original_report_id: '1175778'
title: No rate limit leads to spaming post
weakness: Improper Authentication - Generic
team_handle: reddit
created_at: '2021-05-22T19:42:14.142Z'
disclosed_at: '2023-05-18T13:45:24.096Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 5
asset_identifier: www.reddit.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# No rate limit leads to spaming post

## Metadata

- HackerOne Report ID: 1175778
- Weakness: Improper Authentication - Generic
- Program: reddit
- Disclosed At: 2023-05-18T13:45:24.096Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Hey team,
I found there is no rate limitng in your post which leads to extreme violation of posting like 100 post in one go and no spam bot working to stop 


#Description of Vulnerability

 No rate limit means their is no mechanism to protect against the requests you made in a short frame of time. ... If the repetition doesn't give any error after 50, 100, 1000 repetitions then their will be no rate limit set

#To reproduce
- Intercept post  using burp
- see for post which include your title and information it would look like 
   
{F1311439}
-Send it to intruder and set position to content lenght only 
- use numberic type with steps of 1 you will get to expolit it 

#Poc
{F1311433}
{F1311434}
{F1311435}


For proof - https://www.reddit.com/user/testnsh

Ref - #751604 #838572 #297359

Solution use rate limiting which gave a error like 429

And its not  like bruteforcing yes it lead to ddos but also messs up with any community

Regards
@nsh_cysec

## Impact

A attacker can use to spam any community with extreme number of post as he want and no hold back he can use malicious post to encourage more to get more publicity it can be exploited .even your network and Internet connection by taking up a large amount of bandwidth and, sometimes, requiring large amounts of storage space

#How to prevent
-Define proper rate limiting.
-Limit payload sizes.
-Tailor the rate limiting to be match what API methods, clients, or addresses need or should be allowed to get.
-Add checks on compression ratios.
-Define limits for container resources.

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
