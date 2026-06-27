---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '14529'
original_report_id: '14529'
title: The web application https://mavenlink.com discloses version details of the
  underlying Platform / Server
weakness: Information Disclosure
team_handle: mavenlink
created_at: '2014-06-02T23:18:12.054Z'
disclosed_at: '2014-07-08T10:00:32.648Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- information-disclosure
---

# The web application https://mavenlink.com discloses version details of the underlying Platform / Server

## Metadata

- HackerOne Report ID: 14529
- Weakness: Information Disclosure
- Program: mavenlink
- Disclosed At: 2014-07-08T10:00:32.648Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

The web application https://mavenlink.com discloses version details of the underlying Platform / Server

Following is the response from the server when the application initially communicates to the PORT 80 (HTTP) of the server

HTTP/1.1 301 Moved Permanently
Cache-Control: no-cache
Content-Type: text/html
Date: Mon, 02 Jun 2014 23:08:23 GMT
Location: https://www.mavenlink.com/
Server: nginx/1.2.3 + Phusion Passenger 3.0.17 (mod_rails/mod_rack)
Status: 301
X-Powered-By: Phusion Passenger (mod_rails/mod_rack) 3.0.17
X-Rack-Cache: miss
X-Request-Id: 8d28f92461c5d38e021fff7ff53e30b0
X-Runtime: 0.002525
X-UA-Compatible: IE=Edge,chrome=1
Content-Length: 92
Connection: keep-alive

<html><body>You are being <a href="https://www.mavenlink.com/">redirected</a>.</body></html>

Please find the attached screenshot

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
