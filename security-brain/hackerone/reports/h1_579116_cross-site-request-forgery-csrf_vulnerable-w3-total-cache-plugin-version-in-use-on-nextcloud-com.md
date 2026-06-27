---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '579116'
original_report_id: '579116'
title: Vulnerable W3 Total Cache plugin version in use on nextcloud.com
weakness: Cross-Site Request Forgery (CSRF)
team_handle: nextcloud
created_at: '2019-05-13T15:02:55.043Z'
disclosed_at: '2019-06-21T09:10:01.856Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 5
asset_identifier: nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Vulnerable W3 Total Cache plugin version in use on nextcloud.com

## Metadata

- HackerOne Report ID: 579116
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: nextcloud
- Disclosed At: 2019-06-21T09:10:01.856Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi there,

I noticed you are currently using a vulnerable version of W3 Total Cache, as the changelog containing the plugin version is publicly reachable: https://nextcloud.com/wp-content/plugins/w3-total-cache/changelog.txt

W3 Total Cache makes the site vulnerable to a series of attacks, including XSS, CSRF and SSRF.

Some references:

https://wpvulndb.com/vulnerabilities/8629
https://wpvulndb.com/vulnerabilities/9269
https://secupress.me/blog/4-new-security-flaws-w3-total-cache-0-9-4-1/

### Mitigation

Update the plugin to the last version (or manually patch the vulnerabilities).

On a separate note, I saw this domain is not eligible for bounty :) But wanted to bring this to your attention the same, being WordPress a common target.

Furthermore, this specific vulnerability could lead to a full website defacement: https://blog.mazinahmed.net/2014/12/w3-total-caches-w3totalfail.html

Best Regards,
Francesco

## Impact

Being the vulnerabilities easy to detect with an external scan, hackers could take advantage of, and use the website to run various malicious activities.

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
