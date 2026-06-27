---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1256375'
original_report_id: '1256375'
title: Blog posts atom feed of a  store with password protection  can be accessed
  by anyone
weakness: Information Disclosure
team_handle: shopify
created_at: '2021-07-09T20:33:17.552Z'
disclosed_at: '2021-11-08T15:10:42.229Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 73
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Blog posts atom feed of a  store with password protection  can be accessed by anyone

## Metadata

- HackerOne Report ID: 1256375
- Weakness: Information Disclosure
- Program: shopify
- Disclosed At: 2021-11-08T15:10:42.229Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi shopify,
###DESCRIPTION
I found a issue with blog posts atom feed of a shopify store. So without password we can't access  the blog post atom feed at ```https://yourstore.myshopify.com/blogs/news.atom``` . But this can be bypass to access the atom feed of the blog posts.
For example try out this.  I have added two blog posts in my store which can't be access through https://testcheckagain.myshopify.com/blogs/news , it will just redirect you to password page or accessing atom feed give you ```401 error``` at https://testcheckagain.myshopify.com/blogs/news.atom. But it can be bypassed to check it at https://dummytext2showpoc-55204085816.shopifypreview.com/blogs/news.atom . So preview link can be exploited to get the atom feed of blog posts of password protected store. ```It can't be exploited for a partner development store```.

###STEPS
1.  Create a store at shopify.com
2. Add a blog post and make it visible.
3. If try to check the blog post atom feed in  a different machine you will be thrown ```401 error```.
4. To bypass this  try this link```https://dummytext2showpoc-store_id.shopifypreview.com/blogs/news.atom```.
5. You can the access atom feed

## Impact

Disclosing atom feed of blog posts of password protected store

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
