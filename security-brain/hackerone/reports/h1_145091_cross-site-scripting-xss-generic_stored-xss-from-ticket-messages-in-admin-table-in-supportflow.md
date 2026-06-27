---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145091'
original_report_id: '145091'
title: Stored XSS from ticket messages in admin table in SupportFlow
weakness: Cross-site Scripting (XSS) - Generic
team_handle: iandunn-projects
created_at: '2016-06-16T05:10:25.085Z'
disclosed_at: '2016-06-28T19:44:03.912Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS from ticket messages in admin table in SupportFlow

## Metadata

- HackerOne Report ID: 145091
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: iandunn-projects
- Disclosed At: 2016-06-28T19:44:03.912Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

SupportFlow containers a stored XSS vulnerability in how it generates the admin table of tickets at _SupportFlow -> All Tickets_ (`/wp-admin/edit.php?post_type=sf_ticket`).

Any ticket can be created with an XSS payload like this:

```
<script>alert('XSS');</script>
```

When an admin goes to view the table of tickets, XSS is triggered, because the value is never escaped here:

https://github.com/SupportFlow/supportflow/blob/71a6053848c523f7b50b61a1f3770013badc76c0/classes/class-supportflow-admin.php#L1175

I've attached a screenshot demonstrating the XSS payload - please let me know if there are any questions.

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
