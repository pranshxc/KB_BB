---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1631447'
original_report_id: '1631447'
title: STORED XSS in █████████/nlc/login.aspx via "edit" GET parameter through markdown
  editor [HtUS]
weakness: Cross-site Scripting (XSS) - Stored
team_handle: deptofdefense
created_at: '2022-07-08T15:04:51.953Z'
disclosed_at: '2022-09-14T21:13:53.142Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# STORED XSS in █████████/nlc/login.aspx via "edit" GET parameter through markdown editor [HtUS]

## Metadata

- HackerOne Report ID: 1631447
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: deptofdefense
- Disclosed At: 2022-09-14T21:13:53.142Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

While looking through the source code of https://████████/nlc/login.aspx,I noticed this line (204):
`<a id="ctl00_ContentPlaceHolder1_CancelButton" class="hidden" href="login.aspx?edit=false"><i class="fa fa-times"></i> Cancel</a>`  ,which exposes the **edit** GET parameter.
Upon accessing https://█████████/nlc/login.aspx?edit=true ,a hidden markdown editor will be revealed if you click around where the bottom text is,which allow us to input our own text,upload images,and pretty much anything you can do in markdown.  
████████  
As you can see to prove impact,I inputted an XSS payload(`svg/onload=alert(1)>`) and clicked on **Save**.
After that whenever **anyone** accesses https://██████████/nlc/login.aspx ,the XSS payload will execute.  
███████  
The only way to remove the XSS payload is through accessing the markdown editor through https://█████████/nlc/login.aspx?edit=true ,removing it,and saving it.

## Impact

Using this,an attacker is able to input and execute his own javascript code that will execute on **everyone** that accesses the login page **every time**,no matter what device they're using.They are not limited to Stored XSS though,using the hidden markdown editor they're able to upload images,deface the website and basically anything you can using markdown,however the most impactful scenario being executing arbitrary javascript code.

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
