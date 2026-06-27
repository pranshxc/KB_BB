---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '643442'
original_report_id: '643442'
title: Unauthenticated reflected XSS in preview_as_user function
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: concretecms
created_at: '2019-07-15T11:36:41.063Z'
disclosed_at: '2019-12-06T15:48:41.839Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
asset_identifier: https://github.com/concrete5/concrete5
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Unauthenticated reflected XSS in preview_as_user function

## Metadata

- HackerOne Report ID: 643442
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: concretecms
- Disclosed At: 2019-12-06T15:48:41.839Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

An unauthenticated, reflected cross-site-scripting attack is possible due to the unsanitised `cID` parameter in the preview_as_user functionality.

Example URL: `https://LOCAL-CONCRETE-INSTALL/ccm/system/panels/page/preview_as_user/preview?cID=%22%3E%3C/iframe%3E%3Cscript%3Ealert(1)%3C/script%3E%3C!--`

The error is in the `concrete/views/panels/page/preview_as/frame.php` file, line 4:
```
[..]
src="<?= URL::to('/ccm/system/panels/page/preview_as_user/render') . '?&cID=' . Request::request('cID') ?>
[..]
```

Solutions would be to either cast this value to an int with `intval()`, or pass the value through `htmlentities()` before rendering it. Or both!

## Impact

An attacker could steal cookies or perform actions on other users behalf.

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
