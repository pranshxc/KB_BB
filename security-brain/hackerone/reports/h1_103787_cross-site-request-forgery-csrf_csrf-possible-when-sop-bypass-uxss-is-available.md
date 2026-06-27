---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '103787'
original_report_id: '103787'
title: CSRF possible when SOP Bypass/UXSS is available
weakness: Cross-Site Request Forgery (CSRF)
team_handle: security
created_at: '2015-12-06T12:56:10.665Z'
disclosed_at: '2015-12-30T15:23:41.230Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF possible when SOP Bypass/UXSS is available

## Metadata

- HackerOne Report ID: 103787
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: security
- Disclosed At: 2015-12-30T15:23:41.230Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Description**
If an attacker could extract content from https://hackerone.com, they could perform CSRF attacks due to the fact that:
1. Some pages prints the token in the HTML response (edit user form at https://hackerone.com/settings/profile/edit)
2. Tokens aren't bound per action
3. PATCH/DELETE can be sent via _method

Attacker being allowed to read content but not execute JS could happen if:
1. SOP Bypass in plugin (http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-3115)
2. SOP Bypass in application design (https://miki.it/blog/2014/7/8/abusing-jsonp-with-rosetta-flash/)
3. UXSS (https://blog.innerht.ml/ie-uxss/)

Currently, some mitigations are in place. _method isn't allowed in GET and the Origin header is checked. This isn't enough since FireFox and IE doesn't send Origin header when submitting forms.

**Attack scenario**
The most recent (to my knowledge) SOP bypass was the re-implementation of the IE UXSS bug (https://blog.innerht.ml/ie-uxss/). This was working November 28th 2015. However, the bug required framing at least one resource, and HackerOne sends X-Frame-Options on all resources. Sadly, HackerOne uses CloudFlare so the URL https://hackerone.com/cdn-cgi/trace could be used (doesn't send X-Frame-Options).

So to sum up:
1. Logged in user visits attackers page in IE (vulnerable to UXSS)
2. UXSS runs script on framed "https://hackerone.com/cdn-cgi/trace" to extract CSRF token on https://hackerone.com/settings/profile/edit (via AJAX)
3. User is attacked with the extracted CSRF token

**Fix**
This could be mitigated by storing the token in JavaScript and adding the token to the form after the page is loaded.

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
