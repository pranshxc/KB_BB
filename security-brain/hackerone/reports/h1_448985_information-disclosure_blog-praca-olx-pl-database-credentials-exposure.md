---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '448985'
original_report_id: '448985'
title: blog.praca.olx.pl database credentials exposure
weakness: Information Disclosure
team_handle: olx
created_at: '2018-11-23T03:05:53.566Z'
disclosed_at: '2018-12-26T12:46:58.267Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- information-disclosure
---

# blog.praca.olx.pl database credentials exposure

## Metadata

- HackerOne Report ID: 448985
- Weakness: Information Disclosure
- Program: olx
- Disclosed At: 2018-12-26T12:46:58.267Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi, I found that the site blog.praca.olx.pl is exposing the content of wp-config.php file in plaintext due that a misconfiguration in the file-manager plugin.

The information can be accessed here: http://blog.praca.olx.pl/wp-content/uploads/file-manager/log.txt

The credentials are stored in the log.txt file as can be seen in the following image:
{F379634}

An attacker could use this information for further attacks.

Regards,

## Impact

An attacker could use this information for further attacks if the database access is achieved all the information of the blog will be in risk and could be used to achieved remote code execution via file upload in the admin panel.

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
