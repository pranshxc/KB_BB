---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1543718'
original_report_id: '1543718'
title: DOS via issue preview
weakness: Uncontrolled Resource Consumption
team_handle: gitlab
created_at: '2022-04-18T17:44:47.481Z'
disclosed_at: '2022-11-04T03:47:01.857Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 24
asset_identifier: https://gitlab.com/gitlab-org/gitlab
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# DOS via issue preview

## Metadata

- HackerOne Report ID: 1543718
- Weakness: Uncontrolled Resource Consumption
- Program: gitlab
- Disclosed At: 2022-11-04T03:47:01.857Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

### Summary
Previewing an issue with a specially-crafted description results in high CPU usage for 60 seconds (request timeout).
Multiple requests can be issued in parallel to create a larger impact.

### Steps to reproduce
1. Given an authorized user (on GitLab.com - anyone can self-register. On EE - depends on instance configuration).
2. Create an issue with the following description (provided a one-line python script to avoid bloating):
3. Hit the preview button.

Steps 2&3 can be accomplished via the preview_markdown API endpoint.

The script:
```python -c "print('![l' * int(1048576 / 3 - 1) + '\n')"```
Note: this is essentially the maximal description size, but a smaller number of repetitions works too.

### Impact
After 60 seconds (timeout) - the request fails.
Meanwhile, on the server end, (a single) CPU is burnt out (verified against a local EE instance).
Issuing multiple requests in parallel results in multiple CPUs burn out.
Using the DockerHub image, the entire server is completely unavailable by repeatedly sending a small number of requests repeatedly.

### Examples
The bug is instance-independent, works on latest versions. Since GitLab.com is open-core - it would work on GitLab too.

### What is the current *bug* behavior?
The HTTP request fails for timeout while the server is burning CPU.

On the code side:
```texts_and_contexts``` is being initialized here:

```
def analyze(text, context = {})
      @texts_and_contexts << { text: text, context: context }
    end
```

It is then used at banzai/reference_extractor.rb:
```
def html_documents
      ...
      @html_documents ||= Renderer.cache_collection_render(@texts_and_contexts)
      ...
```

The CPU utilization is found in the execution of ```cache_collection_render```.

### What is the expected *correct* behavior?
Fix the implementation of ```cache_collection_render```.

### Relevant logs and/or screenshots
### Output of checks
#### Results of GitLab environment info

## Impact

A complete denial of service of a GitLab EE instance.
As this vulnerability impacts GitLab.com, we assume that this vulnerability opens the door for a DDOS attack.

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
