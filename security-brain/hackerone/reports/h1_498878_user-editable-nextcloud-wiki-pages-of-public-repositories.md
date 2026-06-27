---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '498878'
original_report_id: '498878'
title: User Editable nextcloud Wiki pages of Public Repositories
team_handle: nextcloud
created_at: '2019-02-20T22:00:44.232Z'
disclosed_at: '2019-08-31T12:32:06.581Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
asset_identifier: nextcloud/logreader
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# User Editable nextcloud Wiki pages of Public Repositories

## Metadata

- HackerOne Report ID: 498878
- Weakness: 
- Program: nextcloud
- Disclosed At: 2019-08-31T12:32:06.581Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

###Summary :
I have found that the "Edit" Permissions of WIKI pages are NOT disabled on the public repositories of nextcloud. Generally Edit permissions are given only to the collaborators of a specific repository. but that is not the case with Nextcloud, It is public editable which isn't right in terms of security. 

An attacker can create a new Wiki page for this particular nextcloud Github Wiki page : There is no restriction on it.


https://github.com/nextcloud/logreader/wiki

An attacker could include any content/links and direct users to other similar nextcloud pages to steal user information. 
Attacker could even provide false information about the user to provide their private keys or passwords using a form/page.

## Impact

These wikis should not be publicly editable due to the possibility of abuse through hacktivities such as Phishing, Defacement, etc

Many companies (even on hackerone) are correcting this issue and removing the "Edit" Permissions to the wiki page of public repositories.

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
