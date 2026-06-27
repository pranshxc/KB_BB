---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '278225'
original_report_id: '278225'
title: If the developer forgets to remove the built in controller welcome.php it helps
  the attacker to identify that the site is built with Codeigniter
weakness: Information Exposure Through Directory Listing
team_handle: codeigniter
created_at: '2017-10-17T16:11:32.470Z'
disclosed_at: '2017-10-18T02:35:59.544Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 4
asset_identifier: https://github.com/bcit-ci/CodeIgniter
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- information-exposure-through-directory-listing
---

# If the developer forgets to remove the built in controller welcome.php it helps the attacker to identify that the site is built with Codeigniter

## Metadata

- HackerOne Report ID: 278225
- Weakness: Information Exposure Through Directory Listing
- Program: codeigniter
- Disclosed At: 2017-10-18T02:35:59.544Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

The attacker can check the website's backend technology simply by typing site_name/index.php/welcome/index it will display the codeigniter welcome page if the developer dosen't removed the built in controller and view welcome.php and welcome_message.php i attaching a screenshot below as a proof of concept

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
