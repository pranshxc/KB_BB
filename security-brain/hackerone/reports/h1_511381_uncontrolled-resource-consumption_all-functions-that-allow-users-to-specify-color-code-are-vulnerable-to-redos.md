---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '511381'
original_report_id: '511381'
title: All functions that allow users to specify color code are vulnerable to ReDoS
weakness: Uncontrolled Resource Consumption
team_handle: gitlab
created_at: '2019-03-17T23:00:46.272Z'
disclosed_at: '2019-08-21T19:23:12.570Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 50
asset_identifier: gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# All functions that allow users to specify color code are vulnerable to ReDoS

## Metadata

- HackerOne Report ID: 511381
- Weakness: Uncontrolled Resource Consumption
- Program: gitlab
- Disclosed At: 2019-08-21T19:23:12.570Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Invalid color code leads to DoS.

**Description:**
GitLab has some functions that allow users to specify color code. (e.g.: Labels/Broadcast Messages)
All those functions are vulnerable to ReDoS.
It seems that there is a problem with the [regex](https://github.com/gitlabhq/gitlabhq/blob/master/app/validators/color_validator.rb#L15) in [app\validators\color_validator.rb](https://github.com/gitlabhq/gitlabhq/blob/master/app/validators/color_validator.rb) to validate a specified color code.
An attacker can exhaust the server's CPU with this vulnerability, and cause a continuous DoS.

## Steps To Reproduce:

1. Create a project.
2. Go to `http(s)://{GitLab Host}/{userid}/{Project Name}/labels/new`.
3. Fill out `Title` form with `PoC`.
4. Click `Create label` button.
5. Intercept the request.
6. Change the value of the parameter of `label%5Bcolor%5D` to `#0...(50000 times)c0ffee`.
7. Forward the request.

Result: Can not access to GitLab service. (CPU usage rate of the server had risen to over 90%.)

Note: If the attacker sends requests continuously, DoS will be continuous.

## Supporting Material/References:
[Regular expression Denial of Service - ReDoS - OWASP](https://www.owasp.org/index.php/Regular_expression_Denial_of_Service_-_ReDoS)

## Impact

All users will not be able to access the entire GitLab service.

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
