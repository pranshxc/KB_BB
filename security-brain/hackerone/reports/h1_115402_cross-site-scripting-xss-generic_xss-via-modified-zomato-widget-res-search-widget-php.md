---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '115402'
original_report_id: '115402'
title: XSS via modified Zomato widget (res_search_widget.php)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: zomato
created_at: '2016-02-08T15:39:16.409Z'
disclosed_at: '2016-03-11T06:17:58.904Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 0
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS via modified Zomato widget (res_search_widget.php)

## Metadata

- HackerOne Report ID: 115402
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: zomato
- Disclosed At: 2016-03-11T06:17:58.904Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Table of Contents:
1.  Short Description of Security Issue
2. Proof of Concept

#### 1. Short Description of Security Issue

The widget API endpoint at `https://www.zomato.com/widgets/res_search_widget.php` is vulnerable to XSS in the `language_id` parameter.

An attacker can create a web page that includes a Zomato widget inside an iframe with a specially crafted URL parameter that contains javascript. If a Zomato user opens this page, the iframe will load and execute the malicious javascript in the zomato.com origin using the user's active session.

This javascript can then steal a CSRF token from the zomato.com homepage and perform actions _as_ the user - actions such as inviting/removing friends, posting reviews, posting ratings and others. This can potentially be used to message other users with the malicious web page and get them to execute the malicious code, creating a sort of javascript worm or embed external malicious documents (flash, pdf, other) to continue the attack on a user's machine. On the good side, the injected javascript _may not_ steal the user's session cookie thanks to the HTTPOnly cookie parameter.

The `language_id` parameter should be filtered so that non-essential characters are removed before being output to users.

#### 2. Proof of Concept

I use a piece of javascript code that creates an alert box with the `document.domain`, which shows the SOP is bypassed: `"}');alert(document.domain);console.log('`. This code is urlencoded and inserted into the `language_id` parameter of the request like so:

```
https://www.zomato.com/widgets/res_search_widget.php?city_id=276&language_id=%22%7D%27)%3Balert(1)%3Bconsole.log(%27&theme=blue&hideCitySearch=on&hideResSearch=on&sort=popularity
```

This URL is used to create an iframe as described in Zomato's widget documentation: https://developers.zomato.com/widgets and the final code looks like this:

```
<html>
    <body>
        <iframe src="https://www.zomato.com/widgets/res_search_widget.php?city_id=273&language_id=%22%7D%27)%3Balert(document.domain)%3Bconsole.log(%27&theme=blue&hideCitySearch=on&hideResSearch=on&sort=popularity" style="position:relative;width:100%;height:100%;" border="0" frameborder="0"></iframe>
    </body>
</html>
```

Opening this html document, even locally, will run the javascript in the context of zomato.com as shown in the attached screenshot.

Let me know if you have any questions.

Best,
Matt

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
