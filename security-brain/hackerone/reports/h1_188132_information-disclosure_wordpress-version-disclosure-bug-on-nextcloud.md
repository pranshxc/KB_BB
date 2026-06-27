---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '188132'
original_report_id: '188132'
title: Wordpress Version Disclosure Bug On Nextcloud
weakness: Information Disclosure
team_handle: nextcloud
created_at: '2016-12-04T06:31:39.344Z'
disclosed_at: '2016-12-04T09:03:23.103Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 6
tags:
- hackerone
- information-disclosure
---

# Wordpress Version Disclosure Bug On Nextcloud

## Metadata

- HackerOne Report ID: 188132
- Weakness: Information Disclosure
- Program: nextcloud
- Disclosed At: 2016-12-04T09:03:23.103Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi @nextcloud ,

#Description
Wordpress version disclosure.

#Affected items
https://nextcloud.com/readme.html
https://nextcloud.com/wp-admin/install.php
https://nextcloud.com/wp-login.php

#The impact of this vulnerability
Possible Wordpress Version information disclosure.You are using wordpress 4.6.1 version also you not delete **`https://nextcloud.com/wp-admin/install.php`** if you got any type of database problem in your site attacker try to install it for deface,And to be noted that you not protect your admin panel **`https://nextcloud.com/wp-login.php`** with captcha attacker can easily Bruteforce your admin panel.

#Web references
* http://www.hackingtutorials.org/web-application-hacking/hack-a-wordpress-website-with-wpscan/

#How to fix this vulnerability
1. Just Delete The **readme.html** from **`/`** root path
1. and also delete **install.php** from **`/wp-admin/`**

Please resolved as close if not acceptable.Because this is my first hunting ;) .
**Thanks**

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
