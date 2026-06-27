---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1065128'
original_report_id: '1065128'
title: No Rate Limit On dashboard.myndr.net/auth
weakness: Improper Authentication - Generic
team_handle: myndr
created_at: '2020-12-23T13:34:12.512Z'
disclosed_at: '2021-09-23T08:41:40.146Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: '*.myndr.nl'
asset_type: WILDCARD
max_severity: none
tags:
- hackerone
- improper-authentication-generic
---

# No Rate Limit On dashboard.myndr.net/auth

## Metadata

- HackerOne Report ID: 1065128
- Weakness: Improper Authentication - Generic
- Program: myndr
- Disclosed At: 2021-09-23T08:41:40.146Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
hello team,

I tested a little bit the website and went to registration page where you will give 7 digits to complete your switch serial, i didn't want to go further with brute forcing because it's  forbidden how ever i gave a try with a small range of tries and have no message for limitting the number of requests. 

## Steps To Reproduce:
To reproduce this you have to follow these steps:

  1. Send requests with  POST  and change the 7 digits of the param #switch-serial  and wait for http statut 200 instead of 404 

POST /auth/validate-switch-serial HTTP/1.1
Host: dashboard.myndr.net
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: */*
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 33
Origin: https://dashboard.myndr.net
DNT: 1
Connection: close
Referer: https://dashboard.myndr.net/auth/register?id=-1

switch-serial=MSA3/8878-XXXXXXX

#Solution

A limit to requests mechanism  must be deployed.

## Impact

An attacker could send a large number of requests to determine the victim switch serial and went to the next step of registration.

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
