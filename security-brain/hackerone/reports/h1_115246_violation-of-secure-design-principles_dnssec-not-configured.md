---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '115246'
original_report_id: '115246'
title: DNSsec not configured
weakness: Violation of Secure Design Principles
team_handle: paragonie
created_at: '2016-02-07T19:49:58.454Z'
disclosed_at: '2016-04-27T00:31:58.610Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# DNSsec not configured

## Metadata

- HackerOne Report ID: 115246
- Weakness: Violation of Secure Design Principles
- Program: paragonie
- Disclosed At: 2016-04-27T00:31:58.610Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Description:

I found out that there is no DNSSEC configured on your webserver to prevent DNS related attacks. This is an issue that would allow attackers to target your DNS directly The Domain Name System Security Extensions (DNSSEC) is a suite of Internet Engineering Task Force (IETF) specifications for securing certain kinds of information provided by the Domain Name System (DNS) as used on Internet Protocol (IP) networks. It is a set of extensions to DNS which provide to DNS clients (resolvers) origin authentication of DNS data, authenticated denial of existence, and data integrity, but not availability or confidentiality. You guys have not become popular among web vendors this is one thing that you should take under consideration Hope this helps

Steps to reproduce:

http://dnssec-debugger.verisignlabs.com/paragonie.com

Check the above results for paragonie.com

And from the local server visit this URL https://dnssectest.sidnlabs.nl/test.php It will also show you that you are not protected against DNSsec related attack

Suggested fix
Enable DNSsec.

Regards:
Vicky

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
