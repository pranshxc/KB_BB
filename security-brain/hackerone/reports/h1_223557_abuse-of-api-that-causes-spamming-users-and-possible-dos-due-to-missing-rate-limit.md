---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223557'
original_report_id: '223557'
title: Abuse of Api that causes spamming users and possible DOS due to missing rate
  limit
team_handle: weblate
created_at: '2017-04-24T19:23:09.404Z'
disclosed_at: '2017-05-17T14:23:07.970Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
---

# Abuse of Api that causes spamming users and possible DOS due to missing rate limit

## Metadata

- HackerOne Report ID: 223557
- Weakness: 
- Program: weblate
- Disclosed At: 2017-05-17T14:23:07.970Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Summary:
In your sub-domain: http://demo.weblate.org , another endpoint doesn't have any rate limit on it to prevent spamming you by posting a lot of questions.

##Description:
Spamming and Possible DOS is being possible due to missing rate limit on this endpoint.

**Request**
POST /accounts/email/ HTTP/1.1
Host: demo.weblate.org
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://demo.weblate.org/
Cookie: XXX
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 126

csrfmiddlewaretoken=&email=victim_email&content=

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
