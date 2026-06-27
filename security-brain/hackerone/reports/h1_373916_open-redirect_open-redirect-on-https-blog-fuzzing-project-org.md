---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '373916'
original_report_id: '373916'
title: Open redirect on https://blog.fuzzing-project.org
weakness: Open Redirect
team_handle: hannob
created_at: '2018-06-29T13:16:49.176Z'
disclosed_at: '2018-11-10T11:54:30.841Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
asset_identifier: '*.fuzzing-project.org'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Open redirect on https://blog.fuzzing-project.org

## Metadata

- HackerOne Report ID: 373916
- Weakness: Open Redirect
- Program: hannob
- Disclosed At: 2018-11-10T11:54:30.841Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

There is an Open Redirect on  https://blog.fuzzing-project.org/exit.php?url= due to the application not checking the value passed by the user to the "url" parameter.

**Description:**

Unchecked redirects occur when an application redirects to a destination controlled by attackers. This often occurs in functionality returning users to a previous page, e.g. after authenticating.

An attacker can control the value of the "url" parameter and make it redirect to a malicious endpoint.

https://blog.fuzzing-project.org/exit.php?url=

## Steps To Reproduce:

Here is a proof of concept to demonstrate how an open redirect occurs. Please note that this particular example is not a vulnerability and just here for demonstration purposes.

PoC: https://blog.fuzzing-project.org/exit.php?url=aHR0cHM6Ly93d3cuaW5mb3NlYy5jb20uYnI=

The URL looks like it should go to https://blog.fuzzing-project.org, but you are redirected to https://www.infosec.com.br

## Supporting Material/References:

Mitigation:

When possible, do not allow user input to directly control redirect destinations; rather, generate them on the server side (e.g. via ID -> URL mapping). When this is not an option, a strict whitelist is highly recommended. Finally, a last-ditch mitigation can be performed by removing protocol specifiers from user input prior to redirection. This last method will not fix intra-site redirect exploits, but can prevent redirects to an attacker-controlled website.

Reference:

https://www.owasp.org/index.php/Unvalidated_Redirects_and_Forwards_Cheat_Sheet

## Impact

Attackers may be able to use this to execute believable phishing attacks, bypass authentication, or (in rare circumstances) violate CSRF mitigations.

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
