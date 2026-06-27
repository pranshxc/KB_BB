---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1019372'
original_report_id: '1019372'
title: Parallel upload hangs curl if upload file not found
weakness: Uncontrolled Resource Consumption
team_handle: curl
created_at: '2020-10-26T21:42:14.273Z'
disclosed_at: '2020-10-29T16:24:29.914Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Parallel upload hangs curl if upload file not found

## Metadata

- HackerOne Report ID: 1019372
- Weakness: Uncontrolled Resource Consumption
- Program: curl
- Disclosed At: 2020-10-29T16:24:29.914Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Attempting to upload (-T) a not found file with parallel (-Z) flag present, will cause curl to get stuck and never terminate, potentially stalling scripts that make use of this particular flags. 

curl -T blabla-notexists -Z upload.example.com www.google.com www.cnn.com www.apple.com


Same issue occurs if using -Z or --parallel flags.


$ curl -T blabla-notexists -Z upload.example.com www.google.com www.cnn.com www.apple.com
curl: Can't open 'blabla-notexists'!
curl: try 'curl --help' or 'curl --manual' for more information
DL% UL%  Dled  Uled  Xfers  Live   Qd Total     Current  Left    Speed
--  --      0     0     1     0     1 --:--:--  0:00:01 --:--:--     0      curl: Can't open 'blabla-notexists'!
curl: try 'curl --help' or 'curl --manual' for more information
curl: Can't open 'blabla-notexists'!
curl: try 'curl --help' or 'curl --manual' for more information
curl: Can't open 'blabla-notexists'!
curl: try 'curl --help' or 'curl --manual' for more information
curl: Can't open 'blabla-notexists'!
curl: try 'curl --help' or 'curl --manual' for more information
curl: Can't open 'blabla-notexists'!
curl: try 'curl --help' or 'curl --manual' for more information
curl: Can't open 'blabla-notexists'!
curl: try 'curl --help' or 'curl --manual' for more information
curl: Can't open 'blabla-notexists'!
curl: try 'curl --help' or 'curl --manual' for more information
curl: Can't open 'blabla-notexists'!
curl: try 'curl --help' or 'curl --manual' for more information
curl: Can't open 'blabla-notexists'!
curl: try 'curl --help' or 'curl --manual' for more information
curl: Can't open 'blabla-notexists'!
curl: try 'curl --help' or 'curl --manual' for more information



Doesn't happen with --parallel-max or --parallel-immediate flags.

Observing the network with tcpdump, shows NO traffic at all.


I suspect this is just an ordinary bug, but reporting it in case there is a security angle that might be present. Really the only obvious security issue is that curl will block possibly forever, and if curl tool is used inside a script or binary (via system() for example) could cause that script/binary to stop/block/hang.  In some cases, this could lead to a bad situation, leading to denial of service or loss of service availability for program/process/server/service using curl in such a way.

Not 100% sure, but I suspect that libcurl does not have this issue.  I could be wrong.


Steps to Reproduce:
Upload (-T) a file with curl while in parallel mode (-Z) and the upload file must not exist locally.

curl -T blabla-notexists -Z upload.example.com www.google.com www.cnn.com www.apple.com

## Impact

curl hangs leading to denial of service or loss of service availablity for script or binary using curl CLI tool.


Mitigation:
Don't use -Z parallel flag with -T upload flag.

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
