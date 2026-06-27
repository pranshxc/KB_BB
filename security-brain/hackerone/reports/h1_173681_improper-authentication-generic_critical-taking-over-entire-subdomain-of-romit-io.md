---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '173681'
original_report_id: '173681'
title: '[CRITICAL]-Taking over entire subdomain of romit.io'
weakness: Improper Authentication - Generic
team_handle: enter
created_at: '2016-10-03T16:17:52.265Z'
disclosed_at: '2016-10-03T17:24:46.821Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 33
tags:
- hackerone
- improper-authentication-generic
---

# [CRITICAL]-Taking over entire subdomain of romit.io

## Metadata

- HackerOne Report ID: 173681
- Weakness: Improper Authentication - Generic
- Program: enter
- Disclosed At: 2016-10-03T17:24:46.821Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi, 

During recon, I found out that `blog.romit.io` was not mapped with `wordpress.com` and the domain was   returning back error like `this domain has not been mapped with wordpress.com, to map it please login into wordpres.com`. 

So, I quickly created an account on `wordpress.com` and mapped `blog.romit.io` by paying **13USD** from my credit card. 

So, **I become the admin of blog.romit.io** for just 13USD.

**Proof of concept:**

Just visit `https://blog.romit.io`. 

**Impact**: This issue can have really huge impact on the companies reputation someone can post malicious content on the blog and then romit.io users will think its official but its **NOT**. 

**FIX?**

1. You can delete the **CNAME** entry for `blog.romit.io`

or.. 

2. You can have my wordpress.com credentials. 

Please see attached screenshots.

Thanks 
-@gone

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
