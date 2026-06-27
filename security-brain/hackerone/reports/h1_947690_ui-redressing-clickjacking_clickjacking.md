---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '947690'
original_report_id: '947690'
title: ClickJacking
weakness: UI Redressing (Clickjacking)
team_handle: acronis
created_at: '2020-07-30T08:40:20.903Z'
disclosed_at: '2021-03-16T09:44:10.788Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
asset_identifier: '*.acronis.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- ui-redressing-clickjacking
---

# ClickJacking

## Metadata

- HackerOne Report ID: 947690
- Weakness: UI Redressing (Clickjacking)
- Program: acronis
- Disclosed At: 2021-03-16T09:44:10.788Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

I have found the vulnerability called Clickjacking.

Please find the details below:

Description     

Clickjacking is an exploit in which malicious coding is hidden beneath apparently legitimate buttons or other clickable content on a website.

  OWASP Benchmark   A6- Security Misconfiguration  


Steps to Reproduce   

1.Craft an HTML page and add the following 
( https://www.acronis.com/en-in/ ) of the application within an iframe.

2.Save the file as *.html and run the file.

3.Open the HTML page in a browser.

4.The following attached screenshot shows webiste is in frame.

Please find the attached screenshot for your reference. 

High Level Fix Recommendation

Clickjacking attacks can be avoided by setting the X-Frame-Options header or by using frame busting code which check if the current web page is the top web page (not within a frame).

## Impact

Impact 

Multitude of attacks including key logging and stealing user credentials.

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
