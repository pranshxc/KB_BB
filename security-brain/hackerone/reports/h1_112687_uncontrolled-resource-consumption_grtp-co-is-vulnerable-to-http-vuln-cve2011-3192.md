---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '112687'
original_report_id: '112687'
title: grtp.co is vulnerable to http-vuln-cve2011-3192
weakness: Uncontrolled Resource Consumption
team_handle: gratipay
created_at: '2016-01-25T13:01:41.394Z'
disclosed_at: '2016-02-12T13:41:33.456Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- uncontrolled-resource-consumption
---

# grtp.co is vulnerable to http-vuln-cve2011-3192

## Metadata

- HackerOne Report ID: 112687
- Weakness: Uncontrolled Resource Consumption
- Program: gratipay
- Disclosed At: 2016-02-12T13:41:33.456Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

vulnerability i have found!

| http-vuln-cve2011-3192: 

|   VULNERABLE:

|   Apache byterange filter DoS

|     State: VULNERABLE

|     IDs:  CVE:CVE-2011-3192  OSVDB:74721

|       The Apache web server is vulnerable to a denial of service attack when numerous

|       overlapping byte ranges are requested.

|     Disclosure date: 2011-08-19

About Vulnerability

The byterange filter in the Apache HTTP Server 2.0.x through 2.0.64, and 2.2.x through 2.2.19 allows remote attackers to cause a denial of service (memory and CPU consumption) via a Range header that expresses multiple overlapping ranges, exploit called "Apache Killer"

i have tested it using nmap and metasploit and is 100% vulnerable
when i found it i tested it in metasploit i used  auxiliary/dos/http/apache_range_dos

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
