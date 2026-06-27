---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6853'
original_report_id: '6853'
title: XSS on [/concrete/concrete/elements/dashboard/sitemap.php]
weakness: Cross-site Scripting (XSS) - Generic
team_handle: concretecms
created_at: '2014-04-10T19:30:42.072Z'
disclosed_at: '2014-08-28T22:40:56.160Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS on [/concrete/concrete/elements/dashboard/sitemap.php]

## Metadata

- HackerOne Report ID: 6853
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: concretecms
- Disclosed At: 2014-08-28T22:40:56.160Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Alright, here's the other bug I said I would report. I have found the file that is affected by this bug, which is outlined in the title. The affected file is here - /concrete/concrete/elements/dashboard/sitemap.php

On line 40, this section:

<div id="tree" sitemap-wrapper="1" sitemap-select-callback="<?php echo $callback?>"

PHP echoes the $callback without filtering any user input. Here is the PoC link - 

http://localhost/concrete/index.php/tools/required/pages/search_dialog?sitemap_select_mode=%22%3E%3Cscript%3Ealert%280%29%3C/script%3E

Change localhost/ to wherever you're hosting your concrete installation.

That might not be the source of the problem, but I used grep to find the place where it was echoed.

Thank you.

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
