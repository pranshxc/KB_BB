---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '269449'
original_report_id: '269449'
title: Banner Grabbing - Apache Server Version Disclousure
weakness: Information Disclosure
team_handle: nextcloud
created_at: '2017-09-19T10:42:08.451Z'
disclosed_at: '2018-05-17T09:05:15.144Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 5
asset_identifier: customerupdates.nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Banner Grabbing - Apache Server Version Disclousure

## Metadata

- HackerOne Report ID: 269449
- Weakness: Information Disclosure
- Program: nextcloud
- Disclosed At: 2018-05-17T09:05:15.144Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello Nextcloud, I'd like to report a nice little bug.

Banner Grabbing is a technique used to gain information about a remote server. Additionally, this  technique is use  to get information about remote servers. 

I've captured the HTTP request while visiting https://customerupdates.nextcloud.com and https://surveyserver.nextcloud.com

https://customerupdates.nextcloud.com/

GET / HTTP/1.1
Host: customerupdates.nextcloud.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:55.0) Gecko/20100101 Firefox/55.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0

HTTP/1.1 403 Forbidden
Date: Tue, 19 Sep 2017 10:29:24 GMT
Server: Apache/2.4.18 (Ubuntu)
Strict-Transport-Security: max-age=15768000; includeSubDomains; preload
Content-Length: 16
Content-Type: text/html; charset=iso-8859-1
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
----------------------------------------------------------

Above you can see server version of Nextcloud [Apache/2.4.18 (Ubuntu)]


This information might help an attacker gain a greater understanding of the systems in use and potentially develop further attacks targeted at the specific version of Apache.

Impact
An attacker might use the disclosed information to harvest specific security vulnerabilities for the version identified.

Remediation
Configure your web server to prevent information leakage from the SERVER header of its HTTP response.

I hope you'll fix it!

I think and hope this report would impress you.

Let me know if u have any question
Thanks
Cheers
Anas

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
