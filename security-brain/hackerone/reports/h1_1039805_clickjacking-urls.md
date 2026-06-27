---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1039805'
original_report_id: '1039805'
title: Clickjacking URLS
team_handle: nextcloud
created_at: '2020-11-20T18:52:08.212Z'
disclosed_at: '2021-03-10T09:46:30.679Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
asset_identifier: pushfeed.nextcloud.com
asset_type: URL
max_severity: low
tags:
- hackerone
---

# Clickjacking URLS

## Metadata

- HackerOne Report ID: 1039805
- Weakness: 
- Program: nextcloud
- Disclosed At: 2021-03-10T09:46:30.679Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey Team
While performing security testing of your websites i have found the vulnerability called Clickjacking.
Many URLS are in scope and vulnerable to Clickjacking.


The server didn't return an X-Frame-Options header which means that this website could be at risk of a clickjacking attack. The X-Frame-Options HTTP response header can be used to indicate whether or not a browser should be allowed to render a page in a <frame> or <iframe>. Sites can use this to avoid clickjacking attacks, by ensuring that their content is not embedded into other sites.
This vulnerability affects Web Server.



##Steps to Reproduce

Vulnerable Urls:
 1.https://nextcloud.com
 2.https://download.nextcloud.com
 3.https://help.nextcloud.com
 4.https://apps.nextcloud.com/
 5.https://docs.nextcloud.com
 6.https://crm.nextcloud.com
 7.https://support.nextcloud.com
 8.https://scan.nextcloud.com/
 9.https://lists.nextcloud.com
10.https://portal.nextcloud.com
11.https://auth.nextcloud.com
12.https://pushfeed.nextcloud.com
13.https://newsletter.nextcloud.com



URL one by one into iframe src value  ..
this is the HTML code

<html>
<style>
   iframe {
       position:relative;
       width:500px;
       height:700px;
       opacity:0.0001;
       z-index:2;
   }
   div {
       position:absolute;
       top:500px;
       left:550px;
       z-index:1;
   }
</style>
<iframe src="url"></iframe>
</html>


The Site Is Fully Loaded

## Impact

This  technique, keystrokes can also be hijacked. With a carefully crafted combination of stylesheets, iframes, and text boxes, a user can be led to believe they are typing in the password to their email  account, but are instead typing into an invisible frame controlled by the attacker.

I attached a Screenshots
thank you

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
