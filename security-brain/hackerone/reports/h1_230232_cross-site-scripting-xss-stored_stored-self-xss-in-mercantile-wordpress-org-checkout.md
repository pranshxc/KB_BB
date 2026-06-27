---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '230232'
original_report_id: '230232'
title: Stored self-XSS in mercantile.wordpress.org checkout
weakness: Cross-site Scripting (XSS) - Stored
team_handle: wordpress
created_at: '2017-05-20T13:40:03.593Z'
disclosed_at: '2017-07-14T06:49:11.979Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored self-XSS in mercantile.wordpress.org checkout

## Metadata

- HackerOne Report ID: 230232
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: wordpress
- Disclosed At: 2017-07-14T06:49:11.979Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,

**Summary**
after i read this #221893 report, i try to find more security issue there, and i was surprise i found an RCE Via Template Injection. Since on that report i see `ng-bindable` word, its possible the site also effect by RCE.

**Step To Reproduce**

1. open https://mercantile.wordpress.org and sign up for account.
2. after finish sign up navigate to `https://mercantile.wordpress.org/my-account/edit-account/` to field your first and last name
3. now navigate again to `https://mercantile.wordpress.org/my-account/edit-address/`
4. field all form for Billing Address with `{{1+1}}` except the `zip code` and field all form with `{{1==1}}` for the Shipping Address. and press save.

{F186514}   

5. now try to make an order by select any product till process or step to `https://mercantile.wordpress.org/checkout/`
6. there you will see, the code `{{1+1}}` that we have field in the form for address bellow is execute as `2` automaticly there. and the `{{1==1}}` in shipping address will be execute as `true` .

{F186513}

This is a vulnerability about Flask Template Engine(Jinja2) Injection or Angular JS Template Injection , more detail can be seen in these blogs for your Reference:

1. https://nvisium.com/blog/2016/03/09/exploring-ssti-in-flask-jinja2/
2. https://nvisium.com/blog/2016/03/11/exploring-ssti-in-flask-jinja2-part-ii/
3. http://blog.portswigger.net/2016/01/xss-without-html-client-side-template.html

Best Regards,

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
