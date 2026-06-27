---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1718371'
original_report_id: '1718371'
title: Subdomain takeover at http://test.www.midigator.com
weakness: Privilege Escalation
team_handle: equifax
created_at: '2022-09-30T16:15:02.256Z'
disclosed_at: '2022-11-12T16:05:05.413Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 31
asset_identifier: '*.midigator.com'
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Subdomain takeover at http://test.www.midigator.com

## Metadata

- HackerOne Report ID: 1718371
- Weakness: Privilege Escalation
- Program: equifax
- Disclosed At: 2022-11-12T16:05:05.413Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Vulnerability
Subdomain test.www.midigator.com points to an AWS S3 bucket that no longer exists. I was able to take control of this bucket and serve my own content on it.

## Proof Of Concept
```code
$ dig test.www.midigator.com
[snipped]
;; ANSWER SECTION:
test.www.midigator.com.	60	IN	CNAME	test.www.midigator.com.s3-website-us-west-1.amazonaws.com.
test.www.midigator.com.s3-website-us-west-1.amazonaws.com. 59 IN CNAME s3-website-us-west-1.amazonaws.com.
s3-website-us-west-1.amazonaws.com. 4 IN A	52.219.193.3
```

{F1963195}

## Remediation
Remove the CNAME entry for the `test.www.midigator.com`

## Impact

Subdomain Takeover

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
