---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1685979'
original_report_id: '1685979'
title: DoS via Playbook
weakness: Uncontrolled Resource Consumption
team_handle: mattermost
created_at: '2022-08-31T00:41:40.539Z'
disclosed_at: '2022-11-23T14:55:52.329Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
asset_identifier: Mattermost Plugins
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# DoS via Playbook

## Metadata

- HackerOne Report ID: 1685979
- Weakness: Uncontrolled Resource Consumption
- Program: mattermost
- Disclosed At: 2022-11-23T14:55:52.329Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
A normal user can create a playbook, that has some attributes like the `run_summary_template`, `retrospective_template` and `description`,that don't have any size check or validation, which allows an attacker to set an unlimited number of characters as their values.

In a production environment is possible to set up to 50MB of data, due to the default nginx configuration, as the `run_summary_template` value. The creation of the playbook for itself is not sufficient to trigger an DoS attack in the application, but once this playbook is executed(run) the server  starts to consume a large amount of computing resources, which causes to the server to stop responding to users requests and ultimately leads to server crash.

This attack is even worst because after the application is restarted, its not possible to the user who created the playbook run to finish its execution via the Web Portal, because both the channel created by the playbook run, and the run dedicated management page, don't properly load, showing only a blank screen.

## Steps To Reproduce:
1.  Log in as a normal user in the platform.
2. Grab the user `MMAUTHTOKEN` authentication token.
3. Generate the playbook payload, that contains 50000000(50MB) characters as the `run_summary_template` attribute value. Use F1893243
4. Send the following `POST` request to the `plugins/playbooks/api/v0/playbooks` API endpoint:
```bash
curl -X POST "http://<domain>/plugins/playbooks/api/v0/playbooks" -H 'Content-Type: application/json' -d @payload --cookie "MMAUTHTOKEN=<user-auth-token>" -H "X-CSRF-TOKEN: <csrf-token>"
```
5. Go to the playbooks page, and click on the newly created playbook.
6. Click in the "Run" button and then set an name for the run.
7. After the run is initiated, the server will start to consume an abnormal quantity of computing resources, and crashes after some seconds.
8. The application becomes unavailable for all its users.

## Supporting Material/References:

  * PoC Video
{F1893242}

## Impact

A user can cause a full denial of service attack in the application server, making the application server unavailable to all its users.

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
