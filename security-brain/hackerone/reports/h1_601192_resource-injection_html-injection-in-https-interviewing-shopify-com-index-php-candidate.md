---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '601192'
original_report_id: '601192'
title: HTML injection in https://interviewing.shopify.com/index.php?candidate=
weakness: Resource Injection
team_handle: shopify
created_at: '2019-06-05T20:40:02.405Z'
disclosed_at: '2019-07-04T17:23:00.874Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
asset_identifier: '*.shopify.com'
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
- resource-injection
---

# HTML injection in https://interviewing.shopify.com/index.php?candidate=

## Metadata

- HackerOne Report ID: 601192
- Weakness: Resource Injection
- Program: shopify
- Disclosed At: 2019-07-04T17:23:00.874Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

`https://interviewing.shopify.com/index.php?candidate=` is inserting the value of `candidate` into the DOM without any filtering (except that the equal sign can't appear in the payload), this allows attacker to injection any html in the DOM. Of course reflected XSS payloads like `<script>[...something...]</script>` will be blocked by browsers' protection, but we can still play with CSS injection:

`https://interviewing.shopify.com/index.php?candidate=z%3Cstyle%3E%20*%20{%20background:%20url(https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png);%20}`

{F503108}

## Impact

HTML injection, mostly CSS injection.

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
