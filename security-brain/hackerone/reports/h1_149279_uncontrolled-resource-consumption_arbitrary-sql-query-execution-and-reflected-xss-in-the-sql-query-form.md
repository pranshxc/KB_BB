---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '149279'
original_report_id: '149279'
title: Arbitrary SQL query execution and reflected XSS in the "SQL Query Form"
weakness: Uncontrolled Resource Consumption
team_handle: expressionengine
created_at: '2016-07-05T06:37:06.437Z'
disclosed_at: '2016-08-18T02:22:07.937Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Arbitrary SQL query execution and reflected XSS in the "SQL Query Form"

## Metadata

- HackerOne Report ID: 149279
- Weakness: Uncontrolled Resource Consumption
- Program: expressionengine
- Disclosed At: 2016-08-18T02:22:07.937Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

The mentioned module is vulnerable to SQL injection due to the fact that a query can be done in a GET request, with the query is Base64 encoded and supplied as the value of the parameter "thequery".

This allows an attacker to perform arbitrary SQL queries if they trick an authenticated admin to click a specially crafted link, which can have devastating outcomes, including the deletion/dropping of whole records/databases, the insertion of new data, etc, following is a PoC:

http://localhost/ee/admin.php?/cp/utilities/query/run-query&thequery=c2VsZWN0ICogZnJvbSBleHBfbWVtYmVycw==

With c2VsZWN0ICogZnJvbSBleHBfbWVtYmVycw== as the Base64 encoded form of `select * from exp_members`.
Also, the same GET parameter is vulnerable to reflected XSS, which originates from the fact that MySQL errors get thrown unencoded when a malformed SQL query is processed. This, in combination with the previously mentioned flaw, can make an attacker not only capable of executing arbitrary SQL queries, but also able to read whatever data is returned from a query, in addition to the normal attacks that can be done with an XSS, following is a PoC:

http://localhost/ee/admin.php?/cp/utilities/query/run-query&thequery=c2VsZWN0IDxzdmcgb25sb2FkPWFsZXJ0KDEpPg==

Where c2VsZWN0IDxzdmcgb25sb2FkPWFsZXJ0KDEpPg== is the Base64 encoded form of `select <svg onload=alert(1)>`.

Regards

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
