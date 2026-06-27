---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '202918'
original_report_id: '202918'
title: yaman.olx.ph/wordpress is using a very vulnerable version of WordPress and
  contains directory listing
weakness: Cross-Site Request Forgery (CSRF)
team_handle: olx
created_at: '2017-02-02T15:27:34.172Z'
disclosed_at: '2017-04-06T07:47:24.510Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# yaman.olx.ph/wordpress is using a very vulnerable version of WordPress and contains directory listing

## Metadata

- HackerOne Report ID: 202918
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: olx
- Disclosed At: 2017-04-06T07:47:24.510Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

__Hello ,__
I want to report that your website is using a vulnerable version of WordPress which is 4.7 (Released on 2016-12-06) . This Can be identified from the read me file located [here](https://yaman.olx.ph/wordpress/readme.html) , and that your website contains directory listing of the web-includes located  [here](https://yaman.olx.ph/wordpress/wp-includes/)ز
# Bugs in this WordPress version
__[!] Potential Remote Command Execution (RCE) in PHPMailer__
    Reference: https://wpvulndb.com/vulnerabilities/8714
[i] Fixed in: 4.7.1

__[!] User Information Disclosure via REST API__
    Reference: https://wpvulndb.com/vulnerabilities/8715
[i] Fixed in: 4.7.1

__[!] Authenticated Cross-Site scripting (XSS) in update-core.php__
    Reference: https://wpvulndb.com/vulnerabilities/8716
[i] Fixed in: 4.7.1

__[!] Cross-Site Request Forgery (CSRF) via Flash Upload__
    Reference: https://wpvulndb.com/vulnerabilities/8717
[i] Fixed in: 4.7.1

__[!] Stored Cross-Site Scripting (XSS) via Theme Name fallback__
    Reference: https://wpvulndb.com/vulnerabilities/8718
[i] Fixed in: 4.7.1

__[!] Post via Email Checks mail.example.com by Default__
    Reference: https://wpvulndb.com/vulnerabilities/8719
[i] Fixed in: 4.7.1

__[!] Accessibility Mode Cross-Site Request Forgery (CSRF)__
    Reference: https://wpvulndb.com/vulnerabilities/8720
[i] Fixed in: 4.7.1

__[!] Cryptographically Weak Pseudo-Random Number Generator (PRNG)__
    Reference: https://wpvulndb.com/vulnerabilities/8721
[i] Fixed in: 4.7.1

__[!] Press This UI Available to Unauthorised Users__
    Reference: https://wpvulndb.com/vulnerabilities/8729
[i] Fixed in: 4.7.2

__[!] WP_Query SQL Injection__
    Reference: https://wpvulndb.com/vulnerabilities/8730
[i] Fixed in: 4.7.2

__[!] Cross-Site Scripting (XSS) in posts list table__
    Reference: https://wpvulndb.com/vulnerabilities/8731
[i] Fixed in: 4.7.2

__[!] Unauthenticated Page/Post Content Modification via REST API__
    Reference: https://wpvulndb.com/vulnerabilities/8734
    Reference: https://blog.sucuri.net/2017/02/content-injection-vulnerability-wordpress-rest-api.html
[i] Fixed in: 4.7.2

# Fix
Updating your blog to the latest version which is 4.7.2 as i believe 

__Thanks ,
Mohamed Sherif__

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
