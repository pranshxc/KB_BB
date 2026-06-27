---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6369'
original_report_id: '6369'
title: Stored XSS {dangerous?} https://www.khanacademy.org/coach/roster/?listId=allStudents
weakness: Cross-site Scripting (XSS) - Generic
team_handle: khanacademy
created_at: '2014-04-07T23:30:32.675Z'
disclosed_at: '2014-04-09T17:00:08.473Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS {dangerous?} https://www.khanacademy.org/coach/roster/?listId=allStudents

## Metadata

- HackerOne Report ID: 6369
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: khanacademy
- Disclosed At: 2014-04-09T17:00:08.473Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

when you go to https://www.khanacademy.org/coach/roster/?listId=allStudents and press on add class you have the possebility to add a class (obvious). when you name it "><img src=x onerror=alert(4)> it will stay persistent.

quite dangerous

Best regards,

Olivier Beg

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
