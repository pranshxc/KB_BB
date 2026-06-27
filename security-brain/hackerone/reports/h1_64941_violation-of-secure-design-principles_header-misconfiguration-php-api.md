---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '64941'
original_report_id: '64941'
title: Header Misconfiguration - PHP API
weakness: Violation of Secure Design Principles
team_handle: shopify
created_at: '2015-05-30T18:12:37.773Z'
disclosed_at: '2015-06-11T19:56:43.885Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# Header Misconfiguration - PHP API

## Metadata

- HackerOne Report ID: 64941
- Weakness: Violation of Secure Design Principles
- Program: shopify
- Disclosed At: 2015-06-11T19:56:43.885Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey,

Your index api page auth can easily be bypassed because it doesn't use proper auth practices in its PHP core. Here is the master code from Shopify: 

https://github.com/Shopify/shopify_php_api/blob/master/index.php

it says:

if (!isset($_SESSION['shop']) || !isset($_SESSION['token'])) header("Location: login.php");

This easily can be bypassed because the browser can decide to receive 301/302 redirects. and since if not logged in, the code tries to decide to redirect back to the login page, and the browser can ignore it. this can create an authentication bypass and also full path disclosure.

 I have written a similar example in my blog, http://www.paulosyibelo.com/2014/08/header-based-login-bypass.html

P.S: The issue exists not only on the index.php page, but in almost every page. (ex: https://github.com/Shopify/shopify_php_api/blob/master/login.php)

The best practice I would recommend would be creating another function instead of the header one, like:

function redirect($url){
    header("Location: $url");
    exit();
}

The easiest approch is to exit(); the code after the redirection. or else, the rest of the page still renders no matter what. I hope I don't need to provide a POC as its a crystal clear bug (also with the link).

Thanks,

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
