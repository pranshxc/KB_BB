---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1210921'
original_report_id: '1210921'
title: Reflected XSS at dailydeals.mtn.co.za
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: mtn_group
created_at: '2021-05-27T16:55:09.262Z'
disclosed_at: '2021-12-24T08:49:13.986Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
asset_identifier: mtn.co.za
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS at dailydeals.mtn.co.za

## Metadata

- HackerOne Report ID: 1210921
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: mtn_group
- Disclosed At: 2021-12-24T08:49:13.986Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello MTN Group:

I found reflected XSS vi  ```category_id=```  parameter .

The server reads data directly from the HTTP request and reflects it back in the HTTP response. Reflected XSS exploits occur when an attacker causes a victim to supply dangerous content to a vulnerable web application, which is then reflected back to the victim and executed by the web browser. The most common mechanism for delivering malicious content is to include it as a parameter in a URL that is posted publicly or e-mailed directly to the victim. URLs constructed in this manner constitute the core of many phishing schemes, whereby an attacker convinces a victim to visit a URL that refers to a vulnerable site. After the site reflects the attacker's content back to the victim, the content is executed by the victim's browser.

## Steps To Reproduce:
1. visite the https://dailydeals.mtn.co.za
2. click on Categories, Then click on any items on it, now you get the ```category_id``` parameter on the URL.
3. add this payload ```3mh8r%3cimg%20src%3da%20onerror%3dalert(1)%3e``` as a value to ```category_id``` parameter 
you will get popup with vaule ```1``` as the POC image 
{F1317658}

##one link POC:
https://dailydeals.mtn.co.za/index.cfm?GO=DEALS&category_id=3mh8r%3Cimg%20src%3da%20onerror%3dalert(1)%3E

##Recommendation:
Your script should filter metacharacters from user input.

## Impact

attacker convinces a victim to visit a URL  & steal users cookies

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
