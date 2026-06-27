---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '289246'
original_report_id: '289246'
title: Following links are vulnerable to clickjacking
weakness: UI Redressing (Clickjacking)
team_handle: semrush
created_at: '2017-11-10T18:29:40.983Z'
disclosed_at: '2018-01-11T09:47:45.261Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- ui-redressing-clickjacking
---

# Following links are vulnerable to clickjacking

## Metadata

- HackerOne Report ID: 289246
- Weakness: UI Redressing (Clickjacking)
- Program: semrush
- Disclosed At: 2018-01-11T09:47:45.261Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report!

**Summary:** [The below listed links, dont have X-FRAME-OPTIONS set to DENY or SAMEORIGIN and they are vulnerable to clickjacking]

**Description:** [The following url can be easily vulnerable to clickjacking]

**Browsers Verified In:**
  * [Firefox V56]
  

**Steps To Reproduce:** [add details for how we can reproduce the issue]
  1. [Run below code from browser and you will see listed links are vulnerable to clickjacking attack]
  2. [<!DOCTYPE html>
<html>

<frameset cols="25%,*,25%">
  <frame src="https://www.semrush.com/?l=us">
  <frame src="https://www.semrush.com/academy/">
  <frame src="https://www.semrush.com/ranking-factors/">
</frameset>

</html>]

**Following links are vulnerable to clickjacking**

+ https://www.semrush.com/semrush-opensearch.xml
+ https://www.semrush.com/academy/
+ https://www.semrush.com/ranking-factors/
+ https://www.semrush.com/manifest.json
+ https://www.semrush.com/?l=us
+ https://www.semrush.com/blog/
+ https://www.semrush.com/ 
+ https://www.semrush.com/prices/
+ https://www.semrush.com/.
+ https://www.semrush.com/.?l=us
  

**Supporting Material/References:**
  * Screenshot is attached with ticket

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
