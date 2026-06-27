---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '277525'
original_report_id: '277525'
title: Formula injection via CSV exports in WordCamp Talks plugin
weakness: Command Injection - Generic
team_handle: iandunn-projects
created_at: '2017-10-15T23:19:41.070Z'
disclosed_at: '2017-10-23T18:47:08.830Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- command-injection-generic
---

# Formula injection via CSV exports in WordCamp Talks plugin

## Metadata

- HackerOne Report ID: 277525
- Weakness: Command Injection - Generic
- Program: iandunn-projects
- Disclosed At: 2017-10-23T18:47:08.830Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The WordCamp Talks plugin does not attempt to sanitize CSV exports, which can lead to spreadsheet formula injection via malicious inputs.

POC
========

* Submit a new talk with the title of `=1+1`. 
* Visit the All Talks page (/wp-admin/edit.php?post_type=talks)
* Click the CSV Export link
* Open the downloaded file in Excel, Numbers, or similar
* Note that the talk's title is displayed as `2`, showing the title was imported as a formula.

Impact
===========

Excel allows external commands to be executed via formulas after a warning prompt. The warning says "Do not enable this content unless you trust the source of this file", but since most users _do_ trust the source (their WordCamp site), they may be more likely to allow it.

Lots of arbitrary commands can be executed this way, including installing other commands in a way that can bypass antivirus scanning. 

More details can be found at https://pentestmag.com/formula-injection/

Remedy
=========

`wct_generate_csv_content()` needs to ensure that the first character in each value is not one of `=`, `-`, or `+`. These can come from several columns such as the title, categories, and tags, so all data should be sanitized.

Further info:

https://www.owasp.org/index.php/CSV_Excel_Macro_Injection
https://hackerone.com/reports/72785

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
