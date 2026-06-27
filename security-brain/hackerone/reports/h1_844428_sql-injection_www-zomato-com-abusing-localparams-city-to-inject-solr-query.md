---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '844428'
original_report_id: '844428'
title: '[www.zomato.com] Abusing LocalParams (city) to Inject SOLR query'
weakness: SQL Injection
team_handle: zomato
created_at: '2020-04-09T18:33:10.236Z'
disclosed_at: '2020-08-10T13:23:11.806Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
asset_identifier: '*.zomato.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- sql-injection
---

# [www.zomato.com] Abusing LocalParams (city) to Inject SOLR query

## Metadata

- HackerOne Report ID: 844428
- Weakness: SQL Injection
- Program: zomato
- Disclosed At: 2020-08-10T13:23:11.806Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Hi Team! ;)

I Found an **limited** ``SOLR Injection`` by Abusing LocalParams (``city``) in ``/webapi/searchapi.php``, **Therefore Please respect my decision to mark this report as** ``Medium`` **instead of** ``High`` **(Based on the fact the code is Vulnerable even if it's hard to exploit).**

- Request (adding single Backslash):

```http
GET /webapi/searchapi.php?city=51\ HTTP/1.1
Host: www.zomato.com
Connection: close
Accept: application/json
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
Chrome/80.0.3987.149 Safari/537.36
Accept-Encoding: gzip, deflate
Accept-Language: en
```

- Response:

```http
HTTP/1.1 500 Internal Server Error
```
- Request (adding double Backslashes):

```http
GET /webapi/searchapi.php?city=51\\ HTTP/1.1
Host: www.zomato.com
Connection: close
Accept: application/json
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
Chrome/80.0.3987.149 Safari/537.36
Accept-Encoding: gzip, deflate
Accept-Language: en
```

- Response:

```http
HTTP/1.1 200 OK
```

**As you can see - adding single Backslash** ``\`` **will break the SOLR query but by adding double Backslashes** ``\\`` **(closing it) will execute the SOLR query properly, Therefore this isn't an "Exception" - it's a valid SOLR Injection!!**

- Source: **https://portswigger.net/research/backslash-powered-scanning-hunting-unknown-vulnerability-classes**

## Impact

**"By exploiting 'Solr (local) Parameters Injection,' it is possible to at least modify or view all the data within the Solr cluster, or even exploit known vulnerabilities to achieve remote code execution."**

- Source: **"https://www.veracode.com/blog/security-news/new-research-apache-solr-parameter-injection"**

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
