---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '148853'
original_report_id: '148853'
title: Stored XSS using  SVG
weakness: Cross-site Scripting (XSS) - Generic
team_handle: paragonie
created_at: '2016-07-02T12:25:01.829Z'
disclosed_at: '2016-07-02T18:01:30.624Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS using  SVG

## Metadata

- HackerOne Report ID: 148853
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: paragonie
- Disclosed At: 2016-07-02T18:01:30.624Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi , 

Background 
------------------------------------

I had problem in setup the airship at ubuntu so I tested on your site .  
If you uploads any file thet can use for XSS (HTML,SWF,etc) the content type will change to "text/plain; charset=us-ascii" . But for images it will stay the same . so if you upload SVG with JS content it will work fine ! 

The "Content-Type: image/svg+xml; charset=us-ascii" header will make this attack works . 

Just upload the svg file to the site . 

PoC
---------------

{F102954}


SVG's  is not good sometimes to view as image and it will be stored in users accounts.

Thanks

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
