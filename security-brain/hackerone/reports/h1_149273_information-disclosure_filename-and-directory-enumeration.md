---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '149273'
original_report_id: '149273'
title: Filename and directory enumeration
weakness: Information Disclosure
team_handle: expressionengine
created_at: '2016-07-05T05:37:57.738Z'
disclosed_at: '2016-08-08T02:42:35.248Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Filename and directory enumeration

## Metadata

- HackerOne Report ID: 149273
- Weakness: Information Disclosure
- Program: expressionengine
- Disclosed At: 2016-08-08T02:42:35.248Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

The "Import File Converter" can be abused by an admin to map the server directories and files, because the "File location" field doesn't sanitize the user input and allows access to root directories and files.

## Steps to reproduce:
1- Go to http://localhost/ee/admin.php?/cp/utilities/import_converter
2- Set the "File location" to `///etc/`, notice that the error "You must have at least 3 fields: username, screen_name, and email address", proving that the file exists.
3- Try with `///strukt/`, notice the different error message, now it says "The path you submitted is not valid.", meaning the directory doesn't exist.
3- Now try with `///etc/passwd`, the first error message shows up.
4- Finally, try with `///etc/strukt`, the second message appears.

## More successful test cases:
`///etc/hosts`
`///usr/`
`///var/`
`../../../../../../../../etc/passwd`

Regards

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
