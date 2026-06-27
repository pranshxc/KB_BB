---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1110229'
original_report_id: '1110229'
title: Reflected/Stored XSS on duckduckgo.com
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: duckduckgo
created_at: '2021-02-24T15:19:33.392Z'
disclosed_at: '2021-04-10T18:15:50.202Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 131
asset_identifier: '*.duckduckgo.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected/Stored XSS on duckduckgo.com

## Metadata

- HackerOne Report ID: 1110229
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: duckduckgo
- Disclosed At: 2021-04-10T18:15:50.202Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi DuckDuckGo,

While browsing normally (since I use DuckDuckGo on a daily basis), I discovered an interesting stored XSS on the duckduckgo main search engine. A payload that somebody had left on urbandictionary.com had triggered a HTML injection, and a stored XSS as a result. 

**Steps to Reproduce**
1. Search the following in the searchbar of DuckDuckGo: `urban dictionary "><img src=x<`
2. A payload left by someone else will render itself and fire in the main DuckDuckGo page.
3. It is also possible to visit the page via the DuckDuckGo URL as [such](https://duckduckgo.com/?q=urban+dictionary+%22%3E%3Cimg+src%3Dx%3C&t=ffab&atb=v1-1&ia=web) and the XSS will trigger.

**POC**
- The page itself renders HTML. The payload fires.
- {F1207848}
- {F1207849}

## Impact

There are several impacts here.
- Firstly, the DuckDuckGo URL serves as a payload, because simply visiting the page with the right search parameter triggers the XSS, although the search parameters themselves do not directly trigger it. 
- Secondly, the XSS is stored in the search results, so this can be considered to be Stored XSS.
- It is possible to execute any Javascript via the main DuckDuckGo page.

If you have any questions or require clarification, I am happy to help.
Cheers,
PMOC

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
