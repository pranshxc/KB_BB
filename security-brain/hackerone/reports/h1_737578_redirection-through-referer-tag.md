---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '737578'
original_report_id: '737578'
title: Redirection through referer tag
team_handle: stripo
created_at: '2019-11-14T18:01:28.106Z'
disclosed_at: '2019-12-18T10:24:23.850Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
asset_identifier: stripo.email
asset_type: URL
max_severity: medium
tags:
- hackerone
---

# Redirection through referer tag

## Metadata

- HackerOne Report ID: 737578
- Weakness: 
- Program: stripo
- Disclosed At: 2019-12-18T10:24:23.850Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
I replaced the referer value https://stripo.email/de/ with www.google.com and it worked, it redirected me to google.com

## Steps To Reproduce:
  1. Open URL https://stripo.email/de/subscribe/
  2. Intercept with BurpSuite
  3. Change the parameter value of referer and insert any domain you want it will redirect you to that page 

## HTTP REQUEST
POST /de/subscribe/ HTTP/1.1
Host: stripo.email
X-Forwarded-Host: https://www.google.com
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Referer: https://www.google.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 97
Cookie: XSRF-TOKEN=eyJpdiI6IjM3U1BCZzdtbENpWEc5YWNGXC81MkV3PT0iLCJ2YWx1ZSI6Ik10cWlqTGJJN0pHSitDYlhQelhVRThcL1RQYmVYVGo0XC81UWlDZU80UnhRSGRlSmtmbExqWTJjdmdNZXcyamxIdCIsIm1hYyI6ImFlNzMyN2Q1Yzk3OTg5MmJkYjU3ZDgyZjYwNTQxOGYzN2M5MTZhMWM3ZGE3OTNjYmE2MWZiM2Y4YzljZWU5NWQifQ%3D%3D; laravel_session=eyJpdiI6IkROUlwvMmlma2tmeHhkdVIzT3Y1Qmh3PT0iLCJ2YWx1ZSI6IkhRVDBScUpyVm8xRTdkUm0rNGg3RUY2ODR6azNPTTVJNjRiWFFyYlBHcW9VRE5pbjd3d2xYNEVzS1N3STFrajgiLCJtYWMiOiI5NGQxYTYyNWE3NzUxNTliYTUyMTI4MDcyZGM3YWQwYjg5ZGVhZjM0Zjk3MDY5NDdkYTVlZWI0MDkwOWVmZGJmIn0%3D

subscribe-email=winter@example.com&_token=WFCpqT3ZTAXA2fdBfdLAqsPIIVNv9bRgZBYUfsCh&source=LANDING
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]
Video File: Stripo.mkv

## Impact

May Lead to Phishing attack or it may be possible that victim machine get malicious if he visited to the malicious webpage redirected by the attacker

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
