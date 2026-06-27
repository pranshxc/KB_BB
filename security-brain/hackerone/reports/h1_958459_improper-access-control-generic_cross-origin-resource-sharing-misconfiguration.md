---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '958459'
original_report_id: '958459'
title: Cross Origin Resource Sharing Misconfiguration
weakness: Improper Access Control - Generic
team_handle: acronis
created_at: '2020-08-14T07:23:37.889Z'
disclosed_at: '2023-01-10T09:06:04.183Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
asset_identifier: '*.acronis.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Cross Origin Resource Sharing Misconfiguration

## Metadata

- HackerOne Report ID: 958459
- Weakness: Improper Access Control - Generic
- Program: acronis
- Disclosed At: 2023-01-10T09:06:04.183Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Description :-
Cross-Origin Resource Sharing (CORS) is a mechanism that uses additional HTTP headers to tell browsers to give a web application running at one origin, access to selected resources from a different origin. The CORS mechanism supports secure cross-origin requests and data transfers between browsers and servers.

## Remediation :-

To mitigate the risk of CORS, we always recommend whitelisting your Access-Control-Allow-Origin instead of wildcarding. Using a 

wildcard prefix such as *.yoursite.com makes it more difficult for the attackers given they would need to find a vulnerability (such as 

cross-site scripting or cross-site request forgery) to issue the cross-origin request. However, it is frowned upon because it does not 

provide the critical need-to-know security control. With whitelisting, the scope of your Access-Control-Allow-Origin will be limited to 

only the sites that deal directly with your primary site or API and exclude any of your sites that do not.

##Steps to Reproduce :-

1. Open the Vulnerable URL : https://motorsport.tech/wp-json
2.  Now intercept the request using burp suite or CURL and add one header like following :
Origin: https://evil.com (You can use anything as website.)
3. In response headers you will notice following headers :
"
```Access-Control-Allow-Origin: https://evil.com ```
```Access-Control-Allow-Methods: OPTIONS,GET,POST,PATCH,DELETE ```
```Access-Control-Allow-Credential: true ```
"
4.  A malicious user can put his own domain or localhost as origin and capture the request.

## Impact

A CORS misconfiguration can leave the application at a high-risk of compromise resulting in an impact on the confidentiality and 

integrity of data by allowing third-party sites to carry out privileged requests through your web site’s authenticated users such as 

retrieving user setting information or saved payment card data.

On the other hand, the risk is low for applications that deal with public data and require that resources are sent to other origins. 

The configuration could be expected behaviour and it would need to be up to the penetration tester to identify the appropriate risk and 

the organization to understand and mitigate, or accept the risk.

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
