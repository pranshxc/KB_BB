---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '147570'
original_report_id: '147570'
title: Local File Inclusion path bypass
weakness: Violation of Secure Design Principles
team_handle: concretecms
created_at: '2016-06-27T00:36:05.950Z'
disclosed_at: '2016-08-19T00:17:46.666Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- violation-of-secure-design-principles
---

# Local File Inclusion path bypass

## Metadata

- HackerOne Report ID: 147570
- Weakness: Violation of Secure Design Principles
- Program: concretecms
- Disclosed At: 2016-08-19T00:17:46.666Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey,

After reading egix's report #59665 and seeing your fix at https://github.com/concrete5/concrete5/commit/19d0cc81c7cd485b856289ac71ebc0389ea7c3da & https://github.com/concrete5/concrete5/commit/c646dd0defcfa79ef119dca8ba1beba2c5bc91ea I think the fixes are insufficient to stop lfi.

If you are going to stick with the `strpos()` trick, you missed something. 
```php
$path = $request->getPathInfo();
$path = rawurldecode($request->getPathInfo());
 if (substr($path, 0, 3) == '../' || substr($path, -3) == '/..' || strpos($path, '/../') ||
     substr($path, 0, 3) == '..\\' || substr($path, -3) == '\\..' || strpos($path, '\\..\\')) {
``` 
while that is one way to go. you forgot about "../\", " ..\/", "/\.." & "\/.." this works because some oses (unix like) parse the backslash to forward slash and proceed. add those and I think you should be fine. :)

Thanks,
P

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
