---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '716570'
original_report_id: '716570'
title: Stored XSS (Hexo-admin plugin)
weakness: Cross-site Scripting (XSS) - Stored
team_handle: nodejs-ecosystem
created_at: '2019-10-17T15:59:05.529Z'
disclosed_at: '2020-01-11T12:05:44.281Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
asset_identifier: hexo-admin
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS (Hexo-admin plugin)

## Metadata

- HackerOne Report ID: 716570
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: nodejs-ecosystem
- Disclosed At: 2020-01-11T12:05:44.281Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report  Stored XSS in Hexo-admin
It allows The Post editor functionality in the hexo-admin plugin 3.9.0 for Node.js is vulnerable to stored XSS via the content of a post.

# Module

**module name:** Hexo-admin
**version:** 3.9.0
**npm page:** `https://www.npmjs.com/package/hexo-admin

## Module Description

An admin UI for the Hexo blog engine. Based off of the Ghost interface, with inspiration from svbtle and prose.io.

## Module Stats

> Replace stats below with numbers from npm’s module page:

[1] 216

# Stored XSS

## Stored XSS occurs when a malicious script is injected directly into a vulnerable web application.

Description about how the vulnerability was found and how it can be exploited, how it harms package users (data modification/lost, system access, other.

## Steps To Reproduce:

Steps of reproduction
==========================
1. Prerequisites are
    - hexojs (Static blog generator)
    - hexo-admin plugin (https://github.com/jaredly/hexo-admin)

2. Start the hexo server from website directory (command: hexo server -d)
3. Access hexo admin panel at localhost:4000/admin
4. Click on the posts section
5. Create the new post and give it a title (Test XSS here) 
6. In the post content you can put the below payloads
    1.  "><img src=x onerror=alert("XSS")>
    2.  "><img src=x onerror=alert(document.domain)>
7. You'll get the XSS pop-up in the post editor
8. Save the post and rebuilt the pages with for changes
9. To generate again, apply below commands
     1. hexo clean
     2. hexo generate
     3. hexo server -d
10. Go to your post "Test XSS"
11. You'll get the XSS pop-up there every time you open that page because it is stored.

## Patch

> NA

## Supporting Material/References:


- Ubuntu
- 12.11.1
- 6.11.3
- Mozilla

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: Y
- I opened an issue in the related repository: Y 

> Notes:
Hey I've already reported the vulnerability to npm security team directly just wanted to report on hackerone. you can cross verify it with my email. I hope you make it a triaged. sorry for the delay.
this is a github issue (https://github.com/jaredly/hexo-admin/issues/185)

## Impact

Stored XSS allows an attacker to embed a malicious script into a vulnerable page, which is then executed when a victim views the page.

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
