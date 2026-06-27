---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '813279'
original_report_id: '813279'
title: Lets Encrypt Certificates affected by CAA Rechecking Incident
weakness: Improper Certificate Validation
team_handle: endless_group
created_at: '2020-03-08T19:55:54.507Z'
disclosed_at: '2020-04-01T12:38:47.167Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
asset_identifier: (*).theendlessweb.com
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- improper-certificate-validation
---

# Lets Encrypt Certificates affected by CAA Rechecking Incident

## Metadata

- HackerOne Report ID: 813279
- Weakness: Improper Certificate Validation
- Program: endless_group
- Disclosed At: 2020-04-01T12:38:47.167Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Lets encrypt released a statement regarding 3 million certificates being revoked due to a issue in the CA signing process, Looking at your subdomains it appears that you are affected by this incident. When the revoking occurs the certificates the certificates are no longer valid. This may affect automatic flows that use these sites and assume the certificates are valid and have no cert error checking. 

## Steps To Reproduce:

root@Bugslife:~/Desktop/endlesshosting# curl -XPOST -d 'fqdn=support.theendlessweb.com' https://checkhost.unboundtest.com/checkhost
The certificate currently available on support.theendlessweb.com needs renewal because it is affected by the Let's Encrypt CAA rechecking problem. Its serial number is 03a7c9ab7ac09b9e1f8772c181c584bff432. See your ACME client documentation for instructions on how to renew a certificate.

root@Bugslife:~/Desktop/endlesshosting# curl -XPOST -d 'fqdn=jira.theendlessweb.com' https://checkhost.unboundtest.com/checkhost
The certificate currently available on jira.theendlessweb.com needs renewal because it is affected by the Let's Encrypt CAA rechecking problem. Its serial number is 03a7c9ab7ac09b9e1f8772c181c584bff432. See your ACME client documentation for instructions on how to renew a certificate.

## Supporting Material/References:
https://letsencrypt.org/caaproblem/
https://threatpost.com/lets-encrypt-revoke-millions-tls-certs/153413/

## Impact

This may affect automatic flows that use these sites and assume the certificates are valid and have no cert error checking. 
As the certificates will no longer be valid this could aid in a successful phishing attack

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
