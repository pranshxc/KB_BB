---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '118024'
original_report_id: '118024'
title: Markdown based stored XSS (IE only)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: gitlab
created_at: '2016-02-22T19:58:40.720Z'
disclosed_at: '2017-05-03T22:28:08.622Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Markdown based stored XSS (IE only)

## Metadata

- HackerOne Report ID: 118024
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: gitlab
- Disclosed At: 2017-05-03T22:28:08.622Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

My other report #116697 deals with any browser even through its not a direct XSS as it doesn't execute in the context of the site. But here is another type of XSS using `vbscript:` which affects only IE users but executes on the context of the site (check the screenshot for POC alert(document.domain)).

### POC:

`[clickme](vbscript:alert(document.domain))`

`vbscript:` is not supported in Microsoft EDGE and updated versions of IE 11 (as per [this link](http://stackoverflow.com/questions/17483782/vbscript-support-in-internet-explorer-11) but it do works if people are working in the compatibility mode (I have read the gitlab instruction which specifically says users to turm off compatibility mode but if IE detects that the incoming webpages has some contents which is supported only on compatibility mode, it recommends that to the users I guess.).

For example, I comment the above link on one of the project/issues and then when I reloaded the page, IE detects that the incoming webpage contains scripts that might not be compatible and hence it told me to enable compatibility options by clicking a button. Usually if people see a warning like that from a browser, they will tend to enable it.

### Mitigation

Other then updated versions of IE 11, it works on IE10, 9, 8, 7. Also fixing this issue is so trivial by just blocking the keyword `vbscript` and since it executes on the context of the site, I believe this should be fixed.

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
