---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '499'
original_report_id: '499'
title: 'Ruby: Heap Overflow in Floating Point Parsing'
team_handle: ruby
created_at: '2013-11-22T00:00:00.000Z'
disclosed_at: '2013-11-22T00:00:00.000Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
tags:
- hackerone
---

# Ruby: Heap Overflow in Floating Point Parsing

## Metadata

- HackerOne Report ID: 499
- Weakness: 
- Program: ruby
- Disclosed At: 2013-11-22T00:00:00.000Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Any time a string is converted to a floating point value, a specially crafted string can cause a heap overflow. This can lead to a denial of service attack via segmentation faults and possibly arbitrary code execution. Any program that converts input of unknown origin to floating point values (especially common when accepting JSON) are vulnerable.

Vulnerable code looks something like this:

`untrusted_data.to_f`

But any code that produces floating point values from external data is vulnerable, such as this:

`JSON.parse untrusted_data`

Note that this bug is similar to CVE-2009-0689.

All users running an affected release should upgrade to the FIXED versions of Ruby.

#Affected versions
- All Ruby 1.8 versions
- All Ruby 1.9 versions prior to Ruby 1.9.3 patchlevel 484
- All Ruby 2.0 versions prior to Ruby 2.0.0 patchlevel 353
- All Ruby 2.1 versions prior to Ruby 2.1.0 preview2
- prior to trunk revision 43780

#Solutions
All users are recommended to upgrade to Ruby 1.9.3 patchlevel 484, Ruby 2.0.0 patchlevel 353 or Ruby 2.1.0 preview2.

Please note that Ruby 1.8 series or any earlier releases are already obsoleted. There is no plan to release new FIXED versions for them. Users of such versions are advised to upgrade as soon as possible as we cannot guarantee the continued availability of security fixes for unsupported releases.

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
