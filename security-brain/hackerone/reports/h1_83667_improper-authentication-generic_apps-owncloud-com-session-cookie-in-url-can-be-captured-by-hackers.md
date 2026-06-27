---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '83667'
original_report_id: '83667'
title: 'apps.owncloud.com: Session Cookie in URL can be captured by hackers'
weakness: Improper Authentication - Generic
team_handle: owncloud
created_at: '2015-08-20T14:42:06.693Z'
disclosed_at: '2015-10-31T11:38:18.102Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# apps.owncloud.com: Session Cookie in URL can be captured by hackers

## Metadata

- HackerOne Report ID: 83667
- Weakness: Improper Authentication - Generic
- Program: owncloud
- Disclosed At: 2015-10-31T11:38:18.102Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Session Cookie in URL
URL: https://apps.owncloud.com/stories/feed+rss
  
Issue detail
The URL in the request appears to contain a PHP Session token within the query string:

https://apps.owncloud.com/stories/feed+rss?id=42590&PHPSESSID=ee0624300266683a4625aabea344212a
  

Issue background
Sensitive information within URLs may be logged in various locations, including the user's browser, the web server, and any forward or reverse proxy servers between the two endpoints. URLs may also be displayed on-screen, bookmarked or emailed around by users. **They may be disclosed to third parties via the Referer header when any off-site links are followed**. Placing session tokens into the URL increases the risk that they will be captured by an attacker.  

Issue remediation
Applications should use an alternative mechanism for transmitting session tokens, such as HTTP cookies or hidden fields in forms that are submitted using the POST method.  


Note: In your webpage, all `<a href=` contain PHPSESSID URL Parameter, which further increases this risk.

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
