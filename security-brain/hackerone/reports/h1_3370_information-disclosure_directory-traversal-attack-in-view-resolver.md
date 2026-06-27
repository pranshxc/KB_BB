---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '3370'
original_report_id: '3370'
title: Directory traversal attack in view resolver
weakness: Information Disclosure
team_handle: rails
created_at: '2014-03-06T11:13:20.634Z'
disclosed_at: '2015-07-09T19:15:27.083Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- information-disclosure
---

# Directory traversal attack in view resolver

## Metadata

- HackerOne Report ID: 3370
- Weakness: Information Disclosure
- Program: rails
- Disclosed At: 2015-07-09T19:15:27.083Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

There seems to be two cases that allow directory traversal when using wildcard URL segments that allow rendering view outside view paths.

For example, let say there is a route

	get '/help/(*action)’, controller: ‘help’

and a matching controller

	class HelpController < ApplicationController
	end

This renders all views that are in 'app/views/help’ (assuming default view paths) even when matching action method is not defined.

If an attacker made a request `GET /help/../../../Gemfile`, ActionView::FileSystemResolver returns Gemfile from project root as the matching view. This simple case can be prevented using Rack::Protection::PathTraversal middleware, but it is not enabled by default in Rails. Also, there could be other mechanisms that may result in rendering views that are outside view path. Not sure if that’s the expected behaviour, but this surprised me.

However, Rack::Protection::PathTraversal can be bypassed using backslashes: `GET /help/%5c../%5c../%5c../Gemfile`. The resolver uses Dir.glob, which escapes backslashes unless File::FNM_NOESCAPE flag is used. Rack::Protection::PathTraversal won’t intercept `'\../'` and the resolver treats `'\../`' as `'../'`.

Attached are fixes for the mentioned vulnerabilities with test cases.

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
