---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1430379'
original_report_id: '1430379'
title: Visibility Robots.txt file
weakness: Information Disclosure
team_handle: krisp
created_at: '2022-01-14T19:16:47.518Z'
disclosed_at: '2022-04-25T12:20:46.605Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 18
asset_identifier: krisp.ai
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Visibility Robots.txt file

## Metadata

- HackerOne Report ID: 1430379
- Weakness: Information Disclosure
- Program: krisp
- Disclosed At: 2022-04-25T12:20:46.605Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Issue detail:-
The web server contains a robots.txt file.  
Issue background:-
The file robots.txt is used to give instructions to web robots, such as search engine crawlers, about locations within the web site that robots are allowed, or not allowed, to crawl and index.
The presence of the robots.txt does not in itself present any kind of security vulnerability. However, it is often used to identify restricted or private areas of a site's contents. The information in the file may therefore help an attacker to map out the site's contents, especially if some of the locations identified are not linked from elsewhere in the site. If the application relies on robots.txt to protect access to these areas, and does not enforce proper access control over them, then this presents a serious vulnerability.
Issue remediation:-
The robots.txt file is not itself a security threat, and its correct use can represent good practice for non-security reasons. You should not assume that all web robots will honor the file's instructions. Rather, assume that attackers will pay close attention to any locations identified in the file. Do not rely on robots.txt to provide any kind of protection over unauthorized access.

URL -  https://krisp.ai/robots.txt

User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php

Sitemap: https://krisp.ai/sitemap.xml

Here, /wp-admin/admin-ajax.php  is Allow which gives some private information.

URL -  https://krisp.ai/robots.txt/wp-admin/ 
                view-source:https://krisp.ai/robots.txt/wp-admin/     
These URL is also Accessible which provide some private information.

Sitemap:  https://krisp.ai/sitemap.xml

## Impact

If u have robots.txt file so attacker can see all Your secret pages!

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
