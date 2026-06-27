---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '152591'
original_report_id: '152591'
title: Stored XSS on invoice, executing on any subdomain
weakness: Cross-site Scripting (XSS) - Generic
team_handle: harvest
created_at: '2016-07-20T16:16:19.688Z'
disclosed_at: '2016-09-10T22:00:18.072Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS on invoice, executing on any subdomain

## Metadata

- HackerOne Report ID: 152591
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: harvest
- Disclosed At: 2016-09-10T22:00:18.072Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Summary
-----------

There is a stored XSS vulnerability, which can execute on any subdomain as the vulnerability lies in an invoice. You are filtering HTML and js, but you neglect to filter out Flash objects, which can execute javascript.

Steps to reproduce
-------------

1. Create an invoice and add a flash file which executes javascript as an attachment. 

    You can use F106128, it is from this site: https://soroush.secproject.com/blog/2012/11/xss-by-uploadingincluding-a-swf-file/ . It will execute whatever javascript you provide in the `js` parameter.

2. Now share the link to your report and the XSS will execute. You can use any subdomain you like. Here are some examples which will execute `alert(document.domain)`:

    https://asdf.harvestapp.com/attachments/171020?client_key=a143393e99114b677ce6450cf9861c3bde60f817&js=alert%28document.domain%29

    https://abcdefghijklmnopqrstuvwxyz.harvestapp.com/attachments/171020?client_key=a143393e99114b677ce6450cf9861c3bde60f817&js=alert%28document.domain%29

Impact
--------------

This is a stored XSS effecting all applications/subdomains on harvest. Notice that of course you can create a flash file which directly executes a payload, without the need for the `js` parameter like in my proof of concept.

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
