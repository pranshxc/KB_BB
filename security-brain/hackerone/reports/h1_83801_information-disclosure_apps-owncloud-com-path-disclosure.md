---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '83801'
original_report_id: '83801'
title: 'apps.owncloud.com: Path Disclosure'
weakness: Information Disclosure
team_handle: owncloud
created_at: '2015-08-21T02:58:12.153Z'
disclosed_at: '2015-09-11T09:36:58.675Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# apps.owncloud.com: Path Disclosure

## Metadata

- HackerOne Report ID: 83801
- Weakness: Information Disclosure
- Program: owncloud
- Disclosed At: 2015-09-11T09:36:58.675Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Threat:
A potentially sensitive file, directory, or directory listing was discovered on the Web server.

Impact:
The contents of this file or directory may disclose sensitive information.

Solution:
Verify that access to this file or directory is permitted. If necessary, remove it or apply access controls to it.

URL: https://apps.owncloud.com/CONTENT/user-pics/0/.svn/entries

Extracted Info:

1. committed-date="2006-06-26T14:30:45.256007Z"
2. url="file:///var/svn/repos/kde-look/trunk/usermanager/pics/0"
3. last-author="root"
4. kind="dir"
5. uuid="02c33d69-2117-0410-82eb-df9ca47e2d51" 
6. repos="file:///var/svn/repos/kde-look"

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
