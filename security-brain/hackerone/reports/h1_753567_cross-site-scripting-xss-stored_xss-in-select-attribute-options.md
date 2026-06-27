---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '753567'
original_report_id: '753567'
title: XSS in select attribute options
weakness: Cross-site Scripting (XSS) - Stored
team_handle: concretecms
created_at: '2019-12-07T09:50:11.597Z'
disclosed_at: '2020-04-29T13:43:08.005Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 20
asset_identifier: https://github.com/concrete5/concrete5
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# XSS in select attribute options

## Metadata

- HackerOne Report ID: 753567
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: concretecms
- Disclosed At: 2020-04-29T13:43:08.005Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## To reproduce
1. Create a new select attribute.
2. Add a select attribute option with value `<script>alert('XSS')</script>` and hit Save.
3. Edit the newly created attribute again and see XSS dialog.

The vulnerability lays in the type_form.php file, see https://github.com/concrete5/concrete5/blob/develop/concrete/attributes/select/type_form.php#L40

## Unauthenticated use
The vuln can be pretty bad if the website has an Express Form with select attribute associated with it that "Allow users to add to this list.". In that case, an (unauthenticated) user can submit a form that results to stored XSS.

## Screenshot
{F653172}

## Impact

Stored XSS on /index.php/dashboard/pages/attributes/edit/xxx page and when editing an Express Form block.

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
