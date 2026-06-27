---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '146948'
original_report_id: '146948'
title: Clickjacking login page of http://book.zomato.com/
weakness: UI Redressing (Clickjacking)
team_handle: zomato
created_at: '2016-06-24T05:50:20.989Z'
disclosed_at: '2017-05-18T16:55:58.640Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- ui-redressing-clickjacking
---

# Clickjacking login page of http://book.zomato.com/

## Metadata

- HackerOne Report ID: 146948
- Weakness: UI Redressing (Clickjacking)
- Program: zomato
- Disclosed At: 2017-05-18T16:55:58.640Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

The login page on book.zomato.com (http://book.zomato.com/account/login.aspx) is vulnerable to a clickjacking attack.

### Reproduction steps:

1. Paste the following HTML into a text editor and save the file as .html

```
<html>
<body>
<iframe src="http://book.zomato.com/account/login.aspx" width="500" height="500">
</body>
</html>
```

2. Open the file in a web browser
3. Note that the iframe appears with the login page inside

### Remediation:
Using the X-Frame-Options header.

OWASP: https://www.owasp.org/index.php/Clickjacking_Defense_Cheat_Sheet

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
