---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '156182'
original_report_id: '156182'
title: Visibility  Robots.txt file
weakness: Information Disclosure
team_handle: zomato
created_at: '2016-08-02T22:35:56.808Z'
disclosed_at: '2017-05-18T16:54:51.496Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 10
tags:
- hackerone
- information-disclosure
---

# Visibility  Robots.txt file

## Metadata

- HackerOne Report ID: 156182
- Weakness: Information Disclosure
- Program: zomato
- Disclosed At: 2017-05-18T16:54:51.496Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Issue detail:-
The web server contains a robots.txt file.  

Issue background:-
The file robots.txt is used to give instructions to web robots, such as search engine crawlers, about locations within the web site that robots are allowed, or not allowed, to crawl and index.
The presence of the robots.txt does not in itself present any kind of security vulnerability. However, it is often used to identify restricted or private areas of a site's contents. The information in the file may therefore help an attacker to map out the site's contents, especially if some of the locations identified are not linked from elsewhere in the site. If the application relies on robots.txt to protect access to these areas, and does not enforce proper access control over them, then this presents a serious vulnerability.

Issue remediation:-
The robots.txt file is not itself a security threat, and its correct use can represent good practice for non-security reasons. You should not assume that all web robots will honor the file's instructions. Rather, assume that attackers will pay close attention to any locations identified in the file. Do not rely on robots.txt to provide any kind of protection over unauthorized access.

URL:- https://www.zomato.com/robots.txt

User-agent: Googlebot
Disallow: /admin/
Disallow: /clients/
Disallow: /acd/
Disallow: /voicephp/
Disallow: /downloads/
Disallow: /nonsvn/
Disallow: /zast
Allow: /

If u have robots.txt file so attacker can see all Your secret pages!
like www.example.com/admin....


Sitemap:- https://www.zomato.com/sitemap_seznam.xml.gz

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
