---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1626205'
original_report_id: '1626205'
title: Wordpress Takeover using setup configuration at http://████.edu [HtUS]
weakness: Misconfiguration
team_handle: deptofdefense
created_at: '2022-07-05T14:01:40.782Z'
disclosed_at: '2023-01-13T18:04:31.536Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 97
tags:
- hackerone
- misconfiguration
---

# Wordpress Takeover using setup configuration at http://████.edu [HtUS]

## Metadata

- HackerOne Report ID: 1626205
- Weakness: Misconfiguration
- Program: deptofdefense
- Disclosed At: 2023-01-13T18:04:31.536Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Description:

The WordPress 'setup-config.php' installation page allows users to install
WordPress in local or remote MySQL databases. This typically requires a user
to have valid MySQL credentials to complete.  However, a malicious user can
host their own MySQL database server and can successfully complete the
WordPress installation without having valid credentials on the target system.


Reproduce step by step:

I found this vulnerable url:
http://███.edu/old/wp-admin/setup-config.php

Then i configured db 
I used this site https://www.freemysqlhosting.net/

After configure I got wordpress admin access

proof:
http://██████████.edu/old/rce.txt


Admin credentials that I set after installing the config
username: ████████
password: ███

Login Panel: http://████████.edu/old/wp-login.php

Video POC has been attached as well.

## Impact

Impact
Remote Code Execution/Total system compromise.
Attacker can upload webshell into the server. I did not upload any shell for security violation.

Malware distribution
Phishing / Spear phishing
XSS
Authentication bypass

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
