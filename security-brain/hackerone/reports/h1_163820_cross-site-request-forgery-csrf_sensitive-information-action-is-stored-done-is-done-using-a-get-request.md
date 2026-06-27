---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '163820'
original_report_id: '163820'
title: Sensitive information/action is stored/done is done using a GET request
weakness: Cross-Site Request Forgery (CSRF)
team_handle: khanacademy
created_at: '2016-08-27T14:22:15.682Z'
disclosed_at: '2019-06-23T09:11:49.022Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 19
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Sensitive information/action is stored/done is done using a GET request

## Metadata

- HackerOne Report ID: 163820
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: khanacademy
- Disclosed At: 2019-06-23T09:11:49.022Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

###Description:
The action **to remove an email from account** is done using a GET request and it has **security token**.

The URL is : `https://www.khanacademy.org/settings/unlinkaccount?email=█████&fkey=<security token here>`

It is never a good practice to have sensitive information in URL. Following are the reasons:
+ GET requests can be cached
+ GET requests remain in the browser history
+ GET requests can be bookmarked

Whereas:
+ POST requests are never cached
+ POST requests do not remain in the browser history
+ POST requests cannot be bookmarked

###Attack Scenario:
If the URL goes in the hands of malicious user then host a malicious website and perform a CSRF attack against the victim and this un-link that email address.

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
