---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '686805'
original_report_id: '686805'
title: .git file accessible
weakness: Information Disclosure
team_handle: makerdao_bbp
created_at: '2019-09-03T11:15:22.234Z'
disclosed_at: '2019-09-13T14:56:45.003Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 20
asset_identifier: blog.makerdao.com
asset_type: URL
max_severity: none
tags:
- hackerone
- information-disclosure
---

# .git file accessible

## Metadata

- HackerOne Report ID: 686805
- Weakness: Information Disclosure
- Program: makerdao_bbp
- Disclosed At: 2019-09-13T14:56:45.003Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,
Your .git file accessible. Thats information disclosure.
URL: https://blog.makerdao.com/wp-content/themes/makerDAO/.git/config

REQUEST:
GET /wp-content/themes/makerDAO/.git/config HTTP/1.1
Host: blog.makerdao.com
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: en-us,en;q=0.5
Cache-Control: no-cache
Cookie: __cfduid=dc0c2f50dd600bfac5f4cb2fee9380e181567508867; wordpress_test_cookie=WP+Cookie+check; pll_language=en
Referer: https://blog.makerdao.com/wp-content/themes/makerDAO/.git/config
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36

REGARDS.

## Impact

GIT repository files can disclose GIT repository usernames and file lists. While disclosures of this type do not provide direct attack vectors, they can be useful for an attacker when combined with other vulnerabilities discovered within the application.

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
