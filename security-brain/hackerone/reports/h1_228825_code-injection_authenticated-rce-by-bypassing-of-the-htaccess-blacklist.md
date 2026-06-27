---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '228825'
original_report_id: '228825'
title: (Authenticated) RCE by bypassing of the .htaccess blacklist
weakness: Code Injection
team_handle: nextcloud
created_at: '2017-05-16T13:42:57.976Z'
disclosed_at: '2020-03-01T11:02:56.685Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- code-injection
---

# (Authenticated) RCE by bypassing of the .htaccess blacklist

## Metadata

- HackerOne Report ID: 228825
- Weakness: Code Injection
- Program: nextcloud
- Disclosed At: 2020-03-01T11:02:56.685Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

`Storage::copyFromStorage` doesn't check the content of a folder it copies against the list of blacklisted files.
Meaning that if a user has access to an external storage (inc. fed. shares) that contains a .htaccess file, he can move the .htaccess file to the local data directory.

The attack works on any nextcloud/owncloud since federated sharing was introduced that uses apache and has the data directory inside the webroot (as is default)

Steps to reproduce:
- Setup an evil instance (nc1) that has the file blacklist disabled (Filesystem.php line 616)
- create a folder 'sharefolder/attack' in nc1 with the following files
  - .htaccess configured to "allow from all"
  - attack.php with the desired attack
- Setup a non-evil instance (nc2) (or pick an existing nc instance that you want to attack)
- Federated share 'sharefolder' from nc1 to nc2
- In nc2, move 'sharefolder/attack' to 'attack' (outside the share)
- navigate to http://nc2/data/userid/files/attack/attack.php

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
