---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '148741'
original_report_id: '148741'
title: Stored Cross-Site-Scripting in CMS Airship's  authors profiles
weakness: Cross-site Scripting (XSS) - Generic
team_handle: paragonie
created_at: '2016-07-01T18:39:17.554Z'
disclosed_at: '2016-07-01T18:59:30.269Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 24
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored Cross-Site-Scripting in CMS Airship's  authors profiles

## Metadata

- HackerOne Report ID: 148741
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: paragonie
- Disclosed At: 2016-07-01T18:59:30.269Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I'm just checking out CMS Airship and some of the security features look pretty nice. Awesome job on that!

After clicking around a bit I stumbled however upon a stored XSS vulnerability in the Bridge.  As per `/bridge/help` I use 1.1.0 version (installed via Docker), as I couldn't find any reference with regard to this in the 1.1.1 changelog from https://github.com/paragonie/airship/commit/29dc60a1b0178222c3c984915f2eda6322ca3453 I believe that it probably is affected as well.

To reproduce this:

1. Install CMS Airship
2. Make sure to use the default settings (or at least do not uncheck "Enable registration")
3. Take another browser tab and go to http://localhost:8081/bridge/board to register a new account
4. Login with that account at http://localhost:8081/bridge/login
5. Go to http://localhost:8080/bridge/author/new
6. Create a new author with the name "<script>alert(1)</script>"
7. Send the author edit link to another user, such as the captain user (e.g. http://localhost:8080/bridge/author/edit/3)
8. Open it as captain

Then you see the XSS executed, or well, if your browser supports CSP a decent CSP warning in your browser console :-)

{F102848}

The HTML in question is:

```
    <div id="bridge_main">    <h2>Edit Author "<script>alert(1)</script>" Details</h2>
<form method="post"><input type="hidden" name="_CSRF_TOKEN" value="ijYiRqBM1DKBw9Kevvn4zjEw:frKdBMZxXK3VUgI0ZEuQHdHerw9NnVwTx8a62QiJhiY3" />
    <div class="table full-width table-pad-1">
        <div class="table-row">
            <div class="table-cell table-label">
                <label for="author_name">Author Name:</label>
            </div>
            <div class="table-cell">
                <input class="full-width" id="author_name" name="name" placeholder="e.g.&#x20;Information&#x20;Technology&#x20;Department" value="&lt;script&gt;alert&#x28;1&#x29;&lt;&#x2F;script&gt;" type="text" />
            </div>
        </div>
```

Since I don't have libsodium and PECL installed locally on my dev machine I couldn't include a tested patch for this. Sorry :-)

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
