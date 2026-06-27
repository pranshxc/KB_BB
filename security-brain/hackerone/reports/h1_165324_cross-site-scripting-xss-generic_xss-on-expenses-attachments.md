---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '165324'
original_report_id: '165324'
title: XSS on expenses attachments
weakness: Cross-site Scripting (XSS) - Generic
team_handle: harvest
created_at: '2016-09-02T16:11:24.601Z'
disclosed_at: '2016-11-27T16:41:01.760Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS on expenses attachments

## Metadata

- HackerOne Report ID: 165324
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: harvest
- Disclosed At: 2016-11-27T16:41:01.760Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Summary
------
Hey there! 
After  #152591 was fixed, I decided to take another look at the attachments and found a new bypass to upload attachments which will be served with a user-controlled `Content-type`. 

The invoices attachments are not vulnerable, as they are all served with `Content-Disposition: attachment;`. 

However, the expense receipts are served inline if we provide a content-type which includes `image/jpeg`. Then we simply need to force the browser to not interpret it as an image, this can be done by supplying `text/html image/jpeg` as content-type. The image/jpeg will just be ignored (tested on firefox and chrome).

Steps to reproduce
------
1. Create a new expense and add a receipt.
2. Intercept the POST request and modify the `receipt` parameter to look like this:

    ```{bash}
Content-Disposition: form-data; name="receipt"; filename="blabla"
Content-Type: text/html image/jpeg

    <script>alert(document.domain);</script>
```
3. It will create the expense and return you a URL for viewing the receipt. Open the url and you should see the XSS

Impact
-------
Expenses can be created by regular users, therefore they could XSS their admins. However, I don't see a feature to publicly share an expense like the invoices in #152591, so I guess you can not use it to XSS cross-app.

**Note**: This bypass works also on the invoices attachments. But since they are served as attachments, no XSS is possible as far as I can tell.

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
