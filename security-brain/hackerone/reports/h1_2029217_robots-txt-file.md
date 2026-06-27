---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2029217'
original_report_id: '2029217'
title: robots.txt file
team_handle: teleport
created_at: '2023-06-16T16:02:06.658Z'
disclosed_at: '2023-07-17T17:57:47.910Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 11
asset_identifier: '*.goteleport.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# robots.txt file

## Metadata

- HackerOne Report ID: 2029217
- Weakness: 
- Program: teleport
- Disclosed At: 2023-07-17T17:57:47.910Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

The web server includes a robots.txt file that serves a crucial role in providing instructions to web robots, such as search engine crawlers, about the permissible areas of the website that they can crawl and index. While the presence of this file does not pose a direct threat to the security of the website, it is often used to identify restricted or private areas of the site's contents, which could be exploited by attackers to map out the site's contents. This is especially true if some of the locations identified are not linked from elsewhere on the site. It is important to note that if the application relies on robots.txt to secure access to these areas, and does not enforce proper access control over them, then this could lead to a serious vulnerability.
To ensure the security of the website, it is crucial to use the robots.txt file correctly and not assume that all web robots will honor the file's instructions. Instead, take the attacker will pay close attention to any locations identified in the file. It is recommended not to rely on robots.txt to provide any kind of protection over unauthorized access. As a helpful assistant, I urge you to take the necessary measures to secure your website and prevent unauthorized access.

URL:  https://goteleport.com/robots.txt

User-agent: *
Disallow: /teleport.sh/
Disallow: /teleconsole/
Disallow: /gravity/
Disallow: /teleport/docs/ver/
Disallow: /teleport/docs/1.3/
Disallow: /teleport/docs/2.0/
Disallow: /teleport/docs/2.3/
Disallow: /teleport/docs/2.4/
Disallow: /categories/
Disallow: /_shared/
Disallow: /docs/ver/
Disallow: /sandbox/
Disallow: /404/
Disallow: /blog/404/
Disallow: /docs/404/
# Algolia-Crawler-Verif: 7547941F377A04CB

## Impact

from the robots.txt file attacker can see all Your secret pages!

like www.example.com/_shared....
Sitemap: https://goteleport.com/sitemapindex.xml

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
