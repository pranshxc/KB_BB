---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '106293'
original_report_id: '106293'
title: Reflective XSS on wholesale.shopify.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2015-12-21T10:15:55.716Z'
disclosed_at: '2015-12-21T23:26:59.805Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflective XSS on wholesale.shopify.com

## Metadata

- HackerOne Report ID: 106293
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2015-12-21T23:26:59.805Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

There is a reflected XSS issue on wholesale.shopify.com

Steps to reproduce:
Call the following URL in Mozilla Firefox:
https://wholesale.shopify.com/asd%27%3Balert%28%27XSS%27%29%3B%27

An alert box with "XSS" appears. This means that an attacker has full control of the scripts, that are executed in the victims browser.

An attack vector would be sending an evil link via e-mail, messenger, etc. As the victim trusts the domain wholesale.shopify.com, it will click the link and could be redirected to a site hosting a browser exploit kit.
This abuses the trust of shopify.com

The main problem with that XSS is, that in script context the quotes, double quotes and ">" + "<" are not encoded at all.

I suggest to convert them either to hex values or escape them.

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
