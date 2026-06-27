---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '250273'
original_report_id: '250273'
title: Image lib - unescaped file path
weakness: Code Injection
team_handle: expressionengine
created_at: '2017-07-16T11:58:19.284Z'
disclosed_at: '2017-09-07T14:56:44.018Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- code-injection
---

# Image lib - unescaped file path

## Metadata

- HackerOne Report ID: 250273
- Weakness: Code Injection
- Program: expressionengine
- Disclosed At: 2017-09-07T14:56:44.018Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Under `./system/ee/legacy/libraries/Image_lib.php`

There are function from CodeIgniter to manipulate images. The issue is that the PHP function `exec` is used two times in two different functions: `image_process_imagemagick` and `image_process_netpbm`

In both cases the `full_src_path` and `full_dst_path` are given unescaped to the `exec` function. If an attacker can control the filename of the image to give he can inject pretty much arbitrary code. I suggest to use `escapeshellarg` on the path arguments at rows:
-590
-604
-608
-691

Furthermore, note that in CodeIgniter Github repo, the function `image_process_imagemagick` that already prevents this potential injection.
https://github.com/bcit-ci/CodeIgniter/blob/27647c9a8b5cd5a0e1fd78123316f359fe61a672/system/libraries/Image_lib.php#L892

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
