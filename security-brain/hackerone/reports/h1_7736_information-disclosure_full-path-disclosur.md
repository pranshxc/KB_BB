---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7736'
original_report_id: '7736'
title: FULL PATH DISCLOSUR
weakness: Information Disclosure
team_handle: concretecms
created_at: '2014-04-16T07:03:41.190Z'
disclosed_at: '2014-04-17T19:12:58.776Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- information-disclosure
---

# FULL PATH DISCLOSUR

## Metadata

- HackerOne Report ID: 7736
- Weakness: Information Disclosure
- Program: concretecms
- Disclosed At: 2014-04-17T19:12:58.776Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Full Path Disclosure (FPD) vulnerabilities enable the attacker to see the path to the webroot/file. e.g.: /home/omg/htdocs/file/. Certain vulnerabilities, such as using the load_file() (within a SQL Injection) query to view the page source, require the attacker to have the full path to the file they wish to view. 

url: 
http://enterprise.concrete5.com/

How to fix this vulnerability
Review the source code for this script.

How to replicate:
Cookie input CONCRETE5 was set to 
Error message found: 
<b>Warning</b>:  session_start() [<a href='function.session-start'>function.session-start</a>]: The session id is too long or contains illegal characters, valid characters are a-z, A-Z, 0-9 and '-,' in <b>/home/enterpri/public_html/updates/concrete5.6.1.2_updater/concrete/startup/session.php</b> on line <b>36</b><br />

as we can see clearly the full path 

Affected params : 
/ 
/index.php 
/tools/required/captcha

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
