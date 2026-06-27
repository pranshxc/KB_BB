---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '280748'
original_report_id: '280748'
title: High server resource usage on captcha (viestinta.lahitapiola.fi)
weakness: Uncontrolled Resource Consumption
team_handle: localtapiola
created_at: '2017-10-19T19:37:42.116Z'
disclosed_at: '2017-12-27T20:11:21.507Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: viestinta.lahitapiola.fi
asset_type: URL
max_severity: none
tags:
- hackerone
- uncontrolled-resource-consumption
---

# High server resource usage on captcha (viestinta.lahitapiola.fi)

## Metadata

- HackerOne Report ID: 280748
- Weakness: Uncontrolled Resource Consumption
- Program: localtapiola
- Disclosed At: 2017-12-27T20:11:21.507Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# Short summary
Hi, I noticed that the following report has been fixed and closed, however the bug has reappeared in different parameters: https://hackerone.com/reports/204208

# Basic report information

**Summary:**
It is possible to generate a simple request which creates a high cpu/bandwidth consumption from the server by abusing the captcha servlet

**Description:**
By sending a specially crafted request and changing the height/width and minWordSize and maxWordSize parameters in the captcha form it is possible to consume large amount of cpu/memory and bandwidth.

**Domain:**
http://viestinta.lahitapiola.fi/

# Browsers / Apps Verified In:

Chrome / CURL

# Steps To Reproduce:

* Send a request to the following url:  https://viestinta.lahitapiola.fi/nms/jsp/captcha.jsp?captchaID=@vq-ooKP6OECsEZDMwxvQGBMqfP81em45ejwud1pg7vc=&width=10000&height=100000&minWordSize=20000&maxWordSize=200000000 and notice that the server is trying to generate the image, however it doesn't respond as it takes tons of resources to generate such image.

# Remarks

In the scope of testing I saw that denial of service is out of scope, This attack is more applicative and doesn't use distributed denial of service methods and I think it is important for you to fix this although it is not in scope.

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
