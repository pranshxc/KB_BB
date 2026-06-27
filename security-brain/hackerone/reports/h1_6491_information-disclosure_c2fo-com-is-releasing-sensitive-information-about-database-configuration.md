---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6491'
original_report_id: '6491'
title: c2fo.com is releasing sensitive Information about Database Configuration.
weakness: Information Disclosure
team_handle: c2fo
created_at: '2014-04-08T12:13:36.550Z'
disclosed_at: '2014-05-08T18:29:17.756Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- information-disclosure
---

# c2fo.com is releasing sensitive Information about Database Configuration.

## Metadata

- HackerOne Report ID: 6491
- Weakness: Information Disclosure
- Program: c2fo
- Disclosed At: 2014-05-08T18:29:17.756Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello C2FO Securiity Team,

Vulnerability Details : Disclosure of Database Username and Password of c2fo.com

Description: Your configuration file of your website is available to download from your website c2fo.com.When i thought to pentest your site,i landed on https://c2fo.com .But instead of showing the website it showed 403 Forbidden error.It seemed weird to me ,then i went to the link https://c2fo.com/wp-config.php and the file downloaded to my computer.Then i tried to download .htaccess and wp-login.php and yes they were also available to download.

POC:

I have made proof of concept video of the same :- https://www.youtube.com/watch?v=AXq-YWO_EhI
The above video is unlisted .

Below is some lines from wp-config.php

# Database Configuration
define('DB_NAME','wp_c2fo');
define('DB_USER','c2fo');
define('DB_PASSWORD','*********');
define('DB_HOST','127.0.0.1');
define('DB_HOST_SLAVE','127.0.0.1');
define('DB_CHARSET', 'utf8');
define('DB_COLLATE', 'utf8_unicode_ci');
$table_prefix = 'wp_';

I have included all the files i have downloaded ,in the attachment .

Remedy:- Please change your configuration file as soon as possible because might be some attacker have also downloaded the file and use it for future attack's on c2fo.com

With regard's

Aditya Agrawal

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
