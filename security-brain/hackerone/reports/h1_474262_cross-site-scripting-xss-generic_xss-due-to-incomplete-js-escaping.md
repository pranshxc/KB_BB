---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '474262'
original_report_id: '474262'
title: XSS due to incomplete JS escaping
weakness: Cross-site Scripting (XSS) - Generic
team_handle: rails
created_at: '2019-01-03T10:28:41.554Z'
disclosed_at: '2020-05-14T23:02:44.214Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
asset_identifier: https://github.com/rails/rails
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS due to incomplete JS escaping

## Metadata

- HackerOne Report ID: 474262
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: rails
- Disclosed At: 2020-05-14T23:02:44.214Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

`ActionView::Helpers::JavaScriptHelper` inside ` rails/actionview/lib/action_view/helpers/javascript_helper.rb` provides JS escaping in Rails, but fails to protect template literal strings. As such, there are two ways XSS can occur:

###XSS via template literal break out:
1) Create a view with the following code: 
```
<script>let a = `<%= j '`+alert`' %>`</script>
```
2) The alert will execute because backticks aren't escaped.

###XSS via template literal placeholder evaluation:
1) Create a view with the following code:
```
<script>let a = `<%= j '${alert()}' %>`</script>
```
2) The alert will execute because `${expression}` isn't escaped
(escaping `$` with `\$` seems sufficient)

## Impact

Attackers can leverage this weakness to [steal private information, hijack accounts and distribute malware](https://chefsecure.com/blog/the-12-exploits-of-xss-mas-infographic) by injecting malicious code instead of an alert.

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
