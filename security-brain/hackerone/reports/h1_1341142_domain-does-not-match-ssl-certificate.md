---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1341142'
original_report_id: '1341142'
title: Domain does not Match SSL Certificate
team_handle: acronis
created_at: '2021-09-16T08:10:34.554Z'
disclosed_at: '2021-10-05T09:20:45.666Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
---

# Domain does not Match SSL Certificate

## Metadata

- HackerOne Report ID: 1341142
- Weakness: 
- Program: acronis
- Disclosed At: 2021-10-05T09:20:45.666Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary
While examining the subdomains  for acronis.com, I noticed that https://pa.acronis.com is not currently protected by your SSL certificate.

## Steps To Reproduce
Open firefox and copy/paste the following into the search bar: https://pa.acronis.com
After you hit enter you will be transferred to 

Did Not Connect: Potential Security Issue

Firefox detected a potential security threat and did not continue to pa.acronis.com because this website requires a secure connection.

What can you do about it?

pa.acronis.com has a security policy called HTTP Strict Transport Security (HSTS), which means that Firefox can only connect to it securely. You can’t add an exception to visit this site.

The issue is most likely with the website, and there is nothing you can do to resolve it. You can notify the website’s administrator about the problem.

Learn more…

Websites prove their identity via certificates. Firefox does not trust this site because it uses a certificate that is not valid for pa.acronis.com. The certificate is only valid for the following names: *.appburst.com, appburst.com
 
Error code: SSL_ERROR_BAD_CERT_DOMAIN
 
View Certificate


  
this certificate is valid for appburst.com

## Impact

MITM Attacks - Information sent and received within https://pa.acronis.com is unprotected and it could potentially be stolen, read, or modified by attackers, hackers, and entities with access to internet infrastructure, such as Internet Service Providers (ISPs) and governments.

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
