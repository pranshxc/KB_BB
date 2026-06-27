---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1872682'
original_report_id: '1872682'
title: Privilege Esacalation at Apache Airflow 2.5.1
team_handle: ibb
created_at: '2023-02-13T15:36:00.736Z'
disclosed_at: '2023-05-18T15:47:24.381Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
asset_identifier: https://github.com/apache/airflow
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# Privilege Esacalation at Apache Airflow 2.5.1

## Metadata

- HackerOne Report ID: 1872682
- Weakness: 
- Program: ibb
- Disclosed At: 2023-05-18T15:47:24.381Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello. I found security issue about airflow's log file. 

Airflow 2.5.1 sets log files to vulnerable privileges.  (chmod 666)

Any Linux user on the host on which the airflow operates can read and tamper with the airflow's logs.

Taking advantage of this, an attacker in local host can retrieve sensitive information from a Linux host that can only access airflow accounts.  ** (This is privilege escaltion from any linux account to airflow's linux account) **
(ex : ssh private key)

** The attack conditions are as follows. **
1. An attacker can log in to a host running airflow with a specific Linux account.
(Or the penetration test was successfully successful.)

2. An attacker can log in to the airflow web server and can read the dag log.

** The attack procedure is as follows.  **

1. After deleting a specific dag log using any account, the attacker regenerates the log file using the ssh private key of the account that runs the airflow as a symbolic link.
{F2171182}

2. The attacker logs in to the airflow webserver and reads the log.
{F2171186}


3. The airflow logs expose SSH PRIVATE KEY.

{F2171190}



## Patch History 
- https://github.com/apache/airflow/pull/29506
- This vulnerability has been allocated CVE-2023-25754 by Apache Security Team.

## Impact

Local linux user can access any file like ssh private key which owned by account which operate airflow.

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
