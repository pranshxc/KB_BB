---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '881918'
original_report_id: '881918'
title: Authenticated Stored Cross-site Scripting in bbPress
weakness: Cross-site Scripting (XSS) - Stored
team_handle: wordpress
created_at: '2020-05-24T19:39:24.327Z'
disclosed_at: '2020-06-29T10:08:42.091Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 24
asset_identifier: BBPress Core
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Authenticated Stored Cross-site Scripting in bbPress

## Metadata

- HackerOne Report ID: 881918
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: wordpress
- Disclosed At: 2020-06-29T10:08:42.091Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Description:
There exists a stored XSS vulnerability in bbPress, due to which the XSS payload which I enter in my content, gets executed at **/wp-admin/edit.php?post_type=forum**. This vulnerability requires you to be an authenticated user.

## Steps To Reproduce:
Step 1. Visit /wp-admin/edit.php?post_type=forum
Step 2. Click on **Add New**
Step 3. Write any title, and in content, write your XSS payload through the "Text" editor, rather than the "Visual" one, and publish the content.
Step 4. Now, visit /wp-admin/edit.php?post_type=forum, and you will be able to see the payload getting executed.

## Recommendations
Making use of proper functions in PHP or WordPress core in the bbPress source code regarding the filtering or sanitization of user input is a recommended way to fix this vulnerability.

## Impact

By taking an advantage of this vulnerability, an owner of a WordPress-based website would be able to execute their malicious JavaScript codes in context to the WordPress dashboard, which could result in bad issues to other users.

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
