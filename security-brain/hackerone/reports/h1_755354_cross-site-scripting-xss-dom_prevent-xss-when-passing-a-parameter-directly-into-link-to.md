---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '755354'
original_report_id: '755354'
title: Prevent XSS when passing a parameter directly into link_to
weakness: Cross-site Scripting (XSS) - DOM
team_handle: rails
created_at: '2019-12-10T18:00:07.892Z'
disclosed_at: '2020-05-13T18:19:25.408Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
asset_identifier: https://github.com/rails/rails
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# Prevent XSS when passing a parameter directly into link_to

## Metadata

- HackerOne Report ID: 755354
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: rails
- Disclosed At: 2020-05-13T18:19:25.408Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

*Note: I would say this is perhaps more of a feature request than an actual vulnerability, but Rafael França deleted this from GitHub and asked to submit it here instead*

In a rails views it's easy to accidentally create an XSS vulnerability by using the following in a template:
`<%= link_to 'Back', params[:back] %>`

Doing this exposes the app to an attack that can easily be demonstrated by simply adding this to URL of that view:
`?back=javascript%3Aalert%28boom%29%3B`

I think it would be good if rails detects this situation and filters the link_to parameter if it's from an untrusted source. The attached two-line patch does this by only allowing the HTTP(S) protocol in that case.

## Impact

If a programmer inadvertently passes a parameter directly into link_to then this would leave his site open to an XSS attack. Since rails filters untrusted parameters in many other situations it may not be apparent to the casual observer that link_to does not filter javascript.

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
