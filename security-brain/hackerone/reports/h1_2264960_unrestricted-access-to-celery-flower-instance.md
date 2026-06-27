---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2264960'
original_report_id: '2264960'
title: Unrestricted Access to Celery Flower Instance
team_handle: exness
created_at: '2023-11-27T11:14:05.247Z'
disclosed_at: '2023-12-14T15:12:14.139Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 89
asset_identifier: api.excalls.mobi
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Unrestricted Access to Celery Flower Instance

## Metadata

- HackerOne Report ID: 2264960
- Weakness: 
- Program: exness
- Disclosed At: 2023-12-14T15:12:14.139Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

The Celery Flower instance is running and publicly accessible via the PIM mobile route /pim/flower/*. The access to this service is presently unrestricted. 

I quickly took a glance at the API to ensure that access is unrestricted. From this quick look, it appears possible to shut down a worker instance, revoke or terminate tasks, and perform other actions. In addition to unrestricted access to tasks and workers, I observed ███ via `/api/tasks` endpoint. Most importantly, the endpoint `/api/task/async-apply/*` seems to apply a task asynchronously, and there seems to be a possibility to execute arbitrary code on the Celery worker through this endpoint. I believe it's unwise for me to go beyond this since the instance is running in the prod environment, so I'm sending this quick report to you. If some form of escalation is needed for impact assessment, please let me know.

##Vulnerable Endpoint
```
https://api.excalls.mobi/pim/flower/
```

#Steps to Reproduce

```
https://api.excalls.mobi/pim/flower/api/workers
https://api.excalls.mobi/pim/flower/api/tasks
https://api.excalls.mobi/pim/flower/api/task/info/dc58fcb7-be31-4f4e-aeff-5837f0c32d30
```



#Proof of Concept
█████

████

██████


#Suggested Mitigation

Set the `flower_unauthenticated_api` environment variable to `false`

## Impact

The impact includes, but is not limited to:

1. Manipulating tasks to achieve unintended outcomes, such as disrupting or halting PIM processes.
2. ███
3. A malicious actor could continuously monitor and revoke tasks as they are created, preventing their execution and consuming resources. This could exhaust the Celery worker's resources and hinder its ability to handle legitimate tasks.
4. There seems to be a possibility to execute arbitrary code on the Celery worker by executing a task asynchronously.

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
