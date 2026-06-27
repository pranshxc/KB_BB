---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '13959'
original_report_id: '13959'
title: privilege escalation
weakness: Improper Authentication - Generic
team_handle: automattic
created_at: '2014-05-29T09:09:04.533Z'
disclosed_at: '2014-08-10T06:00:52.864Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# privilege escalation

## Metadata

- HackerOne Report ID: 13959
- Weakness: Improper Authentication - Generic
- Program: automattic
- Disclosed At: 2014-08-10T06:00:52.864Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This vulnerability includes privileges escalation, authentication bypass, as well as some information disclosure as well. follow the below steps for reproduction.

1. go to https://cloudup.com and make two accounts say X and Y.
2. login with the account X and upload a file(can be txt,php,anything) and set a password for this file, now right click on download and copy the link location of the file. It is something like (https://cloudup.com/files/iDQ23wk5p1O/download)
3. Now logout from account X, and login with account Y. Now load the link location of file copied in step 2. what you will get? Forbidden, right?
4. But wait a second, modify the url mentioned in step 2 like below
 https://cloudup.com/files/iDQ23wk5p1O/   (remove the download part)
5. Load the above modified url, and you will see, you can access the file contents i.e. password protected file (authentication bypass), accessed by another user who is not authorized (privilege escalation) and information disclosure like 
"exif":{"exiftool version number":"9.35","file name":"HiTmbEE-C2","directory":"/tmp/thumbs","file size":"46 kB","file modification date time":"2014:05:29 08:37:22+00:00","file access date time":"2014:05:29 08:37:22+00:00","file inode change date time":"2014:05:29 08:37:22+00:00","file permissions":"rw-rw-r--"

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
