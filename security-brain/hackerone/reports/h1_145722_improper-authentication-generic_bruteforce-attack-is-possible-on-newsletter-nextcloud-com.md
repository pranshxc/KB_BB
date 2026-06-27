---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145722'
original_report_id: '145722'
title: Bruteforce attack is possible on newsletter.nextcloud.com
weakness: Improper Authentication - Generic
team_handle: nextcloud
created_at: '2016-06-18T17:04:44.789Z'
disclosed_at: '2016-06-19T13:42:28.140Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# Bruteforce attack is possible on newsletter.nextcloud.com

## Metadata

- HackerOne Report ID: 145722
- Weakness: Improper Authentication - Generic
- Program: nextcloud
- Disclosed At: 2016-06-19T13:42:28.140Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Since HTTP Basic authentication is used on [https://newsletter.nextcloud.com], This type of authentication is vulnerable to Bruteforce attack.

 *refer the attachment below*
{F100241}       

*refer the attachment below*
{F100240}        

**Attacking via metasploit auxilary scanner http_login:**

*refer the attachment below*
{F100239}   

An attacker can bruteforce the following directories on {https://newsletter.nextcloud.com}

>1) [https://newsletter.nextcloud.com/admin/]
>2) [https://newsletter.nextcloud.com/admin/pma/]
>3) [https://newsletter.nextcloud.com/admin/phpmyadmin/]
>4) [https://newsletter.nextcloud.com/admin/mysql]

>The website also reveals that **PHP list** *version 3.2.5* is used 
 
*refer the attachment below*
{F100238}   

An attacker can take advantage of this and can exploit the framework related vulnerability.

>Recently **PHP list** *version 3.2.5* was vulnerable to XSS and CSRF 
* {https://packetstormsecurity.com/files/137278/PHPList-3.2.4-Cross-Site-Request-Forgery-Cross-Site-Scripting.html}
* {https://www.youtube.com/watch?v=cU6ob4sCKgs}

So it is a good practice to use the latest stable version and dont reveal the banner in the error messages.

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
