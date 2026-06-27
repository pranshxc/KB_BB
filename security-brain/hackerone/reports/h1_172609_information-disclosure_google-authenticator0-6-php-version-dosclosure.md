---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '172609'
original_report_id: '172609'
title: Google Authenticator0.6 - PHP Version Dosclosure
weakness: Information Disclosure
team_handle: iandunn-projects
created_at: '2016-09-28T11:06:04.639Z'
disclosed_at: '2016-10-06T17:18:48.682Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 1
tags:
- hackerone
- information-disclosure
---

# Google Authenticator0.6 - PHP Version Dosclosure

## Metadata

- HackerOne Report ID: 172609
- Weakness: Information Disclosure
- Program: iandunn-projects
- Disclosed At: 2016-10-06T17:18:48.682Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hello
#Vulnerable File and Link :
`http://localhost/wordpress/wp-content/plugins/google-authenticator-per-user-prompt/views/requirements-error.php`


#Vulnerable Link :
8
`<em>(You're running version <?php echo PHP_VERSION; ?>)</em>`

#Vulnerable Code:
`<?php echo PHP_VERSION; ?>`

Good Luck/

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
