---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1777077'
original_report_id: '1777077'
title: S3 bucket takeover [learn2.khanacademy.org]
team_handle: khanacademy
created_at: '2022-11-17T16:57:14.491Z'
disclosed_at: '2022-12-29T06:12:13.014Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 31
tags:
- hackerone
---

# S3 bucket takeover [learn2.khanacademy.org]

## Metadata

- HackerOne Report ID: 1777077
- Weakness: 
- Program: khanacademy
- Disclosed At: 2022-12-29T06:12:13.014Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The subdomain learn2.khanacademy.org was pointed  to Amazon S3, but no bucket with that name was registered [learn2.khanacademy.org]. This meant that anyone could sign up for Amazon S3, claim the bucket as their own and then serve content.

## Steps to reproduce
 
Check the following url:
http://learn2.khanacademy.org

Also

```
>  curl -k http://learn2.khanacademy.org/
<!doctype html>
<html>
  <head>
    <title>S3 takeover POC</title>
  </head>
  <body>
    <p>This is S3 takeover POC </p>
  </body>
</html>
```

## Impact

It's extremely vulnerable to attacks as a malicious user could create any web page with any content and host it on the `ford.com` domain. This would allow them to post malicious content which would be mistaken for a valid site. 

They could perform several attacks like:
 - Cookie Stealing
 - Phishing campaigns. 
 - Bypass Content-Security Policies and CORS.
 
## Recommendations for fix

* Remove the affected DNS record
 

### Supporting Material/References:

 - https://0xpatrik.com/subdomain-takeover/
 - https://hackerone.com/reports/661751

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
