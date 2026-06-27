---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1085079'
original_report_id: '1085079'
title: No Limit on Email Subscription
weakness: Allocation of Resources Without Limits or Throttling
team_handle: openmage
created_at: '2021-01-23T06:20:54.681Z'
disclosed_at: '2021-09-04T07:05:58.295Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
asset_identifier: demo.openmage.org
asset_type: URL
max_severity: medium
tags:
- hackerone
- allocation-of-resources-without-limits-or-throttling
---

# No Limit on Email Subscription

## Metadata

- HackerOne Report ID: 1085079
- Weakness: Allocation of Resources Without Limits or Throttling
- Program: openmage
- Disclosed At: 2021-09-04T07:05:58.295Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hello Madison
As I have Found a Business Logic Error which cause unlimited amount of Newsletter Subscription as you can see in the image i have provided 

## Steps To Reproduce:

1. Open Burpsuite and set the proxy and intercept on.

2.Then Go to https://demo.openmage.org/ and enter the Email you want to Bomb and press subscribe... (Make sure Burp Intercept is ON)

3.Then press enter and you burp has captured a request looks like this


POST /newsletter/subscriber/new/ HTTP/1.1
Host: demo.openmage.org
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 28
Origin: https://demo.openmage.org
Connection: close
Referer: https://demo.openmage.org/
Upgrade-Insecure-Requests: 1

email=deyidi6330%401adir.com

4.Now right click on request and click send to intruder.
5.Now remove the cookies here i have already removed that and at Accept-Language Header Select the 5 and click on Add § Now 5 will look like this §5§ and now in Payload tab select payload type Null Payloads and Select Generate Payloads set it to 50....

And after that click on Start Attack

You will see you are getting unlimited amount of  NewsLetter Subscription Emails

You Also can see about this on this report #1047124

## Impact

An Attacker Can Send Bulk Emails and Many Emails and in Emails He can inject Infected XSS which can captures USER SESSION TOKEN

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
