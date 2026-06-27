---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '507957'
original_report_id: '507957'
title: Stored XSS on www.starbucks.com.sg/careers/career-center/career-landing-*
weakness: Cross-site Scripting (XSS) - Stored
team_handle: starbucks
created_at: '2019-03-11T15:02:21.231Z'
disclosed_at: '2019-04-10T21:20:41.032Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 37
asset_identifier: www.starbucks.com.sg
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS on www.starbucks.com.sg/careers/career-center/career-landing-*

## Metadata

- HackerOne Report ID: 507957
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: starbucks
- Disclosed At: 2019-04-10T21:20:41.032Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** 
While enumeration of the webpage for Starbucks I observed the following pages.

https://www.starbucks.com.sg/careers/career-center/career-landing-5?

The webpage have been highly spam by automated scanners or malicious attack.
By clicking on any of the pages it would redirect the user to a wordpress website

```
<a href="https://obatkebaskesemutan.wordpress.com/" rel="dofollow noopener" style="z-index:9999999999999999;oncontextmenu:return false;onkeydown:return false;onmousedown:return false;position:fixed;top:0px !important;left:0px;width:100%;height:100%;color:transparent !important;display:block;text-align:center;font-size:0px;background-color:transparent;background-position:center;background-repeat:no-repeat;background-size:cover;" target="_blank" title="Obat Herbal">Obat Kebas</a>

```
The owner of the following wordpress pages could manipulate user into redirecting to a Starbucks page for a job offer and an user by clicking on the webpage would redirect to a website of its choosing.

{F439338}
{F439340}

* List any recommendations for bug fix
Remove the pages from Starbucks webpage.

## Impact

The owner of the following wordpress pages could manipulate user into redirecting to a Starbucks page for a job offer and an user by clicking on the webpage would redirect to a website of its choosing.

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
