---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '269705'
original_report_id: '269705'
title: WordPress < 4.8.2 vulnerable to multiple attacks
weakness: Violation of Secure Design Principles
team_handle: nextcloud
created_at: '2017-09-19T23:46:55.369Z'
disclosed_at: '2017-09-27T05:21:06.580Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# WordPress < 4.8.2 vulnerable to multiple attacks

## Metadata

- HackerOne Report ID: 269705
- Weakness: Violation of Secure Design Principles
- Program: nextcloud
- Disclosed At: 2017-09-27T05:21:06.580Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello team,

__Summary:__

I observed that your website `https://nextcloud.com` still uses WP less than `4.8.2` which is vulnerable to multiple attacks, i reported it so that the team will be aware of it, below are the new discovered bug that you can find on this release: https://wordpress.org/news/2017/09/wordpress-4-8-2-security-and-maintenance-release/

  1. $wpdb->prepare() can create unexpected and unsafe queries leading to potential SQL injection (SQLi). WordPress core is not directly vulnerable to this issue, but we’ve added hardening to prevent plugins and themes from accidentally causing a vulnerability. Reported by Slavco
  2. A cross-site scripting (XSS) vulnerability was discovered in the oEmbed discovery. Reported by xknown of the WordPress Security Team.
  3. A cross-site scripting (XSS) vulnerability was discovered in the visual editor. Reported by Rodolfo Assis (@brutelogic) of Sucuri Security.
  4. A path traversal vulnerability was discovered in the file unzipping code. Reported by Alex Chapman (noxrnet).
  5. A cross-site scripting (XSS) vulnerability was discovered in the plugin editor. Reported by 陈瑞琦 (Chen Ruiqi).
  6. An open redirect was discovered on the user and term edit screens. Reported by Yasin Soliman (ysx).
  7. A path traversal vulnerability was discovered in the customizer. Reported by Weston Ruter of the WordPress Security Team.
  8. A cross-site scripting (XSS) vulnerability was discovered in template names. Reported by Luka (siKiritokic).
  9. A cross-site scripting (XSS) vulnerability was discovered in the link modal. Reported by Anas Roubi (qasuar).

__Mitigation:__

Upgrade to wordpress 4.8.2

Regards
Chachi

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
