---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '143935'
original_report_id: '143935'
title: '[sms-be-vip.twitter.com] vulnerable to Jetleak'
weakness: Information Disclosure
team_handle: x
created_at: '2016-06-09T18:41:45.085Z'
disclosed_at: '2018-04-02T18:13:04.670Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 28
tags:
- hackerone
- information-disclosure
---

# [sms-be-vip.twitter.com] vulnerable to Jetleak

## Metadata

- HackerOne Report ID: 143935
- Weakness: Information Disclosure
- Program: x
- Disclosed At: 2018-04-02T18:13:04.670Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Version of Jetty installed on sms-be-vip.twitter.com (9.2.6.v20141205) is vulnerable to Jetleak.
Jetleak allows to read arbitrary data from previous requests submitted to the server by other users.

More information about Jetleak here:
https://blog.gdssecurity.com/labs/2015/2/25/jetleak-vulnerability-remote-leakage-of-shared-buffers-in-je.html 

Tool to check Jeleak:
https://github.com/GDSSecurity/Jetleak-Testing-Script

Below sample HTTP request and response:
GET / HTTP/1.1
Host: sms-be-vip.twitter.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:46.0) Gecko/20100101 Firefox/46.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
DNT: 1
Connection: close

HTTP/1.1 200 OK
Date: Thu, 09 Jun 2016 18:31:04 GMT
Content-Type: text/html; charset=ISO-8859-1
Connection: close
Server: Jetty(9.2.6.v20141205)

<html>
 <head>
  <title>Stratus.025: Welcome</title>
  <style type="text/css">
   h1, p, table, a, body { font-family: Helvetica,Verdana,Arial; font-size: 11px; }
   h1 { font-size: 13px; font-weight: bold; }
   table { border: solid 1px #999999; border-collapse:collapse; empty-cells: show; padding:2px; }
   th { font-weight: bold; background-color:#666666; color:#FFFFFF; text-align: left; }
   th, td  { border-collapse:collapse; border: solid 1px #999999; }
   tr.queue  { background-color:#F5F5F5; }
   tr.warn  { background-color:#FF9090; }
  </style>
 </head>
 <body>
<h1>Stratus.025</h1>
 </body>
</html>

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
