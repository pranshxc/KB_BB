---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1316412'
original_report_id: '1316412'
title: Information Exposure Through Directory Listing
weakness: Information Exposure Through Directory Listing
team_handle: torproject
created_at: '2021-08-23T13:28:51.998Z'
disclosed_at: '2021-08-27T11:15:01.488Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 1
asset_identifier: Tor
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- information-exposure-through-directory-listing
---

# Information Exposure Through Directory Listing

## Metadata

- HackerOne Report ID: 1316412
- Weakness: Information Exposure Through Directory Listing
- Program: torproject
- Disclosed At: 2021-08-27T11:15:01.488Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

##Vulnerability description
The web server is configured to display the list of files contained in this directory. This is not recommended because the directory may contain files that are not normally exposed through links on the web site.

##Link as POC:

https://www.torproject.org/static/
https://www.torproject.org/static/css/
https://www.torproject.org/static/findoc/
https://www.torproject.org/static/fonts/
https://www.torproject.org/static/js/
https://www.torproject.org/static/images/
https://www.torproject.org/static/keys/

For obvious reasons, I can not check whether this service is in scope, thats why i haven't searched for any critical informations and haven't check tokens and other stuff
Please let me know if you need some extra information.
Sorry for out of scope report, i thought it could be informative for you!
Thanks in advance!

## Impact

Exposing the contents of a directory can lead to an attacker gaining access to source code or providing useful information for the attacker to devise exploits, such as creation times of files or any information that may be encoded in file names. The directory listing may also compromise private or confidential data.

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
