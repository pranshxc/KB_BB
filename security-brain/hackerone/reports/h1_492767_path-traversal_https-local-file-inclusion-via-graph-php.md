---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '492767'
original_report_id: '492767'
title: '[https://███] Local File Inclusion via graph.php'
weakness: Path Traversal
team_handle: deptofdefense
created_at: '2019-02-08T05:31:44.009Z'
disclosed_at: '2020-05-14T16:56:23.335Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- path-traversal
---

# [https://███] Local File Inclusion via graph.php

## Metadata

- HackerOne Report ID: 492767
- Weakness: Path Traversal
- Program: deptofdefense
- Disclosed At: 2020-05-14T16:56:23.335Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

There exists a Local File Inclusion vulnerability on https://████ due to a known vulnerability in the ZendTo library. This was fixed in [Version 5.16-6 Beta](https://zend.to/changelog.php), although ██████ is still running ZendTo 5.11.

## Impact

This allows path traversal in a file name that is then returned to the user. Depending on the PHP version ████ is running, this may allow escaping the appended suffix and reading arbitrary local files, which would allow complete compromise of the ██████ system.

## Step-by-step Reproduction Instructions

To reproduce, this requires being an ████████ account. This could be exploited by sending a malicious link to an ████████ of ████████.

1. If you have access to an █████ account on █████████, visit `https://█████/graph.php?p=7&m=../../../../../../usr/share/apache2/icons/pie` as a POC. This loads an image of a pie, demonstrating the path traversal vulnerability.
2. Without access to an ████ account, visit my server at https://████/ and log in with username `████████` and password `██████`.
3. Visit https://████/graph.php?m=dropoff_count&p=7&m=../../../../../../usr/share/apache2/icons/pie. Observe the tiny image of a pie, demonstrating path traversal.

## Vulnerable Code

The following block of code (in `graph.php`) reads a file from the `m` parameter unfiltered:

```
if ( $period && ($metric = $_GET['m']) || ($metric = $_POST['metric']) ) {
      if ( is_readable($path = RRD_DATA_DIR.$metric.$period.'.png') ) {
        readfile($path);
        exit(0);
      }
    }
```

## Product, Version, and Configuration (If applicable)

ZendTo < 5.16-6 Beta

## Suggested Mitigation/Remediation Actions

Update the ZendTo software.

## Impact

.

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
