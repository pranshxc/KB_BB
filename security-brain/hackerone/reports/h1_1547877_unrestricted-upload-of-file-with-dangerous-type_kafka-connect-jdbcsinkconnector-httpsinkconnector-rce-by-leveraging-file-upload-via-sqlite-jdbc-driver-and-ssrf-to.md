---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1547877'
original_report_id: '1547877'
title: '[Kafka Connect] [JdbcSinkConnector][HttpSinkConnector] RCE by leveraging file
  upload via SQLite JDBC driver and SSRF to internal Jolokia'
weakness: Unrestricted Upload of File with Dangerous Type
team_handle: aiven_ltd
created_at: '2022-04-22T12:20:17.321Z'
disclosed_at: '2022-11-08T06:29:22.109Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 50
asset_identifier: 'Aiven for Apache Kafka managed and hosted service '
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- unrestricted-upload-of-file-with-dangerous-type
---

# [Kafka Connect] [JdbcSinkConnector][HttpSinkConnector] RCE by leveraging file upload via SQLite JDBC driver and SSRF to internal Jolokia

## Metadata

- HackerOne Report ID: 1547877
- Weakness: Unrestricted Upload of File with Dangerous Type
- Program: aiven_ltd
- Disclosed At: 2022-11-08T06:29:22.109Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
The Aiven JDBC sink includes the SQLite JDBC Driver. This JDBC driver can be used to upload SQLite database files onto the server. The HTTP sink connector allows sending HTTP requests to localhost. There is unprotected Jolokia listening on `localhost:6725`.  JMX exports the `com.sun.management:type=DiagnosticCommand` MBean, which contains the `jvmtiAgentLoad` operation. This operation can be used to execute the SQLite database as JVM Agent by embedding the JVM Agent JAR file inside the SQLite database as an BLOB field in a table.

## Steps To Reproduce:

{F1703051}

  1. Login into my VPS: `ssh ████`, password: `█████████@`
  1. Execute `nc -nlvp 4446`
  1. cd to `jdbc-sqlite-jolokia-rce` and run `python3 poc.py` (if running locally, install kafka-python using pip first).
  1. Reverse shell connection should now be established to my test instance

## Impact

RCE on the Kafka Connect server

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
