---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1578574'
original_report_id: '1578574'
title: unauth mosquitto ( client emails, ips, license keys exposure )
weakness: Improper Access Control - Generic
team_handle: acronis
created_at: '2022-05-23T07:23:08.949Z'
disclosed_at: '2022-07-18T11:39:34.544Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 17
asset_identifier: '*.acronis.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# unauth mosquitto ( client emails, ips, license keys exposure )

## Metadata

- HackerOne Report ID: 1578574
- Weakness: Improper Access Control - Generic
- Program: acronis
- Disclosed At: 2022-07-18T11:39:34.544Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi team

## Summary
connect.acronis.com ( ip 88.99.142.45:1883 ) has unauth mosquitto mqtt, anyone can connect and read\write messages

## Steps To Reproduce
[add details for how we can reproduce the issue]

  1. https://github.com/bapowell/python-mqtt-client-shell
  1. python3 mqtt_client_shell.py
  1. connection
  1. host 88.99.142.45
   1. connect
   1. subscribe "#" 1


```
Payload (str): b'{"host":"nusite", "tag":"nusite-licenser", "level":"debug", "msg":" response: {\'commands\': [],
 \'license_info\': {\'licensee_name\': \'██████████\',
 \'license_key\': \'█████████\', \'support_exp_date\': \'2021-11-30\',
 \'licensed_actions\': [{\'names\': [\'*\'], \'rules\': [{\'ops\': [{\'action\': \'allow\'}]}]}]}, \'signature\': \'\'}"}'
```

█████


## Recommendations
enable authentication

Thanks

## Impact

access to client data, possibility to write messages to unauth mqtt

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
