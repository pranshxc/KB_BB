---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1050733'
original_report_id: '1050733'
title: '[sub.wordpress.com] - XSS when adjust block Poll - Confirmation Message -  On
  submission:Redirect to another webpage - Redirect address:[xss_payload]'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: automattic
created_at: '2020-12-04T17:35:43.969Z'
disclosed_at: '2021-02-11T12:43:34.372Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
asset_identifier: wordpress.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [sub.wordpress.com] - XSS when adjust block Poll - Confirmation Message -  On submission:Redirect to another webpage - Redirect address:[xss_payload]

## Metadata

- HackerOne Report ID: 1050733
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: automattic
- Disclosed At: 2021-02-11T12:43:34.372Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Dear Wordpress Team,

Today when I tried to create a post with block "Poll" and I have found at Poll Block -> Confirmation Message -> On submission:Redirect to another webpage and  Redirect address:[xss_payload]

At Redirect address line, I can save the ```javascript:alert(document.cookie)``` as an URL webpage after submit a poll. And when an authenticated wordpress user submitted a poll, their cookies may stolen by attacker

## Platform(s) Affected:
https://subdomain.wordpress.com

## Steps To Reproduce:


  1- Logged in your wordpress website and create a post with block Poll, fill question and some choices

{F1104221}
  2- Adjust Poll Block, Confirmation Message -> On submission:Redirect to another webpage and  Redirect address:javascript:alert(document.cookie) then click Update/Publish your post

{F1104220}
  3-  Go to your created poll and Submit, you will see xss popup

{F1104222}

You can see video PoC below for the steps:
{F1104231}

## Impact

Steal cookies

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
