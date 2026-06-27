---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '112955'
original_report_id: '112955'
title: WordPress Failure Notice page will generate arbitrary hyperlinks
team_handle: withinsecurity
created_at: '2016-01-26T21:45:46.762Z'
disclosed_at: '2016-03-25T19:14:36.282Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
---

# WordPress Failure Notice page will generate arbitrary hyperlinks

## Metadata

- HackerOne Report ID: 112955
- Weakness: 
- Program: withinsecurity
- Disclosed At: 2016-03-25T19:14:36.282Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

### Description:
When the "WordPress Failure Notice" page is returned, if the parameter `_wp_http_referer` was supplied with a valid URL, this URL will be used as the "Please try again." link (see attachment). A way to reliably generate this page, is to append `?wpcspReceiveCSPviol=1&_wp_http_referer=example.com` to any page address.

### Impact:
An obvious situation where this could lead to a problem, is if a malicious party is able to force the WordPress Failure Notice page with a parameter pointing to a site he controls. The unsuspecting user would be presented with a seemingly harmless page from a trusted domain, with an innocent looking "Please try again." link, which points to an attacker controlled location.

The severity of this issue is arguably small, however. It would involve some considerable amount of work on the attackers part, to create a situation where this could become a problem. As far as I could tell, the only way to reliably force the "WordPress Failure Notice" page, is to append `?wpcspReceiveCSPviol=1` to an URL.

### Fix:
A fix would be to check that supplied arguments to the `_wp_http_referer` parameter, is restricted to the same domain as the page or to ensure that users aren't able to force Failure pages.

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
