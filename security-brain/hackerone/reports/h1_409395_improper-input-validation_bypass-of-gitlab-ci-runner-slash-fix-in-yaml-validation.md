---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '409395'
original_report_id: '409395'
title: Bypass of GitLab CI runner slash fix in YAML validation
weakness: Improper Input Validation
team_handle: gitlab
created_at: '2018-09-13T11:50:47.225Z'
disclosed_at: '2019-04-10T04:33:42.240Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 355
tags:
- hackerone
- improper-input-validation
---

# Bypass of GitLab CI runner slash fix in YAML validation

## Metadata

- HackerOne Report ID: 409395
- Weakness: Improper Input Validation
- Program: gitlab
- Disclosed At: 2019-04-10T04:33:42.240Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Gitlab Security,

I notice the bug #301432 that Jobert reported earlier is could be bypassed by setting variable in environment.

The reason is that the fix in place preventing url normalization is performed by doing the YAML  validation, however this could be bypassed by setting the environment variable in `https://gitlab.com/{project_id}/settings/ci_cd`

By setting the key ONE and variable value to `../1/key`, it is possible to replicate what jobert did in #301432.

And in `.gitlab-ci.yml`

```
a:
  script:
  - echo "script"
  - echo "a"
  cache:
    key: "$ONE"
    policy: pull #or push if you like to poison
    paths:
      - .
```

Then make any change to `.gitlab-ci.yml` will trigger the bug once again.

Download from cache
{F345819}
Setting environment variable
{F345820}
Upload to cache
{F345821}

## Impact

Quoting from  #301432
```
Depending on the files that are cached, this may allow an attacker to run arbitrary code on a victim's Docker instance running a CI run. This may expose confidential data, inject artifacts in a build pipeline to ship additional code, among other things.
```

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
