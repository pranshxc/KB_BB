---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1555440'
original_report_id: '1555440'
title: match
weakness: External Control of Critical State Data
team_handle: curl
created_at: '2022-04-30T19:22:20.287Z'
disclosed_at: '2022-06-09T07:09:50.376Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 0
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- external-control-of-critical-state-data
---

# match

## Metadata

- HackerOne Report ID: 1555440
- Weakness: External Control of Critical State Data
- Program: curl
- Disclosed At: 2022-06-09T07:09:50.376Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

## Steps To Reproduce:
lib/telnet.c suboption function incorrecly checks for the sscanf return value. Instead of checking that 2 elements are parsed, the code also continues if just one element matches:
if(sscanf(v->data, "%127[^,],%127s", varname, varval)) {
As such it is possible to construct environment values that don't update the varval buffer and instead use the previous value. In combination of advancing in the temp buffer by strlen(v->data) + 1, this means that there will be uninitialized gaps in the generated output temp buffer. These gaps will contain whatever stack contents from previous operation of the application.
Fortunately the environment is controlled by the client and not the server. As such this vulnerability can't be exploited by the server. Practical exploitation is limited by the following requirements:
attacker is able to control the environment passed to libcurl via CURLOPT_TELNETOPTIONS ("NEW_ENV=xxx,yyy") and control xxx and yyy in the curl_slist entries)
attacker is able to either inspect the network traffic of the telnet connection or to select the server/port the connection is established to
When both are true the attacker is able to some content of the stack. Note however that for this leak to be meaningful, some confidential or sensitive information would need to be leaked. This could happen if some key or other sensitive material (that is otherwise out of the reach of the attacker, due to for example setuid + dropping of privileges, or for example only being able to execute the command remotely in a limited fashion, for example php curl, or similar) would thus become visible fully, or partially. The leak is limited to maximum about half of the 2048 byte temp buffer.
Steps To Reproduce:
Run telnet service
tcpdump -i lo -X -s 65535 port 23
Execute

## Impact

lib/telnet.c suboption function incorrecly checks for the sscanf return value. Instead of checking that 2 elements are parsed, the code also continues if just one element matches:
if(sscanf(v->data, "%127[^,],%127s", varname, varval)) {
As such it is possible to construct environment values that don't update the varval buffer and instead use the previous value. In combination of advancing in the temp buffer by strlen(v->data) + 1, this means that there will be uninitialized gaps in the generated output temp buffer. These gaps will contain whatever stack contents from previous operation of the application.
Fortunately the environment is controlled by the client and not the server. As such this vulnerability can't be exploited by the server. Practical exploitation is limited by the following requirements:
attacker is able to control the environment passed to libcurl via CURLOPT_TELNETOPTIONS ("NEW_ENV=xxx,yyy") and control xxx and yyy in the curl_slist entries)
attacker is able to either inspect the network traffic of the telnet connection or to select the server/port the connection is established to
When both are true the attacker is able to some content of the stack. Note however that for this leak to be meaningful, some confidential or sensitive information would need to be leaked. This could happen if some key or other sensitive material (that is otherwise out of the reach of the attacker, due to for example setuid + dropping of privileges, or for example only being able to execute the command remotely in a limited fashion, for example php curl, or similar) would thus become visible fully, or partially. The leak is limited to maximum about half of the 2048 byte temp buffer.
Steps To Reproduce:
Run telnet service
tcpdump -i lo -X -s 65535 port 23
Execute

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
