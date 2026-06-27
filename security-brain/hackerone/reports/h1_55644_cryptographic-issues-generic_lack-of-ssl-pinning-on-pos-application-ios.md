---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '55644'
original_report_id: '55644'
title: Lack of SSL Pinning on POS Application ( iOS )
weakness: Cryptographic Issues - Generic
team_handle: shopify
created_at: '2015-04-10T07:33:09.683Z'
disclosed_at: '2015-05-21T16:10:17.309Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- cryptographic-issues-generic
---

# Lack of SSL Pinning on POS Application ( iOS )

## Metadata

- HackerOne Report ID: 55644
- Weakness: Cryptographic Issues - Generic
- Program: shopify
- Disclosed At: 2015-05-21T16:10:17.309Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

#### Description

Given that this is a POS application and handle CHD, cryptographic security is of most importance. Applications such as Square, Amazons POS, etc. have already implemented this. The iOS application is correctly checking for SSL certs using the os keychain, but due to the lack of checking for wether or not the certificate actually belongs to Sopify, the mobile app is vulnerable to MiTM attacks in which an attacker is able to install or force the user to install a certificate on the device. Given today's known issues with CAs and the lack of trust they are generating lately, Pinning on mobile devices is a technique that is becoming a standard practice. SSL Pinning is a technique for which you pin your applications or clients to one or more SSL Certificates, keys or CAs. This technique allows you to perform the normal SSL chain of trust exchange during SSL transmissions, but also checks that the SSL certificate or key within that cert is actually the one you know and trust.

#### Vulnerable platform

iOS - entire application.

#### Proof of Concept

A simple way of testing this will be to use a tool like Burp Proxy and/or mitmproxy.
Step 1) install the "malicious" cert on device and trust it. An attacker can easily trick a user to install a profile, and/or malicious applications could potentially do it as part of installation.  Step 2) Proxy all the communication through them.  Step 3) You will confirm that your application is no longer using the Certificate it should trust.

#### Recommendation

Even though this is not a high risk vulnerability, lack of SSL Pinning certainly creates an unnecessary risk for applications on mobile devices. It is our recommendation that Shopify implements SSL Pinning on iOS, and do not trust the os-level certificate store since other applications might have control over it and there is no guarantees they won't be maliciously altered. Additionally, you might have other types of attacks in which CA issue wild-card certificates to random entities, as it was recently seen with Google and a Chinese CA.
For more information please refer to 
https://www.owasp.org/index.php/Certificate_and_Public_Key_Pinning

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
