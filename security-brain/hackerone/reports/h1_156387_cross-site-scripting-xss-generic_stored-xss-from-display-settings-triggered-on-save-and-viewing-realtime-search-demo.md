---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '156387'
original_report_id: '156387'
title: Stored XSS from Display Settings triggered on Save and viewing realtime search
  demo
weakness: Cross-site Scripting (XSS) - Generic
team_handle: algolia
created_at: '2016-08-03T23:24:17.569Z'
disclosed_at: '2016-09-07T08:34:23.049Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS from Display Settings triggered on Save and viewing realtime search demo

## Metadata

- HackerOne Report ID: 156387
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: algolia
- Disclosed At: 2016-09-07T08:34:23.049Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Here are the steps to trigger the XSS:

1. Create a JSON record that will contain the following attribute:
     **{"<img src=1 onerror=alert(document.domain)>": "XSS attribute"}**

2. Go to  **Indices -> Display** and select the attribute **<img src=1 onerror=alert(document.domain)>** under **Attributes for Faceting** and click save. 

3. Note that XSS is triggered multiple times on that page.

4. XSS  is now triggered on **https://www.algolia.com/explorer#?index=index_name** as it also shows the attribute.

5. Create a public UI Demo and to the public url, xss is triggered. I've created a demo url:  https://www.algolia.com/realtime-search-demo/xsstest

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
