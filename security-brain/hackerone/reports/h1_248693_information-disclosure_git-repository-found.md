---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '248693'
original_report_id: '248693'
title: Git repository found
weakness: Information Disclosure
team_handle: grab
created_at: '2017-07-12T12:46:57.897Z'
disclosed_at: '2017-08-13T18:55:41.147Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 37
tags:
- hackerone
- information-disclosure
---

# Git repository found

## Metadata

- HackerOne Report ID: 248693
- Weakness: Information Disclosure
- Program: grab
- Disclosed At: 2017-08-13T18:55:41.147Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Git metadata directory (.git) was found in this folder. An attacker can extract sensitive information by requesting the hidden metadata directory that version control tool Git creates. The metadata directories are used for development purposes to keep track of development changes to a set of source code before it is committed back to a central repository (and vice-versa). When code is rolled to a live server from a repository, it is supposed to be done as an export rather than as a local working copy, and hence this problem.

Repository files/directories: 
.gitignore
README.md
ansible/Vagrantfile
ansible/development
ansible/host_vars/development
ansible/host_vars/production
ansible/production
ansible/provision.yml
ansible/roles/common/files/id_rsa
ansible/roles/common/tasks/main.yml

GET /wp-content/themes/.git/config HTTP/1.1
Host: 54.255.134.3:443
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.21
Accept: */*

These files may expose sensitive information that may help an malicious user to prepare more advanced attacks.


Remove these files from production systems or restrict access to the .git directory. To deny access to all the .git folders you need to add the following lines in the appropriate context (either global config, or vhost/directory, or from .htaccess):
<Directory ~ "\.git">
Order allow,deny
Deny from all
</Directory>

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
