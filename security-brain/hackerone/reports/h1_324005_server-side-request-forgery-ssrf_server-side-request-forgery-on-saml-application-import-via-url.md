---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '324005'
original_report_id: '324005'
title: Server-Side Request Forgery on SAML Application - Import via URL
weakness: Server-Side Request Forgery (SSRF)
team_handle: pingidentity
created_at: '2018-03-09T21:57:40.049Z'
disclosed_at: '2019-03-26T20:44:06.747Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
asset_identifier: https://ort-admin.pingone.com/*
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# Server-Side Request Forgery on SAML Application - Import via URL

## Metadata

- HackerOne Report ID: 324005
- Weakness: Server-Side Request Forgery (SSRF)
- Program: pingidentity
- Disclosed At: 2019-03-26T20:44:06.747Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Summary
==

The My Applications feature on PingOne Identity admin allows you to add new SAML applications to your account. One feature allows you to import metadata via URI instead of via upload. This uses Java 1.8 to make an external web request to the URI supplied. Typically this is hard to validate if it's a vulnerability or not because it functions as intended. However, the error responses I was able to get back suggests it can hit internal services and you can perform recon or attack internal services using it.

Steps
==
1. Go to My Applications and click the Add Application button:
 * https://ort-admin.pingone.com/web-portal/cas/connections
2. Fill out basic details and go to the next step
3. Next to Upload metadata, select `or use URL`
4. Try these URLs:
 * https://localhost
 * https://localhost:22
 * http://169.254.169.254/latest/meta-data/
 * http://169.254.169.254/latest/meta-data/a
5. ---> The error responses determine it's hitting internal resources you specify.

Additional Info
==

https://localhost response:
 * `The issuer of the server X.509 certificate at this address is not in PingOne's trusted authority list.`

https://localhost:22 response:
 * `We could not connect to the address 'https://localhost:22'.`

http://169.254.169.254/latest/meta-data/ response:
 * `<ajax-response><redirect><![CDATA[../error]]></redirect></ajax-response>`

http://169.254.169.254/latest/meta-data/a response:
 * `We could not connect to the address &#039;http://169.254.169.254/latest/meta-data/a&#039;.`

## Impact

Server-Side Request Forgery that allows internal requests and provides useful feedback on errors could lead an attacker to mapping internal services and hosts. If there are any vulnerable services such as internal APIs, old ElasticSearch, etc it could lead to an attacker escalating to more critical vulnerabilities.

The hacker selected the **Server-Side Request Forgery (SSRF)** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**Can internal services be reached bypassing network access control?**
Yes

**What internal services were accessible?**
https://localhost
Internal AWS meta data

**Security Impact**
This allows you to hit internal IPs and hostnames in the AWS environment. Any application or host that has security groups preventing external access could potentially be discovered and exploited. Due to no response back, it would mostly be used for recon against internal services/ports.

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
