---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '216812'
original_report_id: '216812'
title: Reflected XSS in error pages (NC-SA-2017-008)
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: nextcloud
created_at: '2017-03-28T21:53:11.174Z'
disclosed_at: '2017-05-15T19:54:37.173Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 28
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS in error pages (NC-SA-2017-008)

## Metadata

- HackerOne Report ID: 216812
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: nextcloud
- Disclosed At: 2017-05-15T19:54:37.173Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

I found a HTML injection vulnerability [1] flaw in the Nextcloud (and Owncloud) latest version. Through this vulnerability an attacker could manipulate the website. This vulnerability could affect to the logged users. An attacker could send a malicious link (that contains the manipulated URL) to a legitimate user that he is logged in and simulate the login screen to stole the password (phishing), or multiple attacks more, like XSS.

The Nextcloud/Owncloud application contains multiple security headers of HTTP, so, inject scripts or redirect to another websites is difficult, the problem is that not all the browser supports these headers (fortunatelly, the most used browsers yes).

Exist more options to attack, for example, redirect the content of an <object> or <script> to a saved and shared items of your directory. Also, the mimetypes are well configured and the most browsers will not execute a javascript file that doesn't have the javascript content-type.

Anyway, all the mitigations are well, but these aren't never-falling. So the solution to this vulnerability is sanitize the output before to deliver the HTML to the final user.

Also, another security flaw is showed, but the impact is less, it is a full path disclosure and it show the full path of the Nextcloud/Owncloud installation.

PoC (Proof of Concept):

https://nextcloud-site/index.php/apps/files/ajax/download.php?files=%00&dir=</p>HTMLCODE

I tested it in the last version.

If you need more information, ask to me.

Regards,

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
