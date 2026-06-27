---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '678727'
original_report_id: '678727'
title: potential RCE and XSS via file upload requiring user account and default settings
weakness: Code Injection
team_handle: nextcloud
created_at: '2019-08-21T19:18:14.807Z'
disclosed_at: '2020-04-01T08:50:37.020Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- code-injection
---

# potential RCE and XSS via file upload requiring user account and default settings

## Metadata

- HackerOne Report ID: 678727
- Weakness: Code Injection
- Program: nextcloud
- Disclosed At: 2020-04-01T08:50:37.020Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

#potential RCE and XSS via file upload requiring user account and default settings

##Requirements
1. User account that can upload files (NO admin)
2. User account name on creation (usually the same as on creation/displayed name)
3. data directory inside of nextcloud server folder (suggested by /var/www/nextcloud/config/config.sample.php)

##Tested on
current release
Version 16.0.4.1
stable
Build: '2019-08-14T18:57:27+00:00 a1a245e88202d834f08f4c2e4451dcbe9baee3aa'

##Basic idea
On nextcloud php files can be uploaded, but when clicked they are only shown in a text editor. If the URL to our skript is known, we get code execution. 
A RCE will work if the server has set it's data directory inside the nextcloud server folder and the username is known. 

##config example
The following is located in /var/www/nextcloud/config/config.sample.php:
[https://github.com/nextcloud/server/blob/master/config/config.sample.php]
~~~~
 *
 * Default to ``data/`` in the Nextcloud directory.
 */
'datadirectory' => '/var/www/nextcloud/data',
~~~~
If this config is used, RCE is possible.

##Attack scenario: 
Short video attached.
(To reproduce use a nextcloud instance and setup a user named attacker. Use any php script called shell.php, and set the datadirectory to /var/www/nextcloud/data)

1. Login to obtained user account (assume his name is "attacker")
2. upload malicious php script. (assume it is called "shell.php")
3. navigate to https://www.ournextclouddomain.com/data/attacker/files/shell.php
4. see some shells poppin

This is possible since we know the direct path to our php script.

Note: This can also be used for XSS since we can upload any html file!

##Prevention
1. user accounts could extend a seed on their foldername like attacker-19320143158015
2. usage of a custom seed inside the data directory.
3. different config than on the example

## Impact

RCE, extract ser data or modify config file (if no special permissions are set), take over the server, also XSS is possible

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
