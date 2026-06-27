---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1955370'
original_report_id: '1955370'
title: Incorrect handling of certain characters passed to the redirection functionality
  in Rails can lead to a single-click XSS vulnerability.
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: rails
created_at: '2023-04-20T01:32:01.375Z'
disclosed_at: '2023-07-28T00:27:41.090Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
asset_identifier: https://github.com/rails/rails
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Incorrect handling of certain characters passed to the redirection functionality in Rails can lead to a single-click XSS vulnerability.

## Metadata

- HackerOne Report ID: 1955370
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: rails
- Disclosed At: 2023-07-28T00:27:41.090Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

### Overview
Incorrect handling of certain characters passed to the redirection functionality in Rails can lead to a single-click XSS vulnerability across web applications. This has been tested on the latest version of Rails as of today (7.0.4.3).

### Description
Downstream parsing of values sent to the redirect_to function will cause the 'location' header to be removed from the response when certain characters are used in the URL. For example, if the `\b` (%08) (backspace) character is used in the URL.

When the location header is missing from the response, it is possible to control the `href` attribute in the HTML response that would normally be briefly shown prior to the redirect, therefore by using a javascript URI, it is possible to prevent the redirect and serve an XSS payload.

During the assessment, the `%01-%08, %0b, %0c, %0e-%1f` characters were found to be vulnerable, however there may be others.

We believe this may be attributed to the rack linters attempting to conform to rfc7230 (https://github.com/rack/rack/blob/f5666bc8cb13b8d731ea0222fbd3ada670f2cd55/lib/rack/lint.rb#L671)

### Proof of Concept
A simple instance is as follows:

`app/controllers/application_controller.rb`
```ruby
class ApplicationController < ActionController::Base
  def vuln
    redirect_to params[:redirect_url], allow_other_host: true
  end
end
```

`config/routes.rb`
```ruby
Rails.application.routes.draw do
  get "/vuln" => "application#vuln"
end
```

And then when we retrieve: `http://localhost:3000/vuln?redirect_url=javascript:alert()%08`

The response will be as follows:
```
HTTP/1.1 302 Found
Cache-Control: no-store
Date: Thu, 06 Apr 2023 05:16:21 GMT
Connection: close
Content-Length: 100

<html><body>You are being <a href="javascript:alert(document.cookie) ">redirected</a>.</body></html>
```

As the page does not redirect, if the user clicks on the link (expecting the redirect for example), the payload will be triggered:
{F2303758}

## Impact

User controlled values being sent to the `redirect_to` function may cause an unwanted XSS vulnerability. This was discovered in the wild and proven to be a legitimate security concern.

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
