---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '172711'
original_report_id: '172711'
title: Content Spoofing in udemy
weakness: Violation of Secure Design Principles
team_handle: udemy
created_at: '2016-09-28T18:34:26.531Z'
disclosed_at: '2017-07-23T10:29:19.948Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# Content Spoofing in udemy

## Metadata

- HackerOne Report ID: 172711
- Weakness: Violation of Secure Design Principles
- Program: udemy
- Disclosed At: 2017-07-23T10:29:19.948Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Scenerio**
An attacker can include any arbitrary text using specially crafted udemy url.
Reporting this but not sure if this is in scope (text injection not marked in exclusion list)
Kindly mark it as informative in case if it is out of scope

Issue seems to be because of source_page=clp param. If this is removed text injection wont work. Also it seems error handling is not proper in case of source_object_id param since this vulnerability occur when you insert a string inside source_object_id param.

**Steps**
1) Attacker distributed the below url by means of spamming or through his website
https://www.udemy.com/api-2.0/recommended-courses/?source_action=view&source_object=course&source_object_id=},{Kindly%20move%20to%20our%20new%20beta%20website%20evil.com&source_page=clp
2) Victim see below text 
{"detail": "Invalid source object id: },{Kindly move to our new beta website evil.com"}
3) Since the text came from official site so user believes and gets into attacker trap

**Resolution**
Crafted text should not be responded back in the response HTML

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
