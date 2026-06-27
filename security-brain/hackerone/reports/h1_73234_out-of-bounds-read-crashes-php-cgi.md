---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '73234'
original_report_id: '73234'
title: out of bounds read crashes php-cgi
team_handle: ibb
created_at: '2014-12-17T00:00:00.000Z'
disclosed_at: '2014-12-30T00:00:00.000Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
---

# out of bounds read crashes php-cgi

## Metadata

- HackerOne Report ID: 73234
- Weakness: 
- Program: ibb
- Disclosed At: 2014-12-30T00:00:00.000Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I found and disclosed CVE-2014-9427 to the PHP dev team on 17 December 2014 (https://bugs.php.net/bug.php?id=68618) and a patch was committed on 30 December 2014 (http://git.php.net/?p=php-src.git;a=commit;h=f9ad3086693fce680fbe246e4a45aa92edd2ac35) and the flaw is now fixed.

Details of the flaw: sapi/cgi/cgi_main.c in the CGI component in PHP through 5.4.36, 5.5.x through 5.5.20, and 5.6.x through 5.6.4, when mmap is used to read a .php file, does not properly consider the mapping's length during processing of an invalid file that begins with a # character and lacks a newline character, which causes an out-of-bounds read and might (1) allow remote attackers to obtain sensitive information from php-cgi process memory by leveraging the ability to upload a .php file or (2) trigger unexpected code execution if a valid PHP script is present in memory locations adjacent to the mapping.

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
