---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '899069'
original_report_id: '899069'
title: Untrusted users able to run pending migrations in production
weakness: Uncontrolled Resource Consumption
team_handle: rails
created_at: '2020-06-15T22:43:10.080Z'
disclosed_at: '2020-07-24T20:07:32.367Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: https://github.com/rails/rails
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Untrusted users able to run pending migrations in production

## Metadata

- HackerOne Report ID: 899069
- Weakness: Uncontrolled Resource Consumption
- Program: rails
- Disclosed At: 2020-07-24T20:07:32.367Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Untrusted users able to run pending migrations in production

There is a vulnerability in versions of Rails prior to 6.0.3.2 that allowed
an untrusted user to run any pending migrations on a Rails app running in
production.

This vulnerability has been assigned the CVE identifier CVE-2020-XXXX.

Versions Affected:  6.0.0 < rails < 6.0.3.2
Not affected:       Applications with `config.action_dispatch.show_exceptions = false` (this is not a default setting in production)
Fixed Versions:     rails >= 6.0.3.2


Releases
--------

The new release (6.0.3.2) is available in the regular locations.

Workarounds
-----------

Until such time as the patch can be applied, application developers should
disable the ActionDispatch middleware in their production environment via
a line such as this one in their config/environment/production.rb:

config.middleware.delete ActionDispatch::ActionableExceptions

Patches
-------

As mentioned, we are releasing the following patch for the 6.0 release
series:

* 0001-6.0.3.1-Only-allow-ActionableErrors-if-show_detailed_excepti.patch


Credits
-------

This issue was discovered independently by Rafael França and Benoit Côté-Jodoin. 
The patch above was provided by Rafael.

## Impact

Using this issue, an attacker would be able to execute any migrations that 
are pending for a Rails app running in production mode. It is important to
note that an attacker is limited to running migrations the application 
developer has already defined in their application and ones that have not
already ran.

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
