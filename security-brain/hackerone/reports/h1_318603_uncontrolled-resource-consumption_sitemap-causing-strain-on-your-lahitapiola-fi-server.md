---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '318603'
original_report_id: '318603'
title: Sitemap causing strain on your Lahitapiola.fi server
weakness: Uncontrolled Resource Consumption
team_handle: localtapiola
created_at: '2018-02-22T17:19:42.970Z'
disclosed_at: '2018-06-19T17:44:31.386Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
asset_identifier: www.lahitapiola.fi
asset_type: URL
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Sitemap causing strain on your Lahitapiola.fi server

## Metadata

- HackerOne Report ID: 318603
- Weakness: Uncontrolled Resource Consumption
- Program: localtapiola
- Disclosed At: 2018-06-19T17:44:31.386Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Basic report information
**Summary:** 
Your sitemap isn't split into many other sitemaps which causes all of the sitemap URL's to start loading in just 1 Sitemap which in turn causes a big strain on your server. 

**Description:** 
It took more than 5 minutes just to load your sitemap.  That is not normal.  

**Impact:**
Servers can lockup because of this.  Look at this Github discussion about a similar issue to yours which has caused servers to lockup for another Webmaster experiencing the same issue as yours. 

https://github.com/maartenba/MvcSiteMapProvider/issues/258

## Browsers / Apps Verified In:

Google Chrome

## Steps To Reproduce:

  1. Visit http://lahitapiola.fi/sitemap.xml or https://lahitapiola.fi/sitemap.xml
  2.  You will notice just how long it takes to load your sitemap.  It takes so long that every hit on your server for Sitemap request, will harm your server CPU and other resources. 

## Additional material

 To reduce load, the sitemap can be split into many sitemaps. 

## Related reports, best practices

## Impact

This impacts your ability to run your web applications efficiently and will thus affect your ability to run your business smoothly.

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
