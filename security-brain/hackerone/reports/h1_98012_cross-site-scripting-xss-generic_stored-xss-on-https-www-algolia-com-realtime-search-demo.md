---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '98012'
original_report_id: '98012'
title: Stored XSS on https://www.algolia.com/realtime-search-demo/*
weakness: Cross-site Scripting (XSS) - Generic
team_handle: algolia
created_at: '2015-11-05T09:20:15.131Z'
disclosed_at: '2016-02-03T22:15:05.264Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS on https://www.algolia.com/realtime-search-demo/*

## Metadata

- HackerOne Report ID: 98012
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: algolia
- Disclosed At: 2016-02-03T22:15:05.264Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

__Description__

When you generate a UI demo, the values of the Attributes are not escaped when printed in the page of the demo.
There is a protection by CloudFlare, but because the values of the Attributes are printed in Javascript code, I found a way to abuse this to execute Javascript code.  Seems like ClodFlare is a little more permissive when the malicious code is in the name of the parameter instead of the value: `'+something+'` is allowed.

__Proof of concept__

1. Using an existing user, go to https://www.algolia.com/explorer.
2. At the bottom of  the right side of the page click on _GENERATE A UI DEMO_.
3. Enter any _Title_.
4. Click on _NEXT_.
5. Right click the field for _Primary attribute_ and click on _Inspect Element_.
6. Change the _name_ of the `<input>` to:

        engine[primary_attribute]['+document.write`${unescape`%3cimg%20src%3dx%20onerror%3dalert%28document.domain%29%3e`}`+']

7. Click on _NEXT_.
8. Click on _GENERATE UI & SHARE_.
9. `alert(document.domain)` is executed.
10. Copy the address from the address bar of your browser.
11. Open the link with other user.
12. `alert(document.domain)` is executed.

I noticed that the same issue is with the other Attributes fields.

I have a live demo here https://www.algolia.com/realtime-search-demo/some-title.
Please, let me know if something is not clear.

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
