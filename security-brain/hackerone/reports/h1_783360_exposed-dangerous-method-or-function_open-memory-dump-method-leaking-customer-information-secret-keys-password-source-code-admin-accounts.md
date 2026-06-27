---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '783360'
original_report_id: '783360'
title: Open memory dump method leaking customer information ,secret keys , password
  , source code & admin accounts
weakness: Exposed Dangerous Method or Function
team_handle: stripo
created_at: '2020-01-25T21:57:38.304Z'
disclosed_at: '2020-01-31T08:11:14.686Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 152
asset_identifier: my.stripo.email
asset_type: URL
max_severity: critical
tags:
- hackerone
- exposed-dangerous-method-or-function
---

# Open memory dump method leaking customer information ,secret keys , password , source code & admin accounts

## Metadata

- HackerOne Report ID: 783360
- Weakness: Exposed Dangerous Method or Function
- Program: stripo
- Disclosed At: 2020-01-31T08:11:14.686Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Stripo uses Spring boot for the backend API development , and misconfigured the application to open actuator APIs to the public.

This issue is found in 3 domains , don't know if I need to publish 3 reports for that, or just one report , but the domains are :
https://my.stripo.email/cabinet/stripeapi/actuator
https://plugins.stripo.email/actuator
https://plugin.stripo.email/actuator

it might be available in other micro services as well



## Steps To Reproduce:

  1. Go to the following URL : https://my.stripo.email/cabinet/stripeapi/actuator/heapdump
  1. This url will download the heap dump of the server 
  1. using a memory analyzer such as Eclipse memory analyzer or VisualVM open the downloaded file
  1. By searching inside the file you can find all the secrets , credentials , urls , JWT tokens & JWT secret keys, which can be used and generate any JWT token and takeover any account on the system.
  1. Attached some examples of what can be found and used by this vulnerability, and you can imagine any bad scenario, and this issue can be used to take over/down Stripo

## Supporting Material/References:
Please find more information about actuator on the following URL:
https://docs.spring.io/spring-boot/docs/current-SNAPSHOT/actuator-api/html/#heapdump


Example of open functionalities:
████

Admin Credentials:
███

Other User's information:
█████████

Billing Service Credentials:
████

Config Server Credentials:
███████

## Impact

This vulnerability allows any attacker to perform many severe attacks such as :

- Upgrade accounts without payments.
- Get logged in customer information and get access to the session & JWT tokes to take over accounts
- PII Data leaking 
- Accessing all credentials from the application properties such as , admin credentials, swagger credentials , billing credentials .
- Get database credentials
- Server Environment variable
- Server config Properties.
- Payments manipulations and money stealing
- and more

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
