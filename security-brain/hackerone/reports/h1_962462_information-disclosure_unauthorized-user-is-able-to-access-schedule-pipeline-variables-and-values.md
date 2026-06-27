---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '962462'
original_report_id: '962462'
title: Unauthorized user is able to access schedule pipeline variables and values
weakness: Information Disclosure
team_handle: gitlab
created_at: '2020-08-19T16:08:55.097Z'
disclosed_at: '2020-11-30T23:17:21.193Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
asset_identifier: gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Unauthorized user is able to access schedule pipeline variables and values

## Metadata

- HackerOne Report ID: 962462
- Weakness: Information Disclosure
- Program: gitlab
- Disclosed At: 2020-11-30T23:17:21.193Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

### Summary

The feature allows to add or overwrite variables that are passed to jobs  in order to modify the behavior just for that specific instance.
 
As per this https://gitlab.com/gitlab-org/gitlab-foss/-/issues/32568#note_32531510 , the current security model is
>If you are owner of schedule (as developer) or master => you can read, modify and delete,
If you are developer => you can just list, not read,

>This allows only owners and masters to read variables assigned to the schedule. It prevents other developers from hijacking schedules, but allows master to fully control them. Master already has access to Secret Variables.

But api endpoints are cleary showing this values to everyone even if the user is not part of the project. https://docs.gitlab.com/ee/api/pipeline_schedules.html#get-a-single-pipeline-schedule


### PoC

This is my test project https://gitlab.com/thevicc/trigg with schedule pipeline which custom variables you can't read.

Now, run this to read the variable and its value

`curl  --header "Private-Token: <your_access_token>"  https://gitlab.com/api/v4/projects/20618145/pipeline_schedules/69918`

Response
{F955402}

### Steps to reproduce

* Create a project and add a schedule pipeline with custom variables
*  Only you or owner can read variables
* As second account, use the api `https://docs.gitlab.com/ee/api/pipeline_schedules.html#get-a-single-pipeline-schedule`

## Impact

This bug allows unauthorized users to read scheduled pipeline custom variables and values. As per security model, this allows other devs to hijack schedules.

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
