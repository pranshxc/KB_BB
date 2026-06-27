---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '204208'
original_report_id: '204208'
title: High server resource usage on captcha (viestinta.lahitapiola.fi)
weakness: Uncontrolled Resource Consumption
team_handle: localtapiola
created_at: '2017-02-07T13:55:02.444Z'
disclosed_at: '2017-03-18T12:37:34.522Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- uncontrolled-resource-consumption
---

# High server resource usage on captcha (viestinta.lahitapiola.fi)

## Metadata

- HackerOne Report ID: 204208
- Weakness: Uncontrolled Resource Consumption
- Program: localtapiola
- Disclosed At: 2017-03-18T12:37:34.522Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Basic report information
**Summary:** 
It is possible to generate a simple request which creates a high cpu/bandwidth consumption from the server by abusing the captcha servlet

**Description:**
By sending a specially crafted request and changing the height/width parameters in the captcha form it is possible to consume large amount of cpu/memory and bandwidth.

By Sending a width 21800 and height 4800 the server responded after a few seconds with a payload of 318k.
When increasing the height to 48000, the server responded after about 15 seconds with a payload of 3M.

Testing was stopped in order to prevent a full denial of service on the website but it seems that there is no limit and easily with a couple of requests we can deny service to the servlet and maybe even the whole server.

**Domain:** 
http://viestinta.lahitapiola.fi/

## Browsers / Apps Verified In:

  * Chrome / CURL

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. Send a request to the following url - http://viestinta.lahitapiola.fi/nms/jsp/captcha.jsp?captchaID=@vq-ooKP6OECsEZDMwxvQGKYlOO5cUAx8hD9Z856vdHI=,122&width=21800&height=4800&minWordSize=8&maxWordSize=8
  2. Increase the parameters width and height until server gets unresponsive or under heavy load


## Remarks

In the scope of testing I saw that denial of service is out of scope, This attack is more applicative and doesn't use distributed denial of service methods and I think it is important for you to fix this although it is not in scope

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
