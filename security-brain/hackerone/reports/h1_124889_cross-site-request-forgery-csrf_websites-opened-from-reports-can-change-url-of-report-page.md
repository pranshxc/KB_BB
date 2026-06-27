---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '124889'
original_report_id: '124889'
title: Websites opened from reports can change url of report page
weakness: Cross-Site Request Forgery (CSRF)
team_handle: security
created_at: '2016-03-21T23:47:18.780Z'
disclosed_at: '2016-04-21T11:00:26.198Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Websites opened from reports can change url of report page

## Metadata

- HackerOne Report ID: 124889
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: security
- Disclosed At: 2016-04-21T11:00:26.198Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Websites opened from the a hackerone report can change the url of the report page. For example, clicking on a link set to "http://d214mfsab.org/same.html" (including this one) will change the still-open report page to http://example.com. This works on current versions of Safari (including mobile) and possibly other browsers.

This vulnerability can lead to phishing attacks, where the user changes the url of the report page to a similar-looking page. Users would trust the tab with the report open to remain the same, and would be unsuspecting.

This is due to mishandling of the 'target="_blank"' option.

To reproduce:

1. In any html page (does not need to be the same origin), add the javascript "opener.location = 'http://example.com'". For this, I created http://d214mfsab.org/same.html
2. Add this url to a hackerone report.
3. When a user clicks on this url, the original report page's url will be changed to a potentially malicious url.

A malicious user could modify the report page to an extremely similar page, which a user would be unlikely to notice. An attacker could duplicate the entire report page, and present a login form, which would steal the user's password.

Although the user is warned about following links, this is not sufficient protection, as hackerone should ensure that pages cannot modify the report url.

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
