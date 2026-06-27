---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1047447'
original_report_id: '1047447'
title: HostAuthorization middleware does not suitably sanitize the Host / X-Forwarded-For
  header allowing redirection.
weakness: Open Redirect
team_handle: rails
created_at: '2020-11-30T23:25:50.430Z'
disclosed_at: '2021-02-11T01:39:07.028Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
asset_identifier: https://github.com/rails/rails
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- open-redirect
---

# HostAuthorization middleware does not suitably sanitize the Host / X-Forwarded-For header allowing redirection.

## Metadata

- HackerOne Report ID: 1047447
- Weakness: Open Redirect
- Program: rails
- Disclosed At: 2021-02-11T01:39:07.028Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

When a site is configured to use the `.tkte.ch` (leading dot) short form for domain name, ex:

```ruby
config.hosts <<  '.tkte.ch'
```

it is then sanitized in sanitize_string, where it is turned into a regex:

```ruby
        def sanitize_string(host)
          if host.start_with?(".")
            /\A(.+\.)?#{Regexp.escape(host[1..-1])}\z/
          else
            host
          end
        end
```

The regex it is wrapped in is too permissive. It allows for things like:

```
❯ curl -i -H "Host: google.com#sub.tkte.ch" http://localhost:3001/
HTTP/1.1 302 Found
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Referrer-Policy: strict-origin-when-cross-origin
Location: http://google.com#sub.tkte.ch/
Content-Type: text/html; charset=utf-8
Cache-Control: no-cache
X-Request-Id: 3b1702ac-a58f-44bf-af8a-a2933a9946fd
X-Runtime: 0.004726
Transfer-Encoding: chunked

<html><body>You are being <a href="http://google.com#sub.tkte.ch/">redirected</a>.</body></html>
```

Where the controller is simply:

```ruby
class RedirectController < ApplicationController
  def main
    redirect_to action: 'main'
  end
end
````

The host header poisoning was reported to us by a 3rd party researcher, and tracking it down led to this.

## Impact

A user can be redirected to a hostile site.

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
