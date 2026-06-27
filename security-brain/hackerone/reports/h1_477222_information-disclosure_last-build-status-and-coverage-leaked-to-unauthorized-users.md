---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '477222'
original_report_id: '477222'
title: Last build status and coverage leaked to unauthorized users
weakness: Information Disclosure
team_handle: gitlab
created_at: '2019-01-09T19:52:23.194Z'
disclosed_at: '2019-09-01T18:06:10.339Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 23
asset_identifier: gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Last build status and coverage leaked to unauthorized users

## Metadata

- HackerOne Report ID: 477222
- Weakness: Information Disclosure
- Program: gitlab
- Disclosed At: 2019-09-01T18:06:10.339Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

GitLab CI supports creating badges for the latest build/coverage on a certain branches. However, with restricted access, where users do not have access to pipelines, users still have access to the build/coverage status of any branch.
This access works for different configurations:

1. For public projects with restricted pipeline access, any user (the user does not need to be signed in) has access to this information
2. For internal projects with restricted pipeline access, any authenticated user has access to this information
3. For private projects, any Guest user of that project has access to this information

## Steps to reproduce

1. Create a public repo, configure CI, and push some code. Consider the project namespace to be `test/cibadges` in these steps.
2. Restrict the visibility of whole repo to `Project Members Only` and disable `Public builds` in the CI settings
3. As a non-authenticated user visit the following page: `https://example.gitlab.com/test/cibadges/badges/master/pipeline.svg`

This will return a SVG image showing the build status of the `master` branch. This works for any other branch as well. The same thing also works with the coverage badge accessible via the following link `https://example.gitlab.com/test/cibadges/badges/master/coverage.svg`
The same works for the other configurations as mentioned above.

Even if repos and therefore also pipelines are completely disabled, the last build status/coverage still can be retrieved via the badges link.

## Steps to mitigate

Perform proper authorization check handling a badge request

## Impact

Users with restricted pipeline access can see the build/coverage status for different branches

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
