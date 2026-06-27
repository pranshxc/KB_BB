---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1794757'
original_report_id: '1794757'
title: Reflective Cross Site Scripting (XSS) on ███████/Pages
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2022-12-06T10:42:15.678Z'
disclosed_at: '2024-03-22T17:32:41.589Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflective Cross Site Scripting (XSS) on ███████/Pages

## Metadata

- HackerOne Report ID: 1794757
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2024-03-22T17:32:41.589Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Reflective Cross-Site Scripting (XSS)
An elevation of privilege vulnerability exists when Microsoft SharePoint Server does not properly sanitize a specially crafted web request to an affected SharePoint server. An authenticated attacker could exploit the vulnerability by sending a specially crafted request to an affected SharePoint server. 
The attacker to read content that the attacker is not authorized to read, use the victim's identity to take actions on the SharePoint site on behalf of the user, such as change permissions and delete content, and inject malicious content in the browser of the user.

## System Host(s)
https://██████████/Pages

## Affected URLs in Scope
https://█████████/Pages/default.aspx?FollowSite=0&SiteName=%27-confirm(%27XSSALERT%27)-%27

## Affected Product(s) and Version(s)
Microsoft SharePoint Foundation 2013 Service Pack 1

██████ 

References
https://msrc.microsoft.com/update-guide/vulnerability/CVE-2017-0255

## CVE Numbers
CVE-2017-0255

## Steps to Reproduce

Injecting this XSS payload containing allows a window to pop up as a result of the payload being executed.

 1. Go to- 
https://████████/Pages/default.aspx?FollowSite=0&SiteName=%27-confirm(%27XSSALERT%27)-%27


## Suggested Mitigation/Remediation Actions
Sanitize data input (to make sure the URL input does not contain any code) is loaded from well-defined endpoints.

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
