---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1619536'
original_report_id: '1619536'
title: xmlrpc.php file enabled at ██████.org
weakness: Violation of Secure Design Principles
team_handle: deptofdefense
created_at: '2022-06-29T18:31:54.056Z'
disclosed_at: '2023-03-24T17:29:26.048Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- violation-of-secure-design-principles
---

# xmlrpc.php file enabled at ██████.org

## Metadata

- HackerOne Report ID: 1619536
- Weakness: Violation of Secure Design Principles
- Program: deptofdefense
- Disclosed At: 2023-03-24T17:29:26.048Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
XML-RPC on WordPress is actually an API that allows developers who make 3rd party application and services the ability to interact to your WordPress site. The XML-RPC API that WordPress provides several key functionalities that include:

Publish a post
Edit a post
Delete a post.
Upload a new file (e.g. an image for a post)
Get a list of comments
Edit comments
For instance, the Windows Live Writer system is capable of posting blogs directly to WordPress because of XML-RPC.

Unfortunately on the normal installation (not tampered with settings, and/or configs) of WordPress the XML-RPC interface opens two kinds of attacks:

XML-RPC pingbacks
Brute force attacks via XML-RPC
##References
https://medium.com/@the.bilal.rizwan/wordpress-xmlrpc-php-common-vulnerabilites-how-to-exploit-them-d8d3c8600b32
https://medium.com/@protector47/how-to-hack-wordpress-website-via-xmlrpc-php-61c813fa3740
https://hackerone.com/reports/325040?fbclid=IwAR0qgG-Xfzfi8epruslb_aB91f-Nj8DitF0su8O9ibFKSFdvefJ8h_qWNyc
https://hackerone.com/reports/752073?fbclid=IwAR2i3AM4woHlr01MvyJR-Vu485XQg_gxb1doWmAhSBTfxPK9cUSRFxO2iFo

## Impact

-->XML-RPC pingbacks
-->Brute force attacks via XML-RPC

## System Host(s)
███.org

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1) Go to https://█████████.org/xmlrpc.php to check if it is enabled or not.
2)If it is enabled, change the HTTP header to POST and make the following requests as shown in the POC

## Suggested Mitigation/Remediation Actions
Disable or remove the xmlrpc.php file completely.

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
