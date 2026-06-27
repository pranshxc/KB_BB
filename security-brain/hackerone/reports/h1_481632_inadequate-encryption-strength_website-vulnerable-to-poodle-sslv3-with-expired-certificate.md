---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '481632'
original_report_id: '481632'
title: Website vulnerable to POODLE (SSLv3) with expired certificate
weakness: Inadequate Encryption Strength
team_handle: deptofdefense
created_at: '2019-01-17T21:04:34.918Z'
disclosed_at: '2021-04-02T18:53:00.392Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- inadequate-encryption-strength
---

# Website vulnerable to POODLE (SSLv3) with expired certificate

## Metadata

- HackerOne Report ID: 481632
- Weakness: Inadequate Encryption Strength
- Program: deptofdefense
- Disclosed At: 2021-04-02T18:53:00.392Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
████████ uses insecure cipher suites (SSL V2 and SSL V3) which makes it vulnerable to many attacks, including POODLE. The ssl certificate has also expired 4 years ago.

##Impact

The POODLE attack can be used against any system or application that supports SSL 3.0 with CBC mode ciphers. This affects most current browsers and websites, but also includes any software that either references a vulnerable SSL/TLS library (e.g. OpenSSL) or implements the SSL/TLS protocol suite itself. By exploiting this vulnerability in a likely web-based scenario, an attacker can gain access to sensitive data passed within the encrypted web session, such as passwords, cookies and other authentication tokens that can then be used to gain more complete access to a website (impersonating that user, accessing database content, etc.).

## Suggested Mitigation/Remediation Actions

Disable SSL 2 and SSL 3, renew the certificate and disable weak cyphers like RC4 to further mitigate other issues.

**Sources:**
https://www.us-cert.gov/ncas/alerts/TA14-290A

## Impact

The POODLE attack can be used against any system or application that supports SSL 3.0 with CBC mode ciphers. This affects most current browsers and websites, but also includes any software that either references a vulnerable SSL/TLS library (e.g. OpenSSL) or implements the SSL/TLS protocol suite itself. By exploiting this vulnerability in a likely web-based scenario, an attacker can gain access to sensitive data passed within the encrypted web session, such as passwords, cookies and other authentication tokens that can then be used to gain more complete access to a website (impersonating that user, accessing database content, etc.).

**Example**:
 http://██████/███ would be vulnerable to this assuming the credentials were transmitted using HTTPS (which they aren't and this is a vulnerability itself).

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
