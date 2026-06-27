---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '236607'
original_report_id: '236607'
title: Remote Code Execution in the Import Channel function
team_handle: expressionengine
created_at: '2017-06-05T15:17:34.888Z'
disclosed_at: '2018-04-04T16:36:38.276Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
---

# Remote Code Execution in the Import Channel function

## Metadata

- HackerOne Report ID: 236607
- Weakness: 
- Program: expressionengine
- Disclosed At: 2018-04-04T16:36:38.276Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

Administrators are allow to import channels by visiting http://HOST/PATH_TO_EE/admin.php?/cp/channels/sets and uploading .zip archives that contain the information about the channels to be imported. The archives are then extracted into temporary directories, which are kept in the `/system/user/cache/cset/` directory. The problem is that, if the archive doesn't have all the required files for the import to be successful, the extracted files remain in their folders and an error is thrown to the administrator stating that a file doesn't exist in the archive.

This allows an administrator to upload .php scripts to the server, which is not allowed by default in ExpressionEngine as far as I can see.

###Steps to reproduce:
1- Download the attached .zip archive and browse to http://HOST/PATH_TO_EE/admin.php?/cp/channels/sets
2- Try to upload the zip file you just downloaded as the imported channel
3- Navigate to http://HOST/PATH_TO_EE/system/user/cache/cset/, which will show a directory listing of all the temporary directories, this is a problem by itself
4- If this is your first time trying this, you should find a single directory, click the directory's name and then click the test.php file and edit the URL in the address bar by adding "?cmd=whoami" to the URL
5- Notice that the command has executed and that the information is returned in the page

Regards,

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
